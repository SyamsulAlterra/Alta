function beliPromise(uang, obj) {
    return new Promise((resolve, reject) => {
      console.log(`Saya pergi membeli ${obj.item}`)
      setTimeout(function() {
        let kembalian = uang - obj.harga
        resolve(kembalian)// your code here
      }, obj.waktu);
    });
  }
  
  module.exports = beliPromise;