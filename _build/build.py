#!/usr/bin/env python3
"""Gera o site estático de laueditora.pt a partir de data.py.  Uso: python3 _build/build.py
Estrutura e aspeto replicam os sites do Hopp; fontes da app 42 (Bodoni Moda, Cormorant Garamond, Niagara) + Arbotek."""
import os, re, html
from data import AUTORES, LIVROS, REVIEWS, VIDEOS, PUBLICACOES, PRATICA_PT, PRATICA_EN

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://laueditora.pt"
EMAIL = "geral@laueditora.pt"
TEL = "+351967257681"
WA = "https://api.whatsapp.com/send?phone=351967257681"
PATREON = "https://www.patreon.com/laueditora"
IG = "https://www.instagram.com/laugoddog/"
LI = "https://www.linkedin.com/in/rafaelaugustocn"
YT = "https://youtube.com/@laugoddog"
SP = "https://open.spotify.com/artist/01Ae3zliOOHD3d9futectI"
WEB = "https://www.rafaelaugusto.com/"
esc = html.escape

S = 'fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"'
ICON = {
 "instagram": f'<svg viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="5" {S}/><circle cx="12" cy="12" r="4.2" {S}/><circle cx="17.4" cy="6.6" r="1.1" fill="currentColor"/></svg>',
 "email": '<svg viewBox="0 0 24 24"><path fill="currentColor" d="M3 5h18a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H3a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1zm9 7.2L4.4 7H19.6zM4 8.6V17h16V8.6l-8 5.5z"/></svg>',
 "whatsapp": f'<svg viewBox="0 0 24 24"><path d="M12 3a9 9 0 0 0-7.8 13.5L3 21l4.6-1.2A9 9 0 1 0 12 3z" {S}/><path d="M8.6 8.2c.2-.5.5-.5.8-.5h.5c.2 0 .4 0 .6.5l.8 1.9c.1.2 0 .4-.1.6l-.6.7c-.1.1-.2.3 0 .5.6 1 1.5 1.9 2.6 2.5.2.1.4.1.5 0l.7-.8c.2-.2.4-.2.6-.1l1.8.9c.2.1.4.2.4.4 0 .5-.2 1.3-.9 1.7-.6.4-1.5.6-3.3-.1-2.2-.9-3.9-3-4.4-3.8-.5-.8-.9-2-.3-3.2z" fill="currentColor"/></svg>',
 "linkedin": '<svg viewBox="0 0 24 24"><path fill="currentColor" d="M4 3.5a2 2 0 1 1 0 4 2 2 0 0 1 0-4zM2.3 9h3.4v12H2.3zM9 9h3.3v1.7c.5-.9 1.7-2 3.6-2 3.7 0 4.4 2.4 4.4 5.6V21h-3.4v-5.9c0-1.4 0-3.2-2-3.2s-2.3 1.5-2.3 3.1v6H9z"/></svg>',
 "youtube": '<svg viewBox="0 0 24 24"><path fill="currentColor" d="M21.6 7.2a2.6 2.6 0 0 0-1.8-1.8C18.2 5 12 5 12 5s-6.2 0-7.8.4A2.6 2.6 0 0 0 2.4 7.2 27 27 0 0 0 2 12a27 27 0 0 0 .4 4.8 2.6 2.6 0 0 0 1.8 1.8C5.8 19 12 19 12 19s6.2 0 7.8-.4a2.6 2.6 0 0 0 1.8-1.8A27 27 0 0 0 22 12a27 27 0 0 0-.4-4.8zM10 15V9l5.2 3z"/></svg>',
 "spotify": '<svg viewBox="0 0 24 24"><path fill="currentColor" d="M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20zm4.6 14.4a.6.6 0 0 1-.9.2c-2.4-1.5-5.4-1.8-9-1a.6.6 0 1 1-.3-1.2c3.9-.9 7.2-.5 10 1.1.3.2.4.6.2.9zm1.2-2.7a.8.8 0 0 1-1.1.3c-2.7-1.7-6.9-2.2-10.1-1.2a.8.8 0 1 1-.5-1.5c3.7-1.1 8.3-.6 11.4 1.3.4.2.5.7.3 1.1zm.1-2.8C14.7 9 9.4 8.8 6.4 9.7a1 1 0 1 1-.6-1.9c3.5-1 9.3-.8 13 1.4a1 1 0 0 1-.9 1.7z"/></svg>',
 "web": f'<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9" {S}/><path d="M3 12h18M12 3c2.5 2.7 3.8 5.7 3.8 9s-1.3 6.3-3.8 9c-2.5-2.7-3.8-5.7-3.8-9S9.5 5.7 12 3z" {S}/></svg>',
 "phone": f'<svg viewBox="0 0 24 24"><path d="M12 3a9 9 0 0 0-7.8 13.5L3 21l4.6-1.2A9 9 0 1 0 12 3z" {S}/></svg>',
 "mail-line": f'<svg viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="14" rx="1.5" {S}/><path d="M3.5 6l8.5 7 8.5-7" {S}/></svg>',
}
TICK = '<svg class="tick" viewBox="0 0 24 24"><path fill="#3897f0" d="M12 1.5l2.6 1.9 3.2-.2 1 3 2.7 1.8-1 3 1 3-2.7 1.8-1 3-3.2-.2L12 22.5l-2.6-1.9-3.2.2-1-3-2.7-1.8 1-3-1-3 2.7-1.8 1-3 3.2.2z"/><path d="M8 12.3l2.6 2.6L16.2 9" fill="none" stroke="#fff" stroke-width="2"/></svg>'

def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w", encoding="utf-8").write(content)

def head(title, desc, url, img, lang="pt", cls="lau"):
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
<meta name="theme-color" content="#1d1d1d">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:opsz,wght@6..96,400..700&family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Oswald:wght@500&display=swap">
<link rel="stylesheet" href="https://use.typekit.net/kww1ryt.css">
<link rel="stylesheet" href="/assets/style.css">
<link rel="icon" href="/img/favicon.png">
<link rel="apple-touch-icon" href="/img/apple-touch-icon.png">
</head>
<body class="{cls}">
"""

def menu():
    return f"""<button class="burger" aria-label="Abrir menu" data-menu-open><span></span><span></span><span></span></button>
<div class="scrim" data-menu-close></div>
<aside class="drawer" aria-label="Menu">
  <button class="close" aria-label="Fechar menu" data-menu-close>&times;</button>
  <img src="/img/logo-lau-branco.png" alt="LAU Edições">
  <nav>
    <a href="/">LAU Edições</a>
    <a href="/#livros">compra os nossos livros</a>
    <a href="/#autores">os nossos autores</a>
    {''.join(f'<a class="sub" href="/autores/{k}/">{esc(a["nome"])}</a>' for k, a in AUTORES.items())}
    <a href="/#pre-lancamentos">pré-lançamentos</a>
    <a href="/#patrono">torna-te patrono e editor</a>
    <a href="/#reviews">deixa uma review</a>
    <a href="/#sobre">sobre nós</a>
    <a href="/rafaelaugusto/">Rafael Augusto</a>
  </nav>
</aside>
"""

def socials(items):
    return '<div class="socials">' + "".join(f'<a href="{u}" aria-label="{n}" title="{n}" target="_blank" rel="noopener">{ICON[k]}</a>' for k, n, u in items) + '</div>'

def contacts(site_label, site_url):
    return f"""<ul class="contacts">
  <li>{ICON['mail-line']}<div><b>Email</b><a href="mailto:{EMAIL}">{EMAIL}</a></div></li>
  <li>{ICON['phone']}<div><b>Phone</b><a href="{WA}">{TEL}</a></div></li>
  <li>{ICON['web']}<div><b>Website</b><a href="{site_url}">{site_label}</a></div></li>
</ul>"""

FOOT = '<script src="/assets/site.js"></script>\n</body></html>\n'

def sec(target, title, sub=None, icon=None, caps=False):
    ic = f'<img class="ic" src="/img/{icon}" alt="">' if icon else ""
    st = f'<span class="st">{sub}</span>' if sub else ""
    return f'<button class="sec{" caps" if caps else ""}" data-open="{target}">{ic}<span class="tt">{title}</span>{st}</button>'

def modal(mid, title, sub, inner, carousel=True):
    sub_html = f"<span>{sub}</span>" if sub else ""
    arrows = '<button class="arrow l" aria-label="anterior">‹</button><button class="arrow r" aria-label="seguinte">›</button><div class="nav"></div>' if carousel else ""
    body = f'<div class="items">{inner}</div>{arrows}' if carousel else inner
    return f"""<div class="modal" id="{mid}" role="dialog" aria-modal="true" aria-label="{esc(title)}">
  <div class="sheet"><div class="mh"><b>{title}</b>{sub_html}</div>{body}</div>
  <button class="xclose" data-close aria-label="Fechar">&times;</button>
</div>"""

def preco(l):
    if l.get("esgotado"):
        return '<div class="out">esgotado</div>'
    s = f'<s>{l["preco_antigo"]}</s>' if l.get("preco_antigo") else ""
    return f'<div class="price">{s}{l["preco"]}</div>'

def texto(l):
    lang = f' lang="{l["lang"]}"' if l.get("lang") else ""
    return "".join(f"<p{lang}>{p}</p>" for p in l["texto"])

def book_item(l):
    buy = "" if l.get("esgotado") else f'<a class="btn" href="{l["compra"]}" target="_blank" rel="noopener">{l.get("botao","comprar")}</a>'
    return f"""<article class="item">
  <img class="cover" src="/img/{l['capa']}" alt="Capa de {esc(l['titulo'])}" loading="lazy">
  <h3>{esc(l['titulo'])}</h3>
  <div class="who">{esc(AUTORES[l['autor']]['nome'])}</div>
  {preco(l)}
  {buy}
  <div class="txt">{texto(l)}</div>
</article>"""

# ---------- página da editora ----------
def page_lau():
    lau = [l for l in LIVROS if l.get("lau")]
    dest = LIVROS[0]
    rv = "".join(f'<article class="item"><img class="cover" src="/img/{next(l["capa"] for l in LIVROS if l["titulo"].startswith(t.split(":")[0]))}" alt="" loading="lazy"><h3>{esc(t)}</h3><a class="btn" href="{g}" target="_blank" rel="noopener">goodreads</a><a class="btn alt" href="{a}" target="_blank" rel="noopener">amazon</a></article>' for t, g, a in REVIEWS)
    wip = f"""<article class="item"><img class="cover" src="/img/wip-luz-do-luto.webp" alt="" loading="lazy"><h3>Mourning Light: Luz do Luto</h3><div class="price">30€</div>
<a class="btn" href="https://buy.stripe.com/8x27sL2278BF25o3ck4gg07" target="_blank" rel="noopener">pré-reservar</a><a class="btn alt" href="{PATREON}" target="_blank" rel="noopener">aceder (patronos LAUWiP)</a>
<div class="txt"><p>O projeto Luz do Luto inclui um livro e um álbum musical. A edição — edição especial do livro, vinil e livro de letras — terá um numero limitado de cópias, que podem ser reservadas através do link.</p><p>Também é possível aceder aos conteúdos antecipadamente através do LAUWiP.</p></div></article>
<article class="item"><img class="cover" src="/img/wip-ao-deus-da-brincadeira.webp" alt="" loading="lazy"><h3>Ao Deus da Brincadeira (livro, ficção)</h3>
<a class="btn alt" href="{PATREON}" target="_blank" rel="noopener">aceder (patronos LAUWiP)</a></article>"""
    pre_intro = '<p style="font-size:17px">Aqui estão os trabalhos em desenvolvimento, alguns quase prontos a lançar, outros em processo de escrita. Podes pré-reservar aqueles que têm um lançamento planeado e, quanto aos outros, tornando-te patrono, podes aceder antecipadamente aos conteúdos e comentá-los, participando no processo editorial.</p>'
    patrono = f"""<div class="item" style="flex:none"><div class="price">15€/mês</div><div class="txt"><p>Enquanto patrono LAU Edições, terás uma participação ativa no processo editorial: com acesso a trabalhos em desenvolvimento, poderás comentar os textos e o teu nome será mencionado nos livros em cuja edição tenhas participado. Para além disso, terás acesso a exemplares autografados de todas as edições normais futuras e a 20% de desconto nos restantes produtos e serviços, entre outros.</p></div><a class="btn" href="{PATREON}" target="_blank" rel="noopener">ir para o Patreon</a></div>"""
    autores_rail = "".join(f'<button class="person" data-open="m-autor-{k}"><img src="/img/{a["foto"]}" alt="{esc(a["nome"])}" loading="lazy"><span>{esc(a["nome"])}</span></button>' for k, a in AUTORES.items())
    autores_modais = ""
    for k, a in AUTORES.items():
        livros = [l for l in LIVROS if l["autor"] == k and not l.get("esgotado")]
        covers = "".join(f'<a href="/livros/{l["slug"]}/"><img src="/img/{l["capa"]}" alt="{esc(l["titulo"])}" style="width:90px;aspect-ratio:2/3;object-fit:cover"></a>' for l in livros)
        extra = f'<a class="btn alt" href="{a["pagina"]}">ver página</a>' if a.get("pagina") else ""
        autores_modais += modal(f"m-autor-{k}", esc(a["nome"]), None,
            f'<div class="item bio" style="flex:none"><img class="thumb" src="/img/{a["foto"]}" alt="" style="aspect-ratio:4/5;filter:grayscale(1)">'
            + "".join(f"<p>{p}</p>" for p in a["bio"])
            + f'<p style="margin-top:14px"><b>{"autora" if k.startswith("maria") else "autor"} de:</b></p><div style="display:flex;gap:10px;flex-wrap:wrap">{covers}</div>'
            + f'<a class="btn" href="/autores/{k}/">livros de {esc(a["nome"])}</a><a class="btn alt" href="{a["amazon"]}" target="_blank" rel="noopener">Amazon</a>{extra}</div>', carousel=False)

    body = f"""{menu()}
<header class="hero">
  <video autoplay muted loop playsinline poster="/img/poster-hero-lau.jpg"><source src="/media/hero-lau.mp4" type="video/mp4"></video>
  <img class="logo" src="/img/logo-lau-branco.png" alt="LAU Edições">
  <p class="tagline">os nossos livros são resumos dos nossos silêncios.</p>
  {socials([("instagram","Instagram",IG),("email","Email","mailto:"+EMAIL),("whatsapp","WhatsApp",WA),("linkedin","LinkedIn",LI)])}
  <a class="down" href="#conteudo" aria-label="descer">↓</a>
</header>
<main class="wrap" id="conteudo">
  <button class="feature" data-open="m-livros" data-index="0">
    <video autoplay muted loop playsinline poster="/img/poster-destaque.jpg"><source src="/media/destaque.mp4" type="video/mp4"></video>
    <span class="t"><span class="big">em destaque</span><span class="it">O Meu Corpo de Barro e Ferro</span><span class="sm">poesia inédita de Leonel Coelho</span></span>
  </button>
  <div id="livros"></div>{sec("m-livros","compra os nossos livros",icon="icone-l.png")}
  <div id="reviews"></div>{sec("m-reviews","deixa uma review",icon="icone-a.png")}
  <div id="pre-lancamentos"></div>{sec("m-pre-lancamentos","pré-lançamentos",icon="icone-u.png")}
  <div id="patrono"></div>{sec("m-patrono","torna-te patrono e editor",icon="icone-aparo.png")}

  <section class="block" id="autores">
    <h2>os nossos autores</h2><div class="h2s">clica na imagem para saber mais</div>
    <div class="rail">{autores_rail}</div>
  </section>

  <section class="block" id="sobre">
    <h3>sobre nós</h3>
    <div id="sobre-txt" class="clamp" style="font-size:18px"><p>A LAU edições é uma editora independente focada em títulos que, através da ficção, do ensaio, da poesia ou do humor, exploram a mente e a natureza humanas. Achando que, na arte, a forma é tão importante como o conteúdo, damos a cada texto a casa que merece, aliando à qualidade dos textos a identidade visual que nos distingue.</p><p>Se gostavas de participar ativamente no processo editorial, receber em casa livros surpresa, ter acesso a conteúdos de livros em desenvolvimento (sobre os quais poderás dar a tua opinião), e ver teu nome nos agradecimentos de edições futuras em que participes, considera tornar-te patrono (topo da página).</p></div>
    <button class="more" data-more="sobre-txt">Mostrar mais ⌄</button>
    <div style="margin-top:18px">
      <details class="line"><summary>produtos e serviços</summary><div class="in"><p>Para além de publicarmos livros, fornecemos vários serviços, editoriais e não só, que poderás explorar abaixo. Se gostarias de trabalhar connosco, não hesites em contactar.</p></div></details>
      <details class="line" id="publica"><summary>publica connosco</summary><div class="in"><p>Se escreveste ou estás a escrever um livro e gostarias de o publicar, envia uma proposta de edição para <a href="mailto:{EMAIL}">{EMAIL}</a>. Depois da análise, decidiremos se se alinha com o nosso projeto editorial.</p><a class="wide" href="mailto:{EMAIL}">fala connosco</a></div></details>
    </div>
  </section>
  {contacts("laueditora.pt/", "/")}
</main>
{modal("m-livros","compra os nossos livros",None,"".join(book_item(l) for l in lau))}
{modal("m-reviews","deixa uma review",None,rv)}
{modal("m-pre-lancamentos","pré-lançamentos",None,pre_intro + '<div class="items">' + wip + '</div><button class="arrow l">‹</button><button class="arrow r">›</button><div class="nav"></div>', carousel=False)}
{modal("m-patrono","torna-te patrono e editor",None,patrono,carousel=False)}
{autores_modais}
"""
    write("index.html", head("LAU EDIÇÕES, a nova editora portuguesa independente",
        "Edição de livros — uma estética que se alinha com a qualidade dos conteúdos. Livros, subscrições, serviços, workshops e cursos.",
        "/", "og-lau.jpg", "pt", "lau") + body + FOOT)

# ---------- página pessoal ----------
def page_rafael():
    livros = [l for l in LIVROS if l.get("pessoal")]
    vids = "".join(f'<article class="item"><a href="{u}" target="_blank" rel="noopener"><img class="thumb" src="/img/{img}" alt="" loading="lazy"></a><h3>{esc(t)}</h3><a class="btn" href="{u}" target="_blank" rel="noopener">Watch now</a></article>' for t, u, img in VIDEOS)
    pubs = "".join(f'<article class="item" lang="en"><a href="{u}" target="_blank" rel="noopener"><img class="thumb" src="/img/{img}" alt="" loading="lazy"></a><h3>{esc(t)}</h3><div class="who">{esc(au)}</div><div class="txt"><p>{esc(ab)}</p></div><a class="btn" href="{u}" target="_blank" rel="noopener">Continue</a></article>' for t, au, u, img, ab in PUBLICACOES)
    wip = f"""<article class="item"><img class="cover" src="/img/wip-luz-do-luto.webp" alt="" loading="lazy"><h3>Luz do Luto</h3><div class="txt"><p>Álbum + livro.</p></div>
<a class="btn" href="https://buy.stripe.com/8x27sL2278BF25o3ck4gg07" target="_blank" rel="noopener">pré-reserva</a><a class="btn alt" href="{PATREON}" target="_blank" rel="noopener">Continue</a></article>
<article class="item"><img class="cover" src="/img/wip-ao-deus-da-brincadeira.webp" alt="" loading="lazy"><h3>Ao Deus da Brincadeira</h3><div class="txt"><p>Ficção narrativa.</p></div><a class="btn alt" href="{PATREON}" target="_blank" rel="noopener">Continue</a></article>"""
    ta = LIVROS[1]
    body = f"""{menu()}
<header class="hero clear" style="min-height:92svh">
  <img class="sig" src="/img/assinatura-branca.png" alt="">
  <h1>Rafael Augusto{TICK}</h1>
  <div class="sub">Unravelling The Mind | Philosophy, Books &amp; Music</div>
  {socials([("instagram","Instagram",IG),("youtube","YouTube",YT),("spotify","Spotify",SP),("web","Website",WEB),("email","Email","mailto:"+EMAIL),("linkedin","LinkedIn",LI),("whatsapp","WhatsApp",WA)])}
</header>
<main class="wrap">
  <button class="feature" data-open="m-books" data-index="0">
    <video autoplay muted loop playsinline poster="/img/poster-now-available.jpg"><source src="/media/now-available.mp4" type="video/mp4"></video>
    <span class="t"><span class="big">now available</span><span class="it">em destaque</span></span>
  </button>
  {sec("m-books","Books","livros",caps=True)}
  {sec("m-music","Music Videos","videoclips",caps=True)}
  {sec("m-academic","Academic Publications","publicações académicas",caps=True)}

  <section class="block" id="practice" lang="en">
    <h2>Philosophical Practice</h2><div class="h2s">Acompanhamento Filosófico</div>
    <h3>Philosophical Practice: An Alternative to therapy, coaches and religions</h3>
    <p style="font-size:18px">Besides my PhD in Philosophy and my MsC in Cognitive Science, I was trained by Lydia Amir as a philosophical practitioner. I work with individuals and couples, in Portuguese and English. The first session is for free.<br>If you want to know more, read below or click the button to send me a message.</p>
    <details class="line" lang="pt"><summary>PT</summary><div class="in">{PRATICA_PT}</div></details>
    <details class="line"><summary>EN</summary><div class="in">{PRATICA_EN}</div></details>
    <a class="wide" href="{WA}&amp;text=">book a free session | enquire</a>
  </section>

  <section class="block" id="wip">
    <h2>Works in Progress</h2><div class="h2s">LAUWiP</div>
    {sec("m-wip","Works in Progress","trabalhos em desenvolvimento",caps=True)}
    <a class="wide" href="{PATREON}" target="_blank" rel="noopener">access LAUWiP (patreon)</a>
  </section>
  {contacts("rafaelaugusto.com", WEB)}
</main>
{modal("m-books","Books","livros","".join(book_item(l) for l in livros))}
{modal("m-music","Music Videos","videoclips",vids)}
{modal("m-academic","Academic Publications","publicações académicas",pubs)}
{modal("m-wip","Works in Progress","trabalhos em desenvolvimento",wip)}
"""
    write("rafaelaugusto/index.html", head("Rafael Augusto | Philosophy, Books & Music",
        "Here you can find my books, my articles, my music, podcasts and other contents.",
        "/rafaelaugusto/", "og-rafael.jpg", "en", "rafael") + body + FOOT)

# ---------- subpáginas (livro e autor) ----------
def page_livro(l):
    a = AUTORES[l["autor"]]
    buy = "" if l.get("esgotado") else f'<a class="wide" href="{l["compra"]}" target="_blank" rel="noopener">{l.get("botao","comprar")}</a>'
    body = f"""{menu()}
<main class="wrap page">
  <img class="cover" src="/img/{l['capa']}" alt="Capa de {esc(l['titulo'])}">
  <h1>{esc(l['titulo'])}</h1>
  <div class="who"><a href="/autores/{l['autor']}/">{esc(a['nome'])}</a></div>
  {preco(l)}
  {buy}
  <div style="font-size:18px">{texto(l)}</div>
  {contacts("laueditora.pt/", "/")}
</main>
"""
    desc = re.sub("<[^>]+>", "", l["texto"][1] if l["texto"][0].startswith("<b>") else l["texto"][0])[:155]
    write(f"livros/{l['slug']}/index.html", head(f"{l['titulo']} — {a['nome']} | LAU Edições", desc, f"/livros/{l['slug']}/", l["capa"]) + body + FOOT)

def page_autor(k, a):
    livros = [l for l in LIVROS if l["autor"] == k]
    grid = "".join(f'<a href="/livros/{l["slug"]}/" style="text-decoration:none"><img src="/img/{l["capa"]}" alt="" style="aspect-ratio:2/3;object-fit:cover;width:100%"><div style="font-family:var(--fd);font-size:16px;margin-top:6px">{esc(l["titulo"])}</div></a>' for l in livros)
    body = f"""{menu()}
<main class="wrap page">
  <img class="cover" src="/img/{a['foto']}" alt="{esc(a['nome'])}" style="filter:grayscale(1)">
  <h1>{esc(a['nome'])}</h1>
  <div style="font-size:18px;margin-top:14px">{''.join(f'<p>{p}</p>' for p in a['bio'])}</div>
  <section class="block"><h2>livros</h2><div style="display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-top:16px">{grid}</div></section>
  <a class="wide" href="{a['amazon']}" target="_blank" rel="noopener">Amazon</a>
  {contacts("laueditora.pt/", "/")}
</main>
"""
    desc = re.sub("<[^>]+>", "", a["bio"][0])[:155]
    write(f"autores/{k}/index.html", head(f"{a['nome']} | LAU Edições", desc, f"/autores/{k}/", a["foto"]) + body + FOOT)

def extras():
    urls = ["/", "/rafaelaugusto/"] + [f"/autores/{k}/" for k in AUTORES] + [f"/livros/{l['slug']}/" for l in LIVROS]
    write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
          + "".join(f"  <url><loc>{SITE}{u}</loc></url>\n" for u in urls) + "</urlset>\n")
    write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
    write("CNAME", "laueditora.pt\n")
    write("404.html", head("Página não encontrada | LAU Edições", "Página não encontrada.", "/404.html", "og-lau.jpg")
          + menu() + '<main class="wrap page"><h1>Página não encontrada</h1><p style="text-align:center"><a href="/">voltar à LAU Edições</a></p></main>' + FOOT)
    write(".nojekyll", "")

if __name__ == "__main__":
    page_lau(); page_rafael()
    for l in LIVROS: page_livro(l)
    for k, a in AUTORES.items(): page_autor(k, a)
    extras()
    print("ok")
