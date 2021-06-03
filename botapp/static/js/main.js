
function addQuery(event) {
    event.preventDefault();
    const newElt = document.getElementById('chat');
    let divContent = '<div class="d-flex justify-content-end mb-4"><div class="msg_cotainer_send">test</div></div><div class="img_cont_msg">
                     '<img src="{{url_for("static", filename="assets/img/user.png")}}" class="rounded-circle user_img_msg"></div>' ;
    newElt.insertAdjacentHTML('beforeend', divContent) ;

};


const submitButton = document.getElementById('send');
submitButton.addEventListener('click', addQuery);