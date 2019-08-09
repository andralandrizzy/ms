// Testimonial modal
var modal = document.getElementById('formModal');

// Get the button that opens the modal
var btn = document.getElementById('formTestBtn');

// Get the <span> element that closes the modal
var span = document.getElementsByClassName('modal-close')[0];

// When the user clicks the button, open the modal
btn.onclick = function() {
	modal.style.display = 'block';
};

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
	modal.style.display = 'none';
};

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
	if (event.target == modal) {
		modal.style.display = 'none';
	}
};

// Alert messages fade out
setTimeout(function() {
	$('#message').fadeOut('slow');
}, 6000);

$('#slideshow > div:gt(0)').hide();

setInterval(function() {
	$('#slideshow > div:first').fadeOut(1000).next().fadeIn(1000).end().appendTo('#slideshow');
}, 10000);

//map loader
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
