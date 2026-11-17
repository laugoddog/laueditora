(function(){
const $=(s,r=document)=>r.querySelector(s),$$=(s,r=document)=>[...r.querySelectorAll(s)];
// menu
$$('.burger').forEach(b=>b.onclick=()=>document.body.classList.add('menu-open'));
$$('.drawer .close,.scrim,.drawer a').forEach(e=>e.addEventListener('click',()=>document.body.classList.remove('menu-open')));
// secções que abrem
function setOpen(acc,on){acc.classList.toggle('open',on);$('.acc-h',acc).setAttribute('aria-expanded',on);
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
$$('[data-more]').forEach(b=>b.onclick=()=>{const t=document.getElementById(b.dataset.more),c=t.classList.toggle('clamp');b.textContent=c?'Mostrar mais ⌄':'Mostrar menos ⌃';});
// cartão em destaque que abre uma secção
function showDetail(d){const p=d.closest('.panel');$$('.detail',p).forEach(x=>x.classList.remove('on'));d.classList.add('on');p.classList.add('showing');p.style.setProperty('--dh',(d.scrollHeight+10)+'px');d.scrollTop=0;}
$$('[data-acc]').forEach(a=>a.addEventListener('click',e=>{const acc=document.getElementById(a.dataset.acc);if(!acc)return;e.preventDefault();
  const d=a.dataset.show&&document.getElementById(a.dataset.show);setOpen(acc,true);if(d)showDetail(d);
  setTimeout(()=>acc.scrollIntoView({behavior:'smooth',block:'start'}),60);}));
// abrir pela âncora (#livros, #patrono…)
const h=location.hash.slice(1),t=h&&document.getElementById(h);if(t&&t.classList.contains('acc'))setOpen(t,true);
})();
