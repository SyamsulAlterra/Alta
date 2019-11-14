function generateAlphaBetBoard(){
    alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = []
    for (let i=0; i<9; i ++){
        let fill = []
        for (let j=0; j<9; j++){
            let num = Math.floor(Math.random()*(alphabet.length-1))
            fill.push(alphabet[num])
        }
        result.push(fill)
    }
    return result
}


function createSegment(nom, box){
    let num=nom-1
    let row = (Math.floor(num/3))*3
    let column = (num%3)*3
    let result=[]
    for (let i=0; i<3; i++){
        for (let j=0; j<3; j++){
            result.push(box[row+i][column+j])
        }
    }
    return result
}

function checkConsonant(char){
    vowels = 'aeiou'
    for (let i=0; i<vowels.length; i++){
        if (char.toLowerCase() == vowels[i]){
            return false
        }
    }
    return true
}

function checkConsonantInBox(nom, box){
    let num = nom-1
    let segment = createSegment(nom,box)
    let side = segment.length
    for (let i=0; i<side; i++){
        if (checkConsonant(segment[i]) == false){
            return false
        }
    }
    return true
}

function generateArrayOfObject(box){
    result=[]
    for (let i=0; i<9; i++){
        let dict = {}
        dict['box_area'] = i+1
        dict['value'] = createSegment(i+1,box)
        dict['all_consonant_in_box'] = checkConsonantInBox(i+1, box)
        result.push(dict)
    }
    return result
}

let box = generateAlphaBetBoard()
console.log(box)

console.log(generateArrayOfObject(box))


