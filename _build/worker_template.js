// LAU Edições — checkout do carrinho (Cloudflare Worker)
// Recebe o carrinho do site e cria uma página de pagamento da Stripe com todos os livros.
// Variáveis no painel da Cloudflare (Settings → Variables and Secrets):
//   STRIPE_SECRET_KEY  (Secret)  chave secreta da Stripe, sk_live_... ou sk_test_...
//   PORTES_PT   portes para Portugal, em cêntimos (ex.: 350 = 3,50€)
//   PORTES_EU   portes para o resto da Europa, em cêntimos
//   PORTES_INT  portes para fora da Europa, em cêntimos
//   GRATIS_PT   portes grátis em Portugal a partir deste total, em cêntimos (ex.: 3000 = 30€)
//   GRATIS_OUTROS  portes grátis fora de Portugal a partir deste total, em cêntimos (ex.: 5000 = 50€)

const SITE = "https://laueditora.pt";
const CATALOGO = __CATALOGO__; // gerado a partir do site: preços confirmados aqui, nunca no browser

const EUROPA = ["AT","BE","BG","HR","CY","CZ","DK","EE","FI","FR","DE","GR","HU","IE","IT","LV","LT","LU","MT","NL","PL","RO","SK","SI","ES","SE","GB","CH","NO","IS","LI","AD","MC","SM","VA","AL","BA","ME","MK","RS","MD","UA"];
const RESTO = ["US","CA","BR","AR","CL","CO","MX","PE","UY","AO","MZ","CV","GW","ST","TL","ZA","MA","AU","NZ","JP","KR","CN","HK","SG","IN","IL","AE","TR"];
const ZONAS = { pt: ["PT"], eu: EUROPA, int: RESTO };

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

    let items, zona;
    try { const d = await req.json(); items = d.items; zona = d.zona; } catch { return json({ error: "pedido inválido" }, 400, h); }
    if (!Array.isArray(items) || !items.length) return json({ error: "carrinho vazio" }, 400, h);

    const p = new URLSearchParams();
    p.append("mode", "payment");
    p.append("locale", "pt");
    p.append("success_url", SITE + "/obrigado/?s={CHECKOUT_SESSION_ID}");
    p.append("cancel_url", SITE + "/?carrinho=1");
    p.append("billing_address_collection", "auto");
    p.append("phone_number_collection[enabled]", "true");
    p.append("tax_id_collection[enabled]", "true");
    if (!["pt", "eu", "int"].includes(zona)) zona = "pt";
    ZONAS[zona].forEach((c, i) => p.append(`shipping_address_collection[allowed_countries][${i}]`, c));

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

    const custo = parseInt({ pt: env.PORTES_PT, eu: env.PORTES_EU, int: env.PORTES_INT }[zona]) || 0;
    const limite = parseInt(zona === "pt" ? env.GRATIS_PT : env.GRATIS_OUTROS) || 0;
    const valor = limite && total >= limite ? 0 : custo;
    const nome = { pt: "Envio para Portugal", eu: "Envio para a Europa", int: "Envio internacional" }[zona];
    p.append("shipping_options[0][shipping_rate_data][type]", "fixed_amount");
    p.append("shipping_options[0][shipping_rate_data][display_name]", valor ? nome : nome + " (grátis)");
    p.append("shipping_options[0][shipping_rate_data][fixed_amount][amount]", String(valor));
    p.append("shipping_options[0][shipping_rate_data][fixed_amount][currency]", "eur");

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
