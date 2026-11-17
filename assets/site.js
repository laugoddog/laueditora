(function(){
  var b=document.body;
  function open(){b.classList.add('menu-open');}
  function close(){b.classList.remove('menu-open');}
  document.querySelectorAll('[data-menu-open]').forEach(function(e){e.addEventListener('click',open);});
  document.querySelectorAll('[data-menu-close]').forEach(function(e){e.addEventListener('click',close);});
  document.querySelectorAll('.drawer a').forEach(function(a){a.addEventListener('click',close);});
  document.addEventListener('keydown',function(e){if(e.key==='Escape')close();});
})();
