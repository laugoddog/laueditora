(function(){
  var b=document.body;
  function closeMenu(){b.classList.remove('menu-open');}
  document.querySelectorAll('[data-menu-open]').forEach(function(e){e.addEventListener('click',function(){b.classList.add('menu-open');});});
  document.querySelectorAll('[data-menu-close]').forEach(function(e){e.addEventListener('click',closeMenu);});

  var openModal=null;
  function show(id){var m=document.getElementById(id);if(!m)return;closeAll();m.classList.add('open');b.style.overflow='hidden';openModal=m;}
  function closeAll(){document.querySelectorAll('.modal.open').forEach(function(m){m.classList.remove('open');});b.style.overflow='';openModal=null;}
  document.querySelectorAll('[data-open]').forEach(function(e){e.addEventListener('click',function(ev){ev.preventDefault();var id=e.getAttribute('data-open');show(id);var i=e.getAttribute('data-index');if(i){var it=document.querySelector('#'+id+' .items');if(it)it.scrollLeft=it.clientWidth*(+i);}closeMenu();});});
  document.querySelectorAll('.modal').forEach(function(m){m.addEventListener('click',function(e){if(e.target===m)closeAll();});});
  document.querySelectorAll('[data-close]').forEach(function(e){e.addEventListener('click',closeAll);});
  document.addEventListener('keydown',function(e){if(e.key==='Escape'){closeAll();closeMenu();}});
  document.querySelectorAll('.drawer a').forEach(function(a){a.addEventListener('click',closeMenu);});

  // carrosséis
  document.querySelectorAll('.sheet').forEach(function(s){
    var it=s.querySelector('.items');if(!it)return;
    var n=it.children.length,nav=s.querySelector('.nav');
    if(nav){for(var i=0;i<n;i++)nav.appendChild(document.createElement('i'));}
    function upd(){var k=Math.round(it.scrollLeft/it.clientWidth);if(nav)[].forEach.call(nav.children,function(d,j){d.classList.toggle('on',j===k);});}
    it.addEventListener('scroll',upd);upd();
    s.querySelectorAll('.arrow').forEach(function(a){a.addEventListener('click',function(){it.scrollBy({left:(a.classList.contains('l')?-1:1)*it.clientWidth,behavior:'smooth'});});});
  });

  // mostrar mais
  document.querySelectorAll('[data-more]').forEach(function(btn){btn.addEventListener('click',function(){var t=document.getElementById(btn.getAttribute('data-more'));t.classList.toggle('clamp');btn.textContent=t.classList.contains('clamp')?'Mostrar mais ⌄':'Mostrar menos ⌃';});});

  // abrir popup pelo endereço (#livros, #reviews…)
  if(location.hash){var m=document.getElementById('m-'+location.hash.slice(1));if(m)show(m.id);}
})();
