function beli(uang, obj, cb){
  console.log(`Saya pergi membeli ${obj.item}`)
  setTimeout(function(){
    let kembalian = uang - obj['harga']
    cb(kembalian)// your code here
  }, obj.waktu);
}

module.exports = beli;
