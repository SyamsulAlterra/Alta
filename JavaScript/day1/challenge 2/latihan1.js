var judul = document.getElementsByTagName('TITLE')
judul[0].innerHTML="latihan1"

var target = document.getElementById('fill-me')
target.innerHTML = 'HALO!'

target = document.getElementsByClassName('change-all-of-me')
for (let i=0; i<target.length; i++){
    console.log(target[i])
    target[i].innerHTML = 'HALO JUGA!'
}

target = document.getElementById('container').getElementsByTagName('H2')
target[0].innerHTML = 'Apa kabar!'
console.log(target[0])