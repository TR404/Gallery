//Get the button
var mybutton = document.getElementById("myBtn");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
};

//		For Rotate Image
let rotation = 0;
    function rotateImg() {
      rotation += 90; // add 90 degrees, you can change this as you want
      if (rotation === 360) { 
        // 360 means rotate back to 0
        rotation = 0;
      }
      document.querySelector("#img").style.transform = `rotate(${rotation}deg)`;
    }
