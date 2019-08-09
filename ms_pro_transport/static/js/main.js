// Testimonial modal
// var modal = document.querySelector('#formModal');
// var btnForm = document.querySelector('#formTestBtn');
// var span = document.querySelector('.modal-close');

// btnForm.addEventListener('click', function styleDisplay() {
// 	modal.style.display = 'block';
// });

// span.addEventListener('click', function closeBtn() {
// 	modal.style.display = 'none';
// });

// window.addEventListener('click', function styleDisplay(e) {
// 	if (e.target === modal) {
// 		modal.style.display = 'none';
// 	}
// });

// ALERT MESSAGES FADE OUT
setTimeout(function() {
	$('#message').fadeOut('slow');
}, 6000);

$('#slideshow > div:gt(0)').hide();

setInterval(function() {
	$('#slideshow > div:first').fadeOut(1000).next().fadeIn(1000).end().appendTo('#slideshow');
}, 10000);

//GOOGLE MAP LOADER
function initMap() {
	// The location of Uluru
	var uluru = { lat: 25.8102373, lng: -80.1751609 };
	// The map, centered at Uluru
	var map = new google.maps.Map(document.getElementById('map'), { zoom: 4, center: uluru });
	// The marker, positioned at Uluru
	var marker = new google.maps.Marker({ position: uluru, map: map });
}

$(document).ready(function() {
	$('.button-collapse').sideNav();
});

// CLIENT SLIDER
// var slideIndex = 0;
// showSlides(slideIndex);

// function showSlides() {
// 	var i;
// 	var slides = document.getElementsByClassName('client-testimonial-content');
// 	var dots = document.getElementsByClassName('dot');
// 	for (i = 0; i < slides.length; i++) {
// 		slides[i].style.display = 'none';
// 	}
// 	slideIndex++;
// 	if (slideIndex > slides.length) {
// 		slideIndex = 1;
// 	}
// 	for (i = 0; i < dots.length; i++) {
// 		dots[i].className = dots[i].className.replace(' active', '');
// 	}
// 	slides[slideIndex - 1].style.display = 'block';
// 	dots[slideIndex - 1].className += ' active';
// 	setTimeout(showSlides, 6000); // Change text every 2 seconds
// }
