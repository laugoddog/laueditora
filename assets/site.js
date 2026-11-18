(function(){
const $=(s,r=document)=>r.querySelector(s),$$=(s,r=document)=>[...r.querySelectorAll(s)];
// menu
$$('.burger').forEach(b=>b.onclick=()=>{document.body.classList.add('menu-open');document.documentElement.classList.add('menu-open');});
$$('.drawer .close,.scrim,.drawer a').forEach(e=>e.addEventListener('click',()=>{document.body.classList.remove('menu-open');document.documentElement.classList.remove('menu-open');}));
// secções que abrem
function setOpen(acc,on){if(acc.classList.contains('fp')&&!on){acc.classList.remove('open');setTimeout(()=>{acc.classList.remove('shown');const f=$('[data-feat="'+acc.id+'"]');if(f)f.classList.remove('hide');},450);$('.acc-h',acc).setAttribute('aria-expanded',false);return;}acc.classList.toggle('open',on);$('.acc-h',acc).setAttribute('aria-expanded',on);
  if(!on){const p=$('.panel',acc);p.classList.remove('showing');$$('.detail',p).forEach(d=>d.classList.remove('on'));}}
$$('.acc').forEach(acc=>{$('.acc-h',acc).onclick=()=>setOpen(acc,!acc.classList.contains('open'));
  const x=acc.nextElementSibling;if(x&&x.classList.contains('xbtn'))x.onclick=()=>{setOpen(acc,false);acc.scrollIntoView({behavior:'smooth',block:'center'});};});
// detalhe do livro dentro da secção (showDetail definida abaixo, hoisted)
$$('[data-detail]').forEach(b=>b.onclick=()=>showDetail(document.getElementById(b.dataset.detail)));
$$('.detail .back').forEach(b=>b.onclick=()=>{const p=b.closest('.panel');p.classList.remove('showing');$$('.detail',p).forEach(x=>x.classList.remove('on'));});
// autores
$$('[data-author]').forEach(b=>b.onclick=()=>{const w=b.closest('.authors');$$('.adet',w).forEach(x=>x.classList.remove('on'));
  document.getElementById(b.dataset.author).classList.add('on');w.classList.add('showing');w.scrollIntoView({behavior:'smooth'});});
$$('.adet .back').forEach(b=>b.onclick=()=>{const w=b.closest('.authors');w.classList.remove('showing');$$('.adet',w).forEach(x=>x.classList.remove('on'));});
// mostrar mais
$$('[data-more]').forEach(b=>b.onclick=()=>{const t=document.getElementById(b.dataset.more),c=t.classList.toggle('clamp');b.textContent=c?'Mostrar mais':'Mostrar menos';b.classList.toggle('on',!c);});
// cartão em destaque que abre uma secção
function showDetail(d){const p=d.closest('.panel');$$('.detail',p).forEach(x=>x.classList.remove('on'));d.classList.add('on');p.classList.add('showing');p.style.setProperty('--dh',(d.scrollHeight+10)+'px');d.scrollTop=0;}
$$('[data-acc]').forEach(a=>a.addEventListener('click',e=>{const acc=document.getElementById(a.dataset.acc);if(!acc)return;e.preventDefault();
  const d=a.dataset.show&&document.getElementById(a.dataset.show);setOpen(acc,true);if(d)showDetail(d);
  setTimeout(()=>acc.scrollIntoView({behavior:'smooth',block:'start'}),60);}));
// abrir pela âncora (#livros, #patrono…)
const h=location.hash.slice(1),t=h&&document.getElementById(h);if(t&&t.classList.contains('acc'))setOpen(t,true);
$$('[data-feat]').forEach(f=>f.onclick=()=>{const acc=document.getElementById(f.dataset.feat);f.classList.add('hide');acc.classList.add('shown');fit();
  requestAnimationFrame(()=>requestAnimationFrame(()=>setOpen(acc,true)));});
// carrossel de vídeos
$$('.car').forEach(car=>{const s=$('.slides',car),n=s.children.length,d=$('.dots',car);d.innerHTML='<i></i>'.repeat(n);
  let cur=0,t;const dots=()=>$$('i',d).forEach((x,k)=>x.classList.toggle('on',k===cur));
  const go=k=>{cur=(k+n)%n;s.scrollTo({left:cur*s.clientWidth});dots();};
  $('.cb.l',car).onclick=()=>go(cur-1);$('.cb.r',car).onclick=()=>go(cur+1);
  s.addEventListener('scroll',()=>{clearTimeout(t);t=setTimeout(()=>{cur=Math.round(s.scrollLeft/s.clientWidth);dots();},120);},{passive:true});dots();});
$$('.yt').forEach(b=>b.onclick=()=>{if($('iframe',b))return;const f=document.createElement('iframe');
  f.src='https://www.youtube-nocookie.com/embed/'+b.dataset.yt+'?autoplay=1&rel=0';f.allow='autoplay; encrypted-media; picture-in-picture; fullscreen';f.allowFullscreen=true;b.appendChild(f);$('.play',b).remove();});
// títulos sempre numa linha: reduz a letra até caber
function fit(){$$('.acc-h .tt,.phero h1,.hero .tagline,.phero .sub,.person span').forEach(el=>{if(!el.parentElement.clientWidth)return;el.style.fontSize='';let fs=parseFloat(getComputedStyle(el).fontSize),box=el.parentElement;
  const avail=()=>el.matches('.person span')?box.clientWidth:!el.matches('.tt')?box.clientWidth-(el.matches('h1')?50:16):box.clientWidth-parseFloat(getComputedStyle(box).paddingLeft)-parseFloat(getComputedStyle(box).paddingRight);
  while(el.scrollWidth>avail()&&fs>10){fs-=.5;el.style.fontSize=fs+'px';}});
  const ps=$$('.person span');if(ps.length){const m=Math.min(...ps.map(s=>parseFloat(getComputedStyle(s).fontSize)));ps.forEach(s=>s.style.fontSize=m+'px');}}
(document.fonts&&document.fonts.ready?document.fonts.ready:Promise.resolve()).then(fit);addEventListener('resize',fit);
// carrinho (guardado neste browser)
const EMAIL='geral@laueditora.pt',CHECKOUT='https://lau-checkout.rafael-coelho-nascimento.workers.dev/';// endereço do Worker da Cloudflare (…workers.dev); vazio = encomenda por email
let cart=[];try{cart=JSON.parse(localStorage.getItem('lau-cart')||'[]')}catch(e){}
const eur=c=>(c/100).toFixed(2).replace('.',',').replace(',00','')+'€';
function saveCart(){try{localStorage.setItem('lau-cart',JSON.stringify(cart))}catch(e){}renderCart();}
function renderCart(){const n=cart.reduce((s,i)=>s+i.q,0);$$('.cartbtn .cnt').forEach(c=>{c.hidden=!n;c.textContent=n;});
  $$('.cart').forEach(box=>{const l=$('.clist',box);
    l.innerHTML=cart.length?cart.map((i,k)=>`<div class="ci"><img src="${i.cover}" alt=""><div class="t">${i.title}<span>${eur(i.price)}</span></div><div class="q"><button data-q="${k}" data-d="-1" aria-label="menos">−</button>${i.q}<button data-q="${k}" data-d="1" aria-label="mais">+</button></div></div>`).join(''):'<p class="cempty">O carrinho está vazio.</p>';
    $('.ctot b',box).textContent=eur(cart.reduce((s,i)=>s+i.price*i.q,0));$('.cfoot',box).style.display=cart.length?'':'none';
    $$('[data-q]',l).forEach(b=>b.onclick=()=>{const i=cart[+b.dataset.q];i.q+=+b.dataset.d;if(i.q<1)cart.splice(+b.dataset.q,1);saveCart();});
    const body='Olá,\n\nGostaria de encomendar:\n'+cart.map(i=>`- ${i.q} × ${i.title} (${eur(i.price)})`).join('\n')+`\n\nTotal: ${eur(cart.reduce((s,i)=>s+i.price*i.q,0))} + portes\n\nNome:\nMorada de envio:\nNIF (opcional):\n\nObrigado.`;
    $('.cgo',box).href='mailto:'+EMAIL+'?subject='+encodeURIComponent('Encomenda — LAU Edições')+'&body='+encodeURIComponent(body);});}
function setCart(on){document.body.classList.toggle('cart-open',on);document.documentElement.classList.toggle('cart-open',on);}
$$('[data-cart-open]').forEach(b=>b.onclick=()=>setCart(true));
$$('[data-cart-close],.scrim').forEach(b=>b.addEventListener('click',()=>setCart(false)));
$$('[data-add-cart]').forEach(b=>b.onclick=()=>{const d=b.dataset,i=cart.find(x=>x.slug===d.slug);
  if(i)i.q++;else cart.push({slug:d.slug,title:d.title,price:+d.price,cover:d.cover,q:1});saveCart();
  $$('.cartbtn').forEach(c=>{c.classList.remove('added');void c.offsetWidth;c.classList.add('added');});
  b.classList.remove('added');void b.offsetWidth;b.classList.add('added');});
$$('.cgo').forEach(a=>a.addEventListener('click',async e=>{if(!CHECKOUT||!cart.length)return;e.preventDefault();a.textContent='a abrir o pagamento…';
  try{const r=await fetch(CHECKOUT,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({zona:($('.czona select')||{}).value||'pt',items:cart.map(i=>({slug:i.slug,q:i.q}))})});const d=await r.json();
    if(d.url){location.href=d.url;return;}throw new Error(d.error);}catch(err){a.textContent='finalizar encomenda';alert('Não foi possível abrir o pagamento. Tenta de novo ou escreve para '+EMAIL+'.');}}));
if(new URLSearchParams(location.search).has('carrinho'))setCart(true);
renderCart();
// cabeçalho: na página inicial aparece aos poucos no fim do vídeo
const hero=$('header.hero'),bar=$('.topbar');
if(hero&&bar){document.body.classList.add('has-hero');const upd=()=>{const end=hero.offsetHeight,y=scrollY,o=Math.max(0,Math.min(1,(y-(end-220))/180));
  bar.style.opacity=o;bar.style.pointerEvents=o>.5?'auto':'none';};addEventListener('scroll',upd,{passive:true});addEventListener('resize',upd);upd();}
})();
