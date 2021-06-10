$(document).on("keypress", "form", function(event) {
    if (event.keyCode == 13 ) {
    event.preventDefault()
    return false ;
    }
});

$(function() {
    $('#send').on('click', function(event) {
        event.preventDefault()
        var userInput = $('#msg').val();
        if ( userInput !== "") {
            addUserMsg(userInput);
            $(".loader").css({display:"block"})

            $.getJSON(
                '/query',
                {'query' : userInput},
                function (data) {

					if (data.error) {
					    addGrandpyMsg(data.msg_fail);
						$("#map").css({display:"none"});
					}
					else {
					    addGrandpyMsg(data.msg_gmaps);
					    addGrandpyMsg(data.msg_wiki);
						var lat = (data.lat);
						var lng = (data.lng);

	                    initMap(lat, lng);
	                    $("#map").css({display:"block"});
					}
					$(".loader").css({display:"none"});
				}
            );
        }
    });
});

function addGrandpyMsg(message) {

    var grandpyMsg = document.createElement("strong");
    grandpyMsg.appendChild(document.createTextNode('GrandPy: '));

    var divMsg = document.createElement('div');
    divMsg.classList.add('msg_cotainer');
    divMsg.appendChild(grandpyMsg);
    divMsg.appendChild(document.createTextNode(message));

    divCard = document.createElement('div');
    divCard.classList.add('grandpy-msg');
    divCard.appendChild(divMsg);

    document.getElementById('chat').append(divCard);

}


function addUserMsg(message) {

    var userMsg = document.createElement("strong");
    userMsg.appendChild(document.createTextNode('User: '));

    var divMsg = document.createElement('div');
    divMsg.classList.add('msg_cotainer_send');
    divMsg.appendChild(userMsg);
    divMsg.appendChild(document.createTextNode(message));

    divCard = document.createElement('div');
    divCard.classList.add('user-msg');
    divCard.appendChild(divMsg);

    document.getElementById('chat').append(divCard);
}

function initMap(lat, lng) {

	var pos = {lat: parseFloat(lat), lng: parseFloat(lng)};
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 10,
        center: pos,
        mapId: 'f6b0d0ad6549a0cb',
    });

    var marker = new google.maps.Marker({
        position: pos,
        map: map
    });
}