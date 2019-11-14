const moment = require('moment')
const lodash = require('lodash')
const mathjs = require('mathjs')
const Spinner = require('cli-spinner').Spinner
const cliGraph = require('cli-graph')

console.log('===================')
console.log('moment')
console.log('===================')
console.log(moment().format('D MMMM YYYY, h:mm:ss a'))
console.log(moment.locale())
console.log(moment().add(120, 'days').calendar())

console.log('')
console.log('===================')
console.log('lodash')
console.log('===================')
console.log(lodash.kebabCase('enak tenan halo'))
console.log(lodash.camelCase('enak tenan halo'))
console.log(lodash.snakeCase('enak tenan halo'))

console.log('')
console.log('===================')
console.log('mathjs')
console.log('===================')
console.log(mathjs.simplify('1/x+x+x+x+2x-5y', {x:2, y:4}).toString())
console.log(mathjs.derivative('tan(x)', 'x').toString())
let a=mathjs.complex(-1,0)
let b=mathjs.complex(3,-10)
console.log(a.toString())
console.log(mathjs.add(a,b).toString())
console.log(mathjs.complex(a).toPolar())

console.log('')
console.log('===================')
console.log('cli-graph')
console.log('===================')
let g1 = new cliGraph({
    height: 40,
    width: 40,
    center: {y: 20}
}).setFunctionX(function(x){
    return Math.sin(x)+x;
})

console.log(g1.toString())

console.log('')
console.log('===================')
console.log('spinner')
console.log('===================')
let spinner = new Spinner('processing.. %s')
// spinner.setSpinnerDelay(0)
spinner.setSpinnerString('|\-//')
spinner.start()
console.log(spinner.isSpinning())
// console.log(a)