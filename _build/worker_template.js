// LAU Edições — checkout do carrinho (Cloudflare Worker)
// Recebe o carrinho do site e cria uma página de pagamento da Stripe com todos os livros.
// Variáveis no painel da Cloudflare (Settings → Variables and Secrets):
//   STRIPE_SECRET_KEY  (Secret)  chave secreta da Stripe, sk_live_... ou sk_test_...
//   PORTES_PT          (Text)    portes para Portugal em cêntimos, ex.: 350 = 3,50€ (opcional)
//   PORTES_INT         (Text)    portes para o estrangeiro em cêntimos (opcional)
//   PORTES_GRATIS      (Text)    portes grátis a partir deste total em cêntimos (opcional)

const SITE = "https://laueditora.pt";
const CATALOGO = __CATALOGO__; // gerado a partir do site: preços confirmados aqui, nunca no browser

const cors = (origin) => ({
  "Access-Control-Allow-Origin": origin && origin.endsWith("laueditora.pt") ? origin : SITE,
  "Access-Control-Allow-Methods": "POST, OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type",
});

export default {
  async fetch(req, env) {
    const h = cors(req.headers.get("Origin"));
    if (req.method === "OPTIONS") return new Response(null, { headers: h });
    if (req.method !== "POST") return new Response("LAU checkout", { headers: h });

    let items;
    try { items = (await req.json()).items; } catch { return json({ error: "pedido inválido" }, 400, h); }
    if (!Array.isArray(items) || !items.length) return json({ error: "carrinho vazio" }, 400, h);

    const p = new URLSearchParams();
    p.append("mode", "payment");
    p.append("locale", "pt");
    p.append("success_url", SITE + "/obrigado/?s={CHECKOUT_SESSION_ID}");
    p.append("cancel_url", SITE + "/?carrinho=1");
    p.append("billing_address_collection", "auto");
    p.append("phone_number_collection[enabled]", "true");
    p.append("tax_id_collection[enabled]", "true");
    ["PT","ES","FR","DE","IT","GB","IE","NL","BE","LU","CH","AT","US","CA","BR"].forEach((c, i) =>
      p.append(`shipping_address_collection[allowed_countries][${i}]`, c));

    let total = 0, n = 0;
    for (const it of items.slice(0, 30)) {
      const b = CATALOGO[it.slug];
      const q = Math.max(1, Math.min(20, parseInt(it.q) || 1));
      if (!b) continue;
      p.append(`line_items[${n}][quantity]`, String(q));
      p.append(`line_items[${n}][price_data][currency]`, "eur");
      p.append(`line_items[${n}][price_data][unit_amount]`, String(b.cents));
      p.append(`line_items[${n}][price_data][product_data][name]`, b.name);
      p.append(`line_items[${n}][price_data][product_data][images][0]`, SITE + b.img);
      total += b.cents * q; n++;
    }
    if (!n) return json({ error: "livros desconhecidos" }, 400, h);

    const gratis = env.PORTES_GRATIS && total >= parseInt(env.PORTES_GRATIS);
    const opcoes = [];
    if (env.PORTES_PT) opcoes.push(["Envio para Portugal", gratis ? 0 : parseInt(env.PORTES_PT)]);
    if (env.PORTES_INT) opcoes.push(["Envio internacional", gratis ? 0 : parseInt(env.PORTES_INT)]);
    opcoes.forEach(([nome, valor], i) => {
      p.append(`shipping_options[${i}][shipping_rate_data][type]`, "fixed_amount");
      p.append(`shipping_options[${i}][shipping_rate_data][display_name]`, nome);
      p.append(`shipping_options[${i}][shipping_rate_data][fixed_amount][amount]`, String(valor));
      p.append(`shipping_options[${i}][shipping_rate_data][fixed_amount][currency]`, "eur");
    });

    const r = await fetch("https://api.stripe.com/v1/checkout/sessions", {
      method: "POST",
      headers: { Authorization: "Bearer " + env.STRIPE_SECRET_KEY, "Content-Type": "application/x-www-form-urlencoded" },
      body: p,
    });
    const s = await r.json();
    if (!r.ok) return json({ error: (s.error && s.error.message) || "erro na Stripe" }, 502, h);
    return json({ url: s.url }, 200, h);
  },
};

const json = (o, status, h) => new Response(JSON.stringify(o), { status, headers: { ...h, "Content-Type": "application/json" } });
