//change title
let title = document.getElementsByTagName('TITLE')[0];
title.innerHTML = 'Tugas Anchor DOM!';

//get div main
let main = document.getElementById('main');

//create content and contentPost, set their attributes
let content = document.createElement('div');
content.setAttribute('id', 'content');
main.appendChild(content);

// loop to create content-post and its children
for (let i=0; i<4; i++){
    let contentPost = document.createElement('div')
    contentPost.setAttribute('class', 'content-post');
    content.appendChild(contentPost);
    
    let judul = document.createElement('H1')
    judul.innerHTML = `Judul Post ${i+1}`
    
    let span = document.createElement('SPAN')
    span.innerHTML = 'Published on 12 May 2016'
    
    let p = document.createElement('P')
    p.innerHTML = 'Lorem Ipsum Dolor Sit Amet'
    
    let button = document.createElement('BUTTON')
    button.setAttribute('class', 'share-post-btn')
    button.setAttribute('value', `post ${i+1}`)
    button.innerHTML = 'Share this post'
    button.addEventListener('click', myFunction)
    
    contentPostChild = [judul, span, p, button]
    for (let i=0; i<contentPostChild.length; i++){
        contentPost.appendChild(contentPostChild[i])
    }
}

let target = document.getElementsByClassName('content-post')[1].children[1].innerHTML = 'Published on 13 May 2016'

function myFunction(){
    let a = this.value
    alert(`You have shared ${a}`)
}