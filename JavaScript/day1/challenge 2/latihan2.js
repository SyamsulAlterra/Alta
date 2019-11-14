var judul = document.getElementsByTagName('TITLE')[0].innerHTML = 'Tugas ANCHOR DOM'

var target = document.getElementById('eldest-parent').children
target[0].innerHTML = 'Diakses Melalui Eldest Parent'

target2 = target[0].nextElementSibling.children[0].children
for (let i=0; i<target2.length; i++){
    if (i != 1){
        target2[i].innerHTML='Diakses Melalui a Child'
    }
}

target3 = target[2].innerHTML = 'Diakses Melalui a Child'