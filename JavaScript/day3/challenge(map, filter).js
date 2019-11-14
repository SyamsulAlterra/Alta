let bdays = ['10-17', '05-19', '20-19']
let newBdays = bdays.map( days => {
    return days.replace('-','/')
})

console.log(newBdays) //[ '10/17', '05/19', '20/19' ]

let value = [1,2,3,4,5,6]
let newValue = value.map( num => {
    return num*2
})

console.log(newValue) //[ 2, 4, 6, 8, 10, 12 ]

let arr = [1.5, 2.56, 5.1, 12.33]
let rounded = arr.map( dec => {
    return Math.ceil(dec)
})

console.log(rounded) //[ 2, 3, 6, 13 ]

let nums = [1,2,3,4]
let sum = nums.reduce( (total, num) => {
    return total+=num
})

console.log(sum) // 10

let filterValue = [-4,3,2,-21,1]
let pos = filterValue.filter(num => {
    return num>0
})

console.log(pos) //[3,2,1]


let data = [
    {name: 'daniel', age:45},
    {name: 'john', age:30},
    {name: 'robert', age:null},
    {name: 'jen', age:undefined},
    {name: null, age:undefined},    
]
let dataMod = data.filter( dict => {
    return !(dict['name'] === undefined || dict['age'] === undefined)
})

console.log(null === null)
console.log(dataMod)