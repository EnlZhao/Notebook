document.addEventListener('DOMContentLoaded', function() {
    const marquee = document.querySelector('.marquee');
    if (marquee) {
      marquee.addEventListener('mouseover', function() {
        marquee.style.animationPlayState = 'paused';
      });
      marquee.addEventListener('mouseout', function() {
        marquee.style.animationPlayState = 'running';
      });
    }
  });
  