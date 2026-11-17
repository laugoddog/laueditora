#!/usr/bin/env python3
"""Gera o site estático de laueditora.pt a partir de data.py.  Uso: python3 _build/build.py"""
import os, html
from data import AUTORES, LIVROS, REVIEWS, VIDEOS, PUBLICACOES, PRATICA_PT, PRATICA_EN

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://laueditora.pt"
EMAIL_LAU = "geral@laueditora.pt"
EMAIL_RA = "geral@laueditora.pt"
TEL = "+351967257681"
WA = "https://api.whatsapp.com/send?phone=351967257681"
PATREON = "https://www.patreon.com/laueditora"
esc = html.escape

ICON = {
 "instagram": '<svg viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="5" fill="none" stroke="currentColor" stroke-width="1.8"/><circle cx="12" cy="12" r="4.2" fill="none" stroke="currentColor" stroke-width="1.8"/><circle cx="17.4" cy="6.6" r="1.2" fill="currentColor"/></svg>',
 "email": '<svg viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="14" rx="1.5" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M3.5 6l8.5 7 8.5-7" fill="none" stroke="currentColor" stroke-width="1.8"/></svg>',
 "whatsapp": '<svg viewBox="0 0 24 24"><path d="M12 3a9 9 0 0 0-7.8 13.5L3 21l4.6-1.2A9 9 0 1 0 12 3z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/><path d="M8.6 8.2c.2-.5.5-.5.8-.5h.5c.2 0 .4 0 .6.5l.8 1.9c.1.2 0 .4-.1.6l-.6.7c-.1.1-.2.3 0 .5.6 1 1.5 1.9 2.6 2.5.2.1.4.1.5 0l.7-.8c.2-.2.4-.2.6-.1l1.8.9c.2.1.4.2.4.4 0 .5-.2 1.3-.9 1.7-.6.4-1.5.6-3.3-.1-2.2-.9-3.9-3-4.4-3.8-.5-.8-.9-2-.3-3.2z" fill="currentColor"/></svg>',
 "linkedin": '<svg viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="2" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M7.5 10v6.5M7.5 7.2v.1M11 16.5V10m0 3c0-1.8 1-3 2.6-3S16.5 11 16.5 13v3.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>',
 "youtube": '<svg viewBox="0 0 24 24"><rect x="2.5" y="5.5" width="19" height="13" rx="3.5" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M10 9.2v5.6l4.8-2.8z" fill="currentColor"/></svg>',
 "spotify": '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M7.5 9.6c3-.9 6.4-.6 9 .9M8 12.6c2.4-.7 5-.5 7.2.8M8.6 15.4c1.9-.5 3.8-.3 5.5.6" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>',
}
def social(items):
    return '<div class="socials">' + "".join(f'<a href="{u}" aria-label="{n}" title="{n}" target="_blank" rel="noopener">{ICON[k]}</a>' for k, n, u in items) + '</div>'

def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)

def head(title, desc, url, img, lang="pt"):
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{SITE}{url}">
<meta property="og:type" content="website">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{SITE}{url}">
<meta property="og:image" content="{SITE}/img/{img}">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:opsz,wght@6..96,400..600&family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Oswald:wght@500&display=swap">
<link rel="stylesheet" href="https://use.typekit.net/kww1ryt.css">
<link rel="stylesheet" href="/assets/style.css">
<link rel="icon" href="/img/favicon.png">
<link rel="apple-touch-icon" href="/img/apple-touch-icon.png">
</head>
<body>
"""

MENU = f"""<header class="topbar">
  <button class="burger" aria-label="Abrir menu" data-menu-open><span></span><span></span><span></span></button>
  <a class="logo" href="/"><b>LAU</b> <span>EDIÇÕES</span></a>
  <span class="spacer"></span>
</header>
<div class="scrim" data-menu-close></div>
<aside class="drawer" aria-label="Menu">
  <button class="close" aria-label="Fechar menu" data-menu-close>&times;</button>
  <nav>
    <a href="/#livros">Livros</a>
    <a href="/#autores">Autores</a>
    {''.join(f'<a class="sub" href="/autores/{k}/">{esc(a["nome"])}</a>' for k, a in AUTORES.items())}
    <a href="/#pre-lancamentos">Pré-lançamentos</a>
    <a href="/#patronos">Patronos</a>
    <a href="/#reviews">Deixa uma review</a>
    <a href="/#sobre">Sobre nós</a>
    <a href="/#publica">Publica connosco</a>
    <a href="/rafaelaugusto/">Rafael Augusto</a>
    <a href="#contactos">Contactos</a>
  </nav>
</aside>
"""

def footer(email, site_label="laueditora.pt", site_url="/"):
    return f"""<footer id="contactos">
  <a class="logo" href="/"><b>LAU</b> <span>EDIÇÕES</span></a>
  {social([("instagram","Instagram","https://www.instagram.com/laugoddog/"),("email","Email","mailto:"+email),("whatsapp","WhatsApp",WA),("linkedin","LinkedIn","https://www.linkedin.com/in/rafaelaugustocn")])}
  <div class="contacts">
    <a href="mailto:{email}">{email}</a><br>
    <a href="{WA}">{TEL}</a><br>
    <a href="{site_url}">{site_label}</a>
  </div>
</footer>
<script src="/assets/site.js"></script>
</body></html>
"""

def autor_link(slug):
    return f'<a href="/autores/{slug}/">{esc(AUTORES[slug]["nome"])}</a>'

def preco(l):
    if l.get("esgotado"):
        return '<div class="price"><span class="out">esgotado</span></div>'
    s = f'<s>{l["preco_antigo"]}</s>' if l.get("preco_antigo") else ""
    return f'<div class="price">{s}{l["preco"]}</div>'

def botao(l, cls="btn"):
    if l.get("esgotado"):
        return ""
    return f'<a class="{cls}" href="{l["compra"]}" target="_blank" rel="noopener">{l.get("botao","comprar")}</a>'

def texto(l):
    lang = f' lang="{l["lang"]}"' if l.get("lang") else ""
    return "".join(f"<p{lang}>{p}</p>" for p in l["texto"])

def book_card(l, show_author=True):
    a = f'<div class="autor">{autor_link(l["autor"])}</div>' if show_author else ""
    return f"""<article class="book">
  <a href="/livros/{l['slug']}/"><img class="cover" src="/img/{l['capa']}" alt="Capa de {esc(l['titulo'])}" loading="lazy"></a>
  <h3><a href="/livros/{l['slug']}/">{esc(l['titulo'])}</a></h3>
  {a}
  {preco(l)}
  <details><summary>ler</summary><div class="txt">{texto(l)}</div></details>
  <div class="btns">{botao(l)}</div>
</article>"""

# ---------- página da editora ----------
def page_lau():
    lau = [l for l in LIVROS if l.get("lau")]
    dest = LIVROS[0]
    reviews = "".join(f'<li><span>{esc(t)}</span><span class="links"><a href="{g}" target="_blank" rel="noopener">goodreads</a><a href="{a}" target="_blank" rel="noopener">amazon</a></span></li>' for t, g, a in REVIEWS)
    autores = "".join(f'<a class="author-card" href="/autores/{k}/"><img src="/img/{a["foto"]}" alt="{esc(a["nome"])}" loading="lazy"><h3>{esc(a["nome"])}</h3></a>' for k, a in AUTORES.items())
    body = f"""{MENU}
<main>
<section class="hero">
  <h1><b>LAU</b> <span>EDIÇÕES</span></h1>
  <p class="lema">os nossos livros são resumos dos nossos silêncios.</p>
  {social([("instagram","Instagram","https://www.instagram.com/laugoddog/"),("email","Email","mailto:"+EMAIL_LAU),("whatsapp","WhatsApp",WA),("linkedin","LinkedIn","https://www.linkedin.com/in/rafaelaugustocn")])}
</section>

<section id="destaque">
  <div class="feature">
    <a href="/livros/{dest['slug']}/"><img src="/img/{dest['capa']}" alt="Capa de {esc(dest['titulo'])}"></a>
    <div>
      <div class="tag">em destaque</div>
      <h2>{esc(dest['titulo'])}</h2>
      <p class="dim">{dest['destaque']}</p>
      {preco(dest)}
      <div class="btns">{botao(dest)}<a class="btn ghost" href="/livros/{dest['slug']}/">sinopse</a></div>
    </div>
  </div>
</section>

<section id="livros">
  <h2 class="kicker">compra os nossos livros</h2>
  <div class="grid">{''.join(book_card(l) for l in lau)}</div>
</section>

<section id="pre-lancamentos">
  <h2 class="kicker">pré-lançamentos</h2>
  <p class="prose">Aqui estão os trabalhos em desenvolvimento, alguns quase prontos a lançar, outros em processo de escrita. Podes pré-reservar aqueles que têm um lançamento planeado e, quanto aos outros, tornando-te patrono, podes aceder antecipadamente aos conteúdos e comentá-los, participando no processo editorial.</p>
  <div class="cards">
    <article class="card">
      <img src="/img/wip-luz-do-luto.webp" alt="Mourning Light: Luz do Luto" loading="lazy">
      <h3>Mourning Light: Luz do Luto</h3>
      <p>O projeto Luz do Luto inclui um livro e um álbum musical. A edição — edição especial do livro, vinil e livro de letras — terá um numero limitado de cópias, que podem ser reservadas através do link.</p>
      <p>Também é possível aceder aos conteúdos antecipadamente através do LAUWiP.</p>
      <div class="price">30€</div>
      <div class="btns"><a class="btn" href="https://buy.stripe.com/8x27sL2278BF25o3ck4gg07" target="_blank" rel="noopener">pré-reservar</a><a class="btn ghost" href="{PATREON}" target="_blank" rel="noopener">aceder (patronos LAUWiP)</a></div>
    </article>
    <article class="card">
      <img src="/img/wip-ao-deus-da-brincadeira.webp" alt="Ao Deus da Brincadeira" loading="lazy">
      <h3>Ao Deus da Brincadeira</h3>
      <p class="dim">livro, ficção</p>
      <div class="btns"><a class="btn ghost" href="{PATREON}" target="_blank" rel="noopener">aceder (patronos LAUWiP)</a></div>
    </article>
  </div>
</section>

<section id="patronos">
  <h2 class="kicker">torna-te patrono e editor</h2>
  <div class="box prose">
    <div class="price">15€/mês</div>
    <p>Enquanto patrono LAU Edições, terás uma participação ativa no processo editorial: com acesso a trabalhos em desenvolvimento, poderás comentar os textos e o teu nome será mencionado nos livros em cuja edição tenhas participado. Para além disso, terás acesso a exemplares autografados de todas as edições normais futuras e a 20% de desconto nos restantes produtos e serviços, entre outros.</p>
    <a class="btn" href="{PATREON}" target="_blank" rel="noopener">ir para o Patreon</a>
  </div>
</section>

<section id="autores">
  <h2 class="kicker">os nossos autores</h2>
  <div class="authors">{autores}</div>
</section>

<section id="reviews">
  <h2 class="kicker">deixa uma review</h2>
  <ul class="list">{reviews}</ul>
</section>

<section id="sobre">
  <h2 class="kicker">sobre nós</h2>
  <div class="cols">
    <div class="prose">
      <p>A LAU edições é uma editora independente focada em títulos que, através da ficção, do ensaio, da poesia ou do humor, exploram a mente e a natureza humanas. Achando que, na arte, a forma é tão importante como o conteúdo, damos a cada texto a casa que merece, aliando à qualidade dos textos a identidade visual que nos distingue.</p>
      <p>Se gostavas de participar ativamente no processo editorial, receber em casa livros surpresa, ter acesso a conteúdos de livros em desenvolvimento (sobre os quais poderás dar a tua opinião), e ver teu nome nos agradecimentos de edições futuras em que participes, considera tornar-te <a href="#patronos">patrono</a>.</p>
    </div>
    <div>
      <h3>produtos e serviços</h3>
      <p>Para além de publicarmos livros, fornecemos vários serviços, editoriais e não só. Se gostarias de trabalhar connosco, não hesites em contactar.</p>
      <h3 id="publica">publica connosco</h3>
      <p>Se escreveste ou estás a escrever um livro e gostarias de o publicar, envia uma proposta de edição para <a href="mailto:{EMAIL_LAU}">{EMAIL_LAU}</a>. Depois da análise, decidiremos se se alinha com o nosso projeto editorial.</p>
      <a class="btn ghost" href="mailto:{EMAIL_LAU}">fala connosco</a>
    </div>
  </div>
</section>
</main>
"""
    write("index.html", head("LAU EDIÇÕES, a nova editora portuguesa independente",
        "Edição de livros — uma estética que se alinha com a qualidade dos conteúdos. Livros, subscrições, serviços, workshops e cursos.",
        "/", "og-lau.jpg") + body + footer(EMAIL_LAU))

# ---------- páginas de livro ----------
def page_livro(l):
    a = AUTORES[l["autor"]]
    lang = l.get("lang", "pt")
    body = f"""{MENU}
<main>
<section>
  <div class="feature">
    <img src="/img/{l['capa']}" alt="Capa de {esc(l['titulo'])}">
    <div>
      <div class="tag">{autor_link(l['autor'])}</div>
      <h1 style="font-family:var(--fd);font-size:clamp(28px,4.6vw,40px);line-height:1.15;margin:8px 0 10px">{esc(l['titulo'])}</h1>
      {preco(l)}
      <div class="btns">{botao(l)}</div>
    </div>
  </div>
</section>
<section class="prose">{texto(l)}</section>
<section>
  <h2 class="kicker">do mesmo autor</h2>
  <div class="grid">{''.join(book_card(x, False) for x in LIVROS if x['autor']==l['autor'] and x is not l)}</div>
</section>
</main>
"""
    desc = (l["texto"][0] if not l["texto"][0].startswith("<b>") else l["texto"][1])
    import re
    desc = re.sub("<[^>]+>", "", desc)[:155]
    write(f"livros/{l['slug']}/index.html", head(f"{l['titulo']} — {a['nome']} | LAU Edições", desc,
        f"/livros/{l['slug']}/", l["capa"], "pt") + body + footer(EMAIL_LAU))

# ---------- páginas de autor ----------
def page_autor(k, a):
    livros = [l for l in LIVROS if l["autor"] == k]
    extra = f'<a class="btn ghost" href="{a["pagina"]}">página pessoal</a>' if a.get("pagina") else ""
    body = f"""{MENU}
<main>
<section>
  <div class="author-page">
    <img src="/img/{a['foto']}" alt="{esc(a['nome'])}">
    <div class="prose">
      <h1 class="kicker">{esc(a['nome'])}</h1>
      {''.join(f'<p>{p}</p>' for p in a['bio'])}
      <div class="btns"><a class="btn ghost" href="{a['amazon']}" target="_blank" rel="noopener">Amazon</a>{extra}</div>
    </div>
  </div>
</section>
<section>
  <h2 class="kicker">livros</h2>
  <div class="grid">{''.join(book_card(l, False) for l in livros)}</div>
</section>
</main>
"""
    import re
    desc = re.sub("<[^>]+>", "", a["bio"][0])[:155]
    write(f"autores/{k}/index.html", head(f"{a['nome']} | LAU Edições", desc, f"/autores/{k}/", a["foto"]) + body + footer(EMAIL_LAU))

# ---------- página pessoal ----------
def page_rafael():
    livros = [l for l in LIVROS if l.get("pessoal")]
    videos = "".join(f'<article class="card video"><a href="{u}" target="_blank" rel="noopener"><img src="/img/{img}" alt="{esc(t)}" loading="lazy"><h3>{esc(t)}</h3><span class="play">watch now</span></a></article>' for t, u, img in VIDEOS)
    pubs = "".join(f'<article class="card"><a href="{u}" target="_blank" rel="noopener"><img src="/img/{img}" alt="" loading="lazy"></a><h3><a href="{u}" target="_blank" rel="noopener">{esc(t)}</a></h3><p class="dim small">{esc(au)}</p><p class="small">{esc(ab)}</p><a class="btn ghost" href="{u}" target="_blank" rel="noopener">read</a></article>' for t, au, u, img, ab in PUBLICACOES)
    ta = LIVROS[1]
    body = f"""{MENU}
<main>
<section class="hero">
  <h1 style="font-family:var(--fd);font-weight:400;font-size:clamp(40px,9vw,80px)">Rafael Augusto</h1>
  <p class="lema">Unravelling The Mind | Philosophy, Books &amp; Music</p>
  {social([("instagram","Instagram","https://www.instagram.com/laugoddog/"),("youtube","YouTube","https://youtube.com/@laugoddog"),("spotify","Spotify","https://open.spotify.com/artist/01Ae3zliOOHD3d9futectI"),("linkedin","LinkedIn","https://www.linkedin.com/in/rafaelaugustocn"),("email","Email","mailto:"+EMAIL_RA),("whatsapp","WhatsApp",WA)])}
</section>

<section>
  <div class="feature">
    <a href="/livros/{ta['slug']}/"><img src="/img/{ta['capa']}" alt="Thinking Animal"></a>
    <div lang="en">
      <div class="tag">Now Avaliable</div>
      <h2>{esc(ta['titulo'])}</h2>
      {preco(ta)}
      <div class="btns"><a class="btn" href="{ta['compra']}" target="_blank" rel="noopener">Buy Now</a></div>
    </div>
  </div>
</section>

<section id="books">
  <h2 class="kicker">books</h2>
  <div class="grid">{''.join(book_card(l, False) for l in livros)}</div>
</section>

<section id="music">
  <h2 class="kicker">music videos</h2>
  <div class="cards">{videos}</div>
</section>

<section id="academic" lang="en">
  <h2 class="kicker">academic publications</h2>
  <div class="cards">{pubs}</div>
</section>

<section id="practice" lang="en">
  <h2 class="kicker">philosophical practice</h2>
  <div class="prose">
    <h3>Philosophical Practice: An Alternative to therapy, coaches and religions</h3>
    <p style="margin-top:12px">Besides my PhD in Philosophy and my MsC in Cognitive Science, I was trained by Lydia Amir as a philosophical practitioner. I work with individuals and couples, in Portuguese and English. The first session is for free.</p>
    <p>If you want to know more, read below or click the button to send me a message.</p>
    <a class="btn" href="{WA}&amp;text=">book a free session | enquire</a>
    <details lang="pt"><summary>PT</summary><div class="txt">{PRATICA_PT}</div></details>
    <details><summary>EN</summary><div class="txt">{PRATICA_EN}</div></details>
  </div>
</section>

<section id="wip">
  <h2 class="kicker">works in progress</h2>
  <div class="cards">
    <article class="card"><img src="/img/wip-luz-do-luto.webp" alt="Luz do Luto" loading="lazy"><h3>Luz do Luto</h3><p>Álbum + livro.</p><div class="btns"><a class="btn" href="https://buy.stripe.com/8x27sL2278BF25o3ck4gg07" target="_blank" rel="noopener">pré-reserva</a><a class="btn ghost" href="{PATREON}" target="_blank" rel="noopener">continue</a></div></article>
    <article class="card"><img src="/img/wip-ao-deus-da-brincadeira.webp" alt="Ao Deus da Brincadeira" loading="lazy"><h3>Ao Deus da Brincadeira</h3><p>Ficção narrativa.</p><div class="btns"><a class="btn ghost" href="{PATREON}" target="_blank" rel="noopener">continue</a></div></article>
  </div>
  <div class="btns" style="margin-top:24px"><a class="btn" href="{PATREON}" target="_blank" rel="noopener">access LAUWiP (patreon)</a></div>
</section>
</main>
"""
    write("rafaelaugusto/index.html", head("Rafael Augusto | Philosophy, Books & Music",
        "Here you can find my books, my articles, my music, podcasts and other contents.",
        "/rafaelaugusto/", "og-rafael.jpg", "en") + body + footer(EMAIL_RA, "rafaelaugusto.com", "https://www.rafaelaugusto.com/"))

def extras():
    urls = ["/", "/rafaelaugusto/"] + [f"/autores/{k}/" for k in AUTORES] + [f"/livros/{l['slug']}/" for l in LIVROS]
    write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
          + "".join(f"  <url><loc>{SITE}{u}</loc></url>\n" for u in urls) + "</urlset>\n")
    write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
    write("CNAME", "laueditora.pt\n")
    write("404.html", head("Página não encontrada | LAU Edições", "Página não encontrada.", "/404.html", "og-lau.jpg")
          + MENU + '<main><section class="hero"><h1 style="font-family:var(--fd);font-size:48px">Página não encontrada</h1><p class="lema"><a href="/">voltar à LAU Edições</a></p></section></main>' + footer(EMAIL_LAU))
    write(".nojekyll", "")

if __name__ == "__main__":
    page_lau(); page_rafael()
    for l in LIVROS: page_livro(l)
    for k, a in AUTORES.items(): page_autor(k, a)
    extras()
    print("ok")
