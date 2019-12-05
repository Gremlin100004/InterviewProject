let tx = document.getElementsByTagName('textarea');
for (let i = 0; i < tx.length; i++) {
    tx[i].setAttribute('style', 'height:' + (tx[i].scrollHeight) + 'px;overflow-y:hidden;');
    tx[i].addEventListener("input", OnInput, false);
}

function OnInput(e) {
    this.style.height = 'auto';
    this.style.height = (this.scrollHeight) + 'px';
}

function addcomment() {
    let div = document.getElementById("Comments__show");
    let username_comment =  document.getElementById("username").textContent;
    let a_username = document.createElement('A');
    let p_comment = document.createElement('p');
    let user_text = document.getElementById('comments-text').value;
    let url = document.getElementById('form_add_comment').getAttribute("action");
    let data = {};
    let csrf_token = $('#form_add_comment [name="csrfmiddlewaretoken"]').val();
    data["csrfmiddlewaretoken"] = csrf_token;
    data.username = username_comment;
    data.text_comment = user_text;
    document.getElementById('comments-text').value = '';

    $.ajax({
        url: url,
        type: "POST",
        data: data,
        dataTypes: "html",
    });

    a_username.className = "User__comment";
    a_username.href = '/user/posts_autot/';
    a_username.innerHTML = username_comment;
    p_comment.className = "Post__comment";
    p_comment.innerHTML = user_text;
    div.appendChild(a_username);
    div.appendChild(p_comment);
}

function delete_post(id) {
    let url = '/user/delete/' +id;

    $.ajax({
        url: url,
        type: "get"
    });

    document.getElementById('Post' + id).remove();
}

function delete_comment(id) {
    let url = '/user/deleteComment/' +id;

    $.ajax({
        url: url,
        type: "get"
    });
    document.getElementById('Comment__post' + id).remove();
}

function change_like(id) {
    let number_likes = document.getElementById("number_likes" + id);
    let number_likes_int = parseInt(number_likes.textContent, 10);
    let flag_post = document.getElementById("flag_user" + id);
    let a_like = document.createElement("A");
    let Post__like = document.getElementById("Post__like" + id);
    let url = '/user/addlike/' +id;

    a_like.href = "javascript:change_like(" + id + ");";
    let img = document.createElement("IMG");
    a_like.appendChild(img);

    if (flag_post.textContent == '1'){
        number_likes_int -=1
        img.src = "../../static/Posts/ico/like.png"
        flag_post.innerHTML = '0'
    }
    else {
        number_likes_int +=1
        img.src = "../../static/Posts/ico/like1.png"
        flag_post.innerHTML = '1'
    }

    $.ajax({
        url: url,
        type: "get"
    });

    number_likes.innerHTML = number_likes_int;
    Post__like.innerHTML = '';
    Post__like.appendChild(a_like);
    Post__like.appendChild(document.createTextNode(number_likes_int));
}

