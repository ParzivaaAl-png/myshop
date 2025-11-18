// static/js/main.js
document.addEventListener('DOMContentLoaded', function(){
  // gallery thumbnail click
  document.querySelectorAll('.thumb').forEach(function(t){
    t.addEventListener('click', function(){
      var src = t.getAttribute('data-src');
      var main = document.getElementById('mainImage');
      if(main && src){
        main.src = src;
      }
    });
  });
});
