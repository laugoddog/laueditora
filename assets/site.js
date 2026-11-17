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
})();
