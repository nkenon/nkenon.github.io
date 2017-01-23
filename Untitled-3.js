window.onload = setTimeout(function() { alert("Welcome to my portfolio! Click the buttons to go further down my page. Or just scroll down? What happens when you click the first 'O' of my last name??????? Scroll back to top when done? :)"); },1000);

function hoverBigger() {
	var hovered = document.getElementById("hovering");
	hovered.width = 576;
	hovered.height = 324;
}

function hoverNorm() {
	var hoverBye = document.getElementById("hovering");
	hoverBye.width = 192;
	hoverBye.height = 108;
}

function moreabout() {
	var aboutmethings = document.getElementById("aboutme");
	aboutmethings.innerHTML = "I'm currently a rising senior at Stuyvesant High School in NYC. Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo."
}

window.smoothScrollTo = (function () {
  var timer, start, factor;
  
  return function (target, duration) {
    var offset = window.pageYOffset,
        delta  = target - window.pageYOffset; // Y-offset difference
    duration = duration || 1000;              // default 1 sec animation
    start = Date.now();                       // get start time
    factor = 0;
    
    if( timer ) {
      clearInterval(timer); // stop any running animations
    }
    
    function step() {
      var y;
      factor = (Date.now() - start) / duration; // get interpolation factor
      if( factor >= 1 ) {
        clearInterval(timer); // stop animation
        factor = 1;           // clip to max 1.0
      } 
      y = factor * delta + offset;
      window.scrollBy(0, y - window.pageYOffset);
    }
    
    timer = setInterval(step, 10);
    return timer;
  }
}())

// window.smoothScroll = function(target) {
// 	var scrollContainer = target;
// 	do {
// 		scrollContainer = scrollContainer.parentNode;
// 		if (!scrollContainer) return;
// 		scrollContainer.scrollTop += 1;
// 	}
// 	while (scrollContainer.scrollTop == 0);;

// 	var targetY = 0;
// 	do {
// 		if (target == scrollContainer) break;
// 		targetY += target.offsetTop;
// 	}
// 	while (target = target.offsetParent);

// 	scroll = function(c,a,b,i) {
// 		i++, if (i > 30) return;
// 		c.scrollTop = a + (b-a) / 30 * i;
// 		setTimeOut(function(){scroll(c,a,b,i);}, 20);
// 	}
// 	scroll(scrollContainer,scrollContainer.scrollTop, targetY, 0)
// }// JavaScript Document