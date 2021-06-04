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
        }
    });
});




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