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
TICK = '<svg class="tick" viewBox="0 0 24 24" aria-label="verificado"><path fill="#3897f0" stroke="#3897f0" stroke-width="1.6" stroke-linejoin="round" d="M12.00 0.80 L13.87 2.58 L16.29 1.65 L17.33 4.02 L19.92 4.08 L19.98 6.67 L22.35 7.71 L21.42 10.13 L23.20 12.00 L21.42 13.87 L22.35 16.29 L19.98 17.33 L19.92 19.92 L17.33 19.98 L16.29 22.35 L13.87 21.42 L12.00 23.20 L10.13 21.42 L7.71 22.35 L6.67 19.98 L4.08 19.92 L4.02 17.33 L1.65 16.29 L2.58 13.87 L0.80 12.00 L2.58 10.13 L1.65 7.71 L4.02 6.67 L4.08 4.08 L6.67 4.02 L7.71 1.65 L10.13 2.58Z"/><path d="M7.6 12.2l3 3 5.8-6" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>'

def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w", encoding="utf-8").write(content)

import hashlib
VER = hashlib.md5((open(os.path.join(ROOT,"assets/style.css"),"rb").read()+open(os.path.join(ROOT,"assets/site.js"),"rb").read())).hexdigest()[:8]

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
<link rel="stylesheet" href="/assets/style.css?v={VER}">
<link rel="icon" href="/img/favicon.png">
<link rel="apple-touch-icon" href="/img/apple-touch-icon.png">
</head>
<body class="{cls}">
"""

def menu():
    return f"""<button class="burger" aria-label="Abrir menu" data-menu-open><span></span><span></span><span></span></button>
<div class="scrim" data-menu-close></div>
<button class="cartbtn" aria-label="Abrir carrinho" data-cart-open>{CART_SVG}<span class="cnt" hidden>0</span></button>
<aside class="cart" aria-label="Carrinho">
  <div class="ch"><b>carrinho</b><button class="close" aria-label="Fechar carrinho" data-cart-close>&times;</button></div>
  <div class="clist"></div>
  <div class="cfoot"><div class="ctot"><span>total</span><b></b></div>
  <label class="czona">envio para <select><option value="pt">Portugal</option><option value="eu">Europa</option><option value="int">resto do mundo</option></select></label>
  <p class="cnote">Portes grátis acima de 30€ em Portugal e de 50€ no estrangeiro. O valor dos portes aparece no pagamento.</p>
  <a class="btn cgo" href="#">finalizar encomenda</a></div>
</aside>
<aside class="drawer" aria-label="Menu">
  <button class="close" aria-label="Fechar menu" data-menu-close>&times;</button>
  <a class="dlogo" href="/"><img src="/img/logo-lau-longo.png" alt="LAU Edições"></a>
  <nav>
    <a href="/">LAU Edições</a>
    <a href="/#livros">compra os nossos livros</a>
    <a href="/#autores">os nossos autores</a>
    {''.join(f'<a class="sub" href="/autores/{k}/">{esc(a["nome"])}</a>' for k, a in AUTORES.items())}
    <a href="/#patrono">torna-te patrono e editor</a>
    <a href="/#reviews">deixa uma review</a>
    <a href="/#sobre">sobre nós</a>
    <a href="/rafaelaugusto/">Rafael Augusto</a>
  </nav>
  <div class="dsoc">{socials([("instagram","Instagram",IG),("email","Email","mailto:"+EMAIL),("whatsapp","WhatsApp",WA),("linkedin","LinkedIn",LI)])}</div>
</aside>
<header class="topbar"><a href="/" aria-label="LAU Edições — página inicial"><img src="/img/logo-lau-longo.png" alt="LAU Edições"></a></header>
"""

def socials(items):
    return '<div class="socials">' + "".join(f'<a href="{u}" aria-label="{n}" title="{n}" target="_blank" rel="noopener">{ICON[k]}</a>' for k, n, u in items) + '</div>'

def contacts(site_label, site_url):
    return f"""<ul class="contacts">
  <li>{ICON['mail-line']}<div><b>Email</b><a href="mailto:{EMAIL}">{EMAIL}</a></div></li>
  <li>{ICON['phone']}<div><b>Phone</b><a href="{WA}">{TEL}</a></div></li>
  <li>{ICON['web']}<div><b>Website</b><a href="{site_url}">{site_label}</a></div></li>
</ul>"""

FOOT = f'<script src="/assets/site.js?v={VER}"></script>\n</body></html>\n'

def acc(aid, title, inner, sub=None, icon=None, caps=False, keep=False):
    ic = f'<img class="ic{" keep" if keep else ""}" src="/img/{icon}" alt="">' if icon else ""
    st = f'<span class="st">{sub}</span>' if sub else ""
    return f"""<section class="acc{" caps" if caps else ""}" id="{aid}">
  <button class="acc-h" aria-expanded="false">{ic}<span class="tt">{title}</span>{st}</button>
  <div class="acc-b"><div class="acc-in"><div class="panel">{inner}</div></div></div>
</section><button class="xbtn" aria-label="Fechar">&times;</button>"""

def preco(l, cls="pr"):
    if l.get("variantes"):
        return f'<div class="{cls}">' + " – ".join(v[1] for v in l["variantes"]) + "</div>"
    if l.get("esgotado"):
        return '<div class="out">esgotado</div>'
    s = f'<s>{l["preco_antigo"]}</s>' if l.get("preco_antigo") else ""
    return f'<div class="{cls}">{s}{l["preco"]}</div>'

def texto(l):
    lang = f' lang="{l["lang"]}"' if l.get("lang") else ""
    return "".join(f'<h4{lang}>{re.sub("</?b>","",p)}</h4>' if re.fullmatch(r"<b>[^<]*</b>", p) else f"<p{lang}>{p}</p>" for p in l["texto"])

def buy(l, cls="buy"):
    return "" if l.get("esgotado") else f'<a class="{cls}" href="{l["compra"]}" target="_blank" rel="noopener">{l.get("botao","comprar")}</a>'

CART_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M3 4h2.2l2.3 11.2a1.5 1.5 0 0 0 1.5 1.2h8.6a1.5 1.5 0 0 0 1.5-1.1L21 8H6.1"/><circle cx="9.5" cy="20" r="1.3"/><circle cx="17.5" cy="20" r="1.3"/></svg>'

def pcents(p):
    return round(float(p.replace("€","").replace(",",".").strip())*100)

def cents(l):
    return pcents(l["preco"])

def cat(l):
    return f'<div class="cat">{" · ".join(l["categoria"])}</div>' if l.get("categoria") else ""

def can_cart(l):
    """vendido pela LAU (passa pelo carrinho); livros vendidos fora (ex.: Amazon) têm só o link"""
    c = l.get("compra", "")
    return not l.get("esgotado") and "mybook.to" not in c and "amazon." not in c and "amzn." not in c

def variants(l):
    """[(slug do carrinho, nome, preço)] — livros com capa mole/rija têm várias"""
    if l.get("variantes"):
        return [(f'{l["slug"]}-{v[0].split()[-1]}', f'{l["titulo"]} ({v[0]})', v[0], v[1]) for v in l["variantes"]]
    return [(l["slug"], l["titulo"], "", l["preco"])]

def buttons(l, round_=False):
    """tudo passa pelo carrinho; livros vendidos fora levam ao sítio onde se compram"""
    if l.get("esgotado"): return ""
    cls = "buyrow" if round_ else "buycol"
    if not can_cart(l):
        return f'<div class="{cls}"><a class="buy" href="{l["compra"]}" target="_blank" rel="noopener">comprar</a></div>'
    out = []
    for slug, nome, var, p in variants(l):
        d = f'data-add-cart data-slug="{slug}" data-title="{esc(nome)}" data-price="{pcents(p)}" data-cover="/img/{l["capa"]}"'
        txt = ((f"{var.split()[-1]} · {p}" if round_ else f"{var} · {p}") if var else ("adicionar" if round_ else "adicionar ao carrinho"))
        out.append(f'<button class="buy addc" {d}>{CART_SVG}<span>{txt}</span></button>')
    return f'<div class="{cls}{" multi" if len(out) > 1 else ""}">{"".join(out)}</div>'

def clamped(l, uid):
    return f'<div class="txt lit"><div id="{uid}" class="clamp">{texto(l)}</div></div><button class="more" data-more="{uid}">Mostrar mais</button>'

def feat(fid, label, video, poster, l):
    a = AUTORES[l["autor"]]
    inner = f"""<video autoplay muted loop playsinline poster="/img/{poster}" style="width:100%;aspect-ratio:16/9;object-fit:cover;border-radius:4px"><source src="/media/{video}" type="video/mp4"></video>
<div class="detail-static"><div class="dtop"><div>{cat(l)}<h3>{esc(l['titulo'])}</h3><div class="who"><a href="/autores/{l['autor']}/">{esc(a['nome'])}</a></div>{preco(l)}</div><img class="dcover" src="/img/{l['capa']}" alt="Capa de {esc(l['titulo'])}"></div>{buttons(l)}{clamped(l, "fx-"+fid)}</div>"""
    return f"""<button class="feature" data-feat="{fid}" aria-label="{re.sub('<[^>]+>','',label)}"><video autoplay muted loop playsinline poster="/img/{poster}"><source src="/media/{video}" type="video/mp4"></video></button>
{acc(fid, label, inner).replace('class="acc"', 'class="acc fp"')}"""

def books_row(livros, pid):
    row = "".join(f"""<div class="bk"><button class="cv" data-detail="{pid}-{l['slug']}"><img src="/img/{l['capa']}" alt="Capa de {esc(l['titulo'])}" loading="lazy"></button>
<h4>{esc(l['titulo'])}</h4><div class="who">{esc(AUTORES[l['autor']]['nome'])}</div>{preco(l)}{buttons(l, True)}</div>""" for i, l in enumerate(livros))
    det = "".join(f"""<div class="detail" id="{pid}-{l['slug']}"><div class="dh"><button class="back" aria-label="voltar">&larr;</button>{esc(l['titulo'])}</div>
<img src="/img/{l['capa']}" alt="">{cat(l)}<h3>{esc(l['titulo'])}</h3><div class="who"><a href="/autores/{l['autor']}/">{esc(AUTORES[l['autor']]['nome'])}</a></div>{preco(l)}
{buttons(l)}{clamped(l, "dx-"+pid+"-"+l["slug"])}</div>""" for i, l in enumerate(livros))
    return f'<div class="row">{row}</div>{det}'

PATRONO_TXT = "Enquanto patrono LAU Edições, terás uma participação ativa no processo editorial: com acesso a trabalhos em desenvolvimento, poderás comentar os textos e o teu nome será mencionado nos livros em cuja edição tenhas participado. Para além disso, terás acesso a exemplares autografados de todas as edições normais futuras e a 20% de desconto nos restantes produtos e serviços, entre outros."
PATRONO_LI = ["Acesso antecipado a WIPs (Works in Progress) selecionados.",
  "Direito a deixar comentários escritos em rascunhos de trabalhos em desenvolvimento, acessíveis aos autores (requer acesso ao Notion)",
  "Exemplares autografados de todos os livros futuros LAU EDIÇÕES (máximo de 1 livro/mês; exclui edições especiais)",
  "Nome destacado na página de agradecimentos das obras para as quais tenha contribuído",
  "20% de desconto nos restantes produtos e serviços"]

# ---------- página da editora ----------
def page_lau():
    lau = [l for l in LIVROS if l.get("lau")]
    rv = "".join(f'<div class="rv"><img src="/img/{next(l["capa"] for l in LIVROS if l["titulo"].startswith(t.split(":")[0]))}" alt="" loading="lazy"><div class="t">{esc(t)}</div><div class="l"><a href="{g}" target="_blank" rel="noopener">goodreads</a><a href="{am}" target="_blank" rel="noopener">amazon</a></div></div>' for t, g, am in REVIEWS)
    pre = f"""<div class="row">
<div class="bk"><button class="cv" data-detail="pre-0"><img src="/img/wip-luz-do-luto.webp" alt="Luz do Luto" loading="lazy"></button><h4>Mourning Light: Luz do Luto</h4><div class="who">Rafael Augusto</div><div class="pr">30€</div><a class="buy" href="https://buy.stripe.com/8x27sL2278BF25o3ck4gg07" target="_blank" rel="noopener">pré-reservar</a></div>
<div class="bk"><button class="cv" data-detail="pre-1"><img src="/img/wip-ao-deus-da-brincadeira.webp" alt="Ao Deus da Brincadeira" loading="lazy"></button><h4>Ao Deus da Brincadeira</h4><div class="who">Rafael Augusto</div><div class="pr">ficção</div><a class="buy" href="{PATREON}" target="_blank" rel="noopener">aceder (LAUWiP)</a></div>
</div>
<div class="detail" id="pre-0"><div class="dh"><button class="back" aria-label="voltar">&larr;</button>Luz do Luto</div><img src="/img/wip-luz-do-luto.webp" alt=""><h3>Mourning Light: Luz do Luto</h3><div class="who">Rafael Augusto</div><div class="pr">30€</div>
<div class="txt lit"><p>O projeto Luz do Luto inclui um livro e um álbum musical. A edição — edição especial do livro, vinil e livro de letras — terá um numero limitado de cópias, que podem ser reservadas através do link.</p><p>Também é possível aceder aos conteúdos antecipadamente através do LAUWiP.</p></div>
<a class="buy" href="https://buy.stripe.com/8x27sL2278BF25o3ck4gg07" target="_blank" rel="noopener">pré-reservar</a><a class="btn alt" href="{PATREON}" target="_blank" rel="noopener">aceder (patronos LAUWiP)</a></div>
<div class="detail" id="pre-1"><div class="dh"><button class="back" aria-label="voltar">&larr;</button>Ao Deus da Brincadeira</div><img src="/img/wip-ao-deus-da-brincadeira.webp" alt=""><h3>Ao Deus da Brincadeira</h3><div class="who">Rafael Augusto · livro, ficção</div>
<a class="buy" href="{PATREON}" target="_blank" rel="noopener">aceder (patronos LAUWiP)</a></div>
<div class="lit" style="font-size:17px;margin-top:6px"><p>Aqui estão os trabalhos em desenvolvimento, alguns quase prontos a lançar, outros em processo de escrita. Podes pré-reservar aqueles que têm um lançamento planeado e, quanto aos outros, tornando-te patrono, podes aceder antecipadamente aos conteúdos e comentá-los, participando no processo editorial.</p></div>"""
    patrono = f"""<div class="lit" style="font-size:17px"><div id="pat-txt" class="clamp"><p>{PATRONO_TXT}</p></div></div><button class="more" data-more="pat-txt">Mostrar mais</button>
<ul class="checks">{"".join(f"<li>{x}</li>" for x in PATRONO_LI)}</ul>
<div class="pr" style="font-family:var(--fd);font-size:18px;margin-top:10px">15€<span class="fb">/mês</span></div><a class="btn" href="{PATREON}" target="_blank" rel="noopener">torna-te patrono</a>"""
    rail = "".join(f'<a class="person" href="/autores/{k}/"><img src="/img/{a["foto"]}" alt="{esc(a["nome"])}" loading="lazy"><span>{esc(a["nome"])}</span></a>' for k, a in AUTORES.items())
    dets = ""
    for k, a in AUTORES.items():
        ls = [l for l in LIVROS if l["autor"] == k and not l.get("esgotado")]
        covers = "".join(f'<a href="/livros/{l["slug"]}/"><img src="/img/{l["capa"]}" alt="{esc(l["titulo"])}"></a>' for l in ls)
        extra = f'<a class="wide" href="{a["pagina"]}">ver página</a>' if a.get("pagina") else ""
        dets += f"""<div class="adet" id="a-{k}"><div class="dh"><button class="back" aria-label="voltar">&larr;</button>{esc(a['nome'])}</div>
<img class="ph" src="/img/{a['foto']}" alt=""><h3>{esc(a['nome'])}</h3>
<div class="lit" style="font-size:18px"><div id="bio-{k}" class="clamp">{"".join(f"<p>{p}</p>" for p in a["bio"])}</div></div><button class="more" data-more="bio-{k}">Mostrar mais</button>
<div class="books">{covers}</div><a class="wide" href="/autores/{k}/">livros de {esc(a['nome'])}</a>{extra}</div>"""

    body = f"""{menu()}
<header class="hero">
  <video autoplay muted loop playsinline poster="/img/poster-hero-lau.jpg"><source src="/media/hero-lau.mp4" type="video/mp4"></video>
  <img class="logo" src="/img/logo-lau-branco.png" alt="LAU Edições">
  <p class="tagline">os nossos livros são resumos dos nossos silêncios.</p>
  {socials([("instagram","Instagram",IG),("email","Email","mailto:"+EMAIL),("whatsapp","WhatsApp",WA),("linkedin","LinkedIn",LI)])}
  <a class="down" href="#conteudo" aria-label="descer"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M12 4v16M6 14l6 6 6-6"/></svg></a>
</header>
<main class="wrap" id="conteudo">
  {feat("destaque","em <b class='k'>destaque</b>","destaque.mp4","poster-destaque.jpg",LIVROS[0])}
  {acc("livros","compra os nossos <b class='k'>livros</b>",books_row(lau,"lv"),icon="icone-l.png")}
  {acc("reviews","deixa uma <b class='k'>review</b>",rv,icon="icone-a.png")}
  {acc("patrono","torna-te <b class='k'>patrono</b> e editor",patrono,icon="icone-u.png")}

  <section class="block authors" id="autores">
    <h2>os nossos <b class='k'>autores</b></h2><div class="h2s">clica na imagem para saber mais</div>
    <div class="arail">{rail}</div>
  </section>

  <section class="block" id="sobre">
    <h3><b class='k'>sobre</b> nós</h3>
    <div class="lit" style="font-size:18px"><div id="sobre-txt" class="clamp"><p>A LAU edições é uma editora independente focada em títulos que, através da ficção, do ensaio, da poesia ou do humor, exploram a mente e a natureza humanas. Achando que, na arte, a forma é tão importante como o conteúdo, damos a cada texto a casa que merece, aliando à qualidade dos textos a identidade visual que nos distingue.</p><p>Se gostavas de participar ativamente no processo editorial, receber em casa livros surpresa, ter acesso a conteúdos de livros em desenvolvimento (sobre os quais poderás dar a tua opinião), e ver teu nome nos agradecimentos de edições futuras em que participes, considera tornar-te patrono (topo da página).</p></div></div>
    <button class="more" data-more="sobre-txt">Mostrar mais</button>
    <div style="margin-top:18px">
      <details class="line"><summary><span>produtos e <b class='k'>serviços</b></span></summary><div class="in lit"><p>Para além de publicarmos livros, fornecemos vários serviços, editoriais e não só, que poderás explorar abaixo. Se gostarias de trabalhar connosco, não hesites em contactar.</p></div></details>
      <details class="line" id="publica"><summary><span><b class='k'>publica</b> connosco</span></summary><div class="in"><div class="lit"><p>Se escreveste ou estás a escrever um livro e gostarias de o publicar, envia uma proposta de edição para <a href="mailto:{EMAIL}">{EMAIL}</a>. Depois da análise, decidiremos se se alinha com o nosso projeto editorial.</p></div><a class="wide" href="mailto:{EMAIL}">fala connosco</a></div></details>
    </div>
  </section>
  {contacts("laueditora.pt/", "/")}
</main>
"""
    write("index.html", head("LAU EDIÇÕES, a nova editora portuguesa independente",
        "Edição de livros — uma estética que se alinha com a qualidade dos conteúdos. Livros, subscrições, serviços, workshops e cursos.",
        "/", "og-lau.jpg", "pt", "lau") + body + FOOT)

# ---------- página pessoal ----------
def page_rafael():
    livros = [l for l in LIVROS if l.get("pessoal")]
    vids = '<div class="car"><div class="slides">' + "".join(f'<div class="sl"><button class="yt" data-yt="{u.rsplit("/",1)[1]}" aria-label="Ver {esc(t)}"><img src="/img/{img}" alt="" loading="lazy"><span class="play"></span></button><h4>{esc(t)}</h4></div>' for t, u, img in VIDEOS) + '</div><button class="cb l" aria-label="anterior"></button><button class="cb r" aria-label="seguinte"></button><div class="dots"></div></div>'
    pubs = '<div class="car"><div class="slides">' + "".join(f'<div class="sl vd" lang="en"><a class="pubimg" href="{u}" target="_blank" rel="noopener"><img src="/img/{img}" alt="" loading="lazy"></a><h4>{esc(t)}</h4><div class="who">{esc(au)}</div><div class="lit"><div id="pub-{k}" class="clamp"><p>{esc(ab)}</p></div></div><button class="more" data-more="pub-{k}">Mostrar mais</button><a class="buy pubgo" href="{u}" target="_blank" rel="noopener">Continue</a></div>' for k, (t, au, u, img, ab) in enumerate(PUBLICACOES)) + '</div><button class="cb l" aria-label="anterior"></button><button class="cb r" aria-label="seguinte"></button><div class="dots"></div></div>'
    wip = f"""<div class="row">
<div class="bk"><img src="/img/wip-luz-do-luto.webp" alt="" loading="lazy" style="aspect-ratio:2/3;object-fit:cover;box-shadow:0 8px 18px rgba(0,0,0,.25)"><h4>Luz do Luto</h4><div class="who">álbum + livro</div><a class="buy" style="margin-top:8px" href="https://buy.stripe.com/8x27sL2278BF25o3ck4gg07" target="_blank" rel="noopener">pré-reserva</a></div>
<div class="bk"><img src="/img/wip-ao-deus-da-brincadeira.webp" alt="" loading="lazy" style="aspect-ratio:2/3;object-fit:cover;box-shadow:0 8px 18px rgba(0,0,0,.25)"><h4>Ao Deus da Brincadeira</h4><div class="who">ficção narrativa</div><a class="buy" style="margin-top:8px" href="{PATREON}" target="_blank" rel="noopener">Continue</a></div></div>"""
    body = f"""{menu()}
<header class="phero">
  <img class="photo" src="/img/fundo-rafael.jpg" alt="Rafael Augusto">
  <div class="info">
    <img class="sig" src="/img/assinatura-branca.png" alt="">
    <h1><span class='fit'>Rafael <b class='k'>Augusto</b></span>{TICK}</h1>
    <div class="sub">Unravelling The Mind | Philosophy, Books &amp; Music</div>
    {socials([("instagram","Instagram",IG),("youtube","YouTube",YT),("spotify","Spotify",SP),("web","Website",WEB),("email","Email","mailto:"+EMAIL),("linkedin","LinkedIn",LI),("whatsapp","WhatsApp",WA)])}
  </div>
</header>
<main class="wrap">
  {feat("now","Now <b class='k'>Available</b>","now-available.mp4","poster-now-available.jpg",next(x for x in LIVROS if x["slug"]=="thinking-animal"))}
  {acc("books","<b class='k'>Books</b>",books_row(livros,"bk"),"livros",caps=True)}
  {acc("music","Music <b class='k'>Videos</b>",vids,"videoclips",caps=True)}
  {acc("academic","Academic <b class='k'>Publications</b>",pubs,"publicações académicas",caps=True)}

  <section class="block" id="practice" lang="en">
    <h2>Philosophical <b class='k'>Practice</b></h2><div class="h2s">Acompanhamento Filosófico</div>
    <h3>Philosophical Practice: An Alternative to therapy, coaches and religions</h3>
    <div class="lit" style="font-size:18px"><p>Besides my PhD in Philosophy and my MsC in Cognitive Science, I was trained by Lydia Amir as a philosophical practitioner. I work with individuals and couples, in Portuguese and English. The first session is for free.</p><p>If you want to know more, read below or click the button to send me a message.</p></div>
    <details class="line" lang="pt"><summary>PT</summary><div class="in lit">{PRATICA_PT}</div></details>
    <details class="line"><summary>EN</summary><div class="in lit">{PRATICA_EN}</div></details>
    <a class="wide" href="{WA}">book a free session | enquire</a>
  </section>

  {contacts("rafaelaugusto.com", WEB)}
</main>
"""
    write("rafaelaugusto/index.html", head("Rafael Augusto | Philosophy, Books & Music",
        "Here you can find my books, my articles, my music, podcasts and other contents.",
        "/rafaelaugusto/", "og-rafael.jpg", "en", "rafael") + body + FOOT)

# ---------- subpáginas (livro e autor) ----------
def page_livro(l):
    a = AUTORES[l["autor"]]
    body = f"""{menu()}
<main class="wrap page livro">
  <img class="cover" src="/img/{l['capa']}" alt="Capa de {esc(l['titulo'])}">
  {cat(l)}<h1>{esc(l['titulo'])}</h1>
  <div class="who"><a href="/autores/{l['autor']}/">{esc(a['nome'])}</a></div>
  {preco(l, "price")}
  {buttons(l)}
  <div class="txt lit">{texto(l)}</div>
  {contacts("laueditora.pt/", "/")}
</main>
"""
    desc = re.sub("<[^>]+>", "", l["texto"][1] if l["texto"][0].startswith("<b>") else l["texto"][0])[:155]
    write(f"livros/{l['slug']}/index.html", head(f"{l['titulo']} — {a['nome']} | LAU Edições", desc, f"/livros/{l['slug']}/", l["capa"]) + body + FOOT)

def page_autor(k, a):
    livros = [l for l in LIVROS if l["autor"] == k]
    grid = "".join(f'<a href="/livros/{l["slug"]}/" style="text-decoration:none"><img src="/img/{l["capa"]}" alt=""><div>{esc(l["titulo"])}</div></a>' for l in livros)
    body = f"""{menu()}
<main class="wrap page">
  <img class="cover" src="/img/{a['foto']}" alt="{esc(a['nome'])}" style="filter:grayscale(1)">
  <h1>{esc(a['nome'])}</h1>
  <div class="txt lit" style="margin-top:14px">{''.join(f'<p>{p}</p>' for p in a['bio'])}</div>
  <section class="block"><h2>livros</h2><div class="grid2">{grid}</div></section>
  {contacts("laueditora.pt/", "/")}
</main>
"""
    desc = re.sub("<[^>]+>", "", a["bio"][0])[:155]
    write(f"autores/{k}/index.html", head(f"{a['nome']} | LAU Edições", desc, f"/autores/{k}/", a["foto"]) + body + FOOT)


def worker():
    import json
    cat = {s: {"name": n, "cents": pcents(p), "img": "/img/" + l["capa"]} for l in LIVROS if can_cart(l) for s, n, v, p in variants(l)}
    t = open(os.path.join(ROOT, "_build/worker_template.js")).read().replace("__CATALOGO__", json.dumps(cat, ensure_ascii=False, indent=2))
    write("_worker/worker.js", t)

def page_obrigado():
    body = f"""{menu()}
<main class="wrap page" style="text-align:center">
  <h1>obrigado</h1>
  <div class="txt lit" style="text-align:center"><p>A tua encomenda foi recebida e o pagamento confirmado. Vais receber um email da Stripe com o recibo, e nós entramos em contacto quando os livros seguirem.</p></div>
  <a class="wide" href="/">voltar à LAU Edições</a>
</main>
<script>try{{localStorage.removeItem('lau-cart')}}catch(e){{}}</script>
"""
    write("obrigado/index.html", head("Obrigado | LAU Edições", "Encomenda recebida.", "/obrigado/", "og-lau.jpg") + body + FOOT)

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
    extras(); worker(); page_obrigado()
    print("ok")
