// promise

const beliPromise = require('./beli-2');

let sandal = {
  item: 'sandal',
  harga: 2000,
  waktu: 2000,
};
let tas = {
  item: 'tas',
  harga: 2000,
  waktu: 2000,
};
let kaos = {
  item: 'kaos',
  harga: 2000,
  waktu: 2000,
};
let jaket = {
  item: 'jaket',
  harga: 2000,
  waktu: 2000,
};
let topi = {
  item: 'topi',
  harga: 2000,
  waktu: 2000,
};

beliPromise(100000, sandal)
  .then(kembalianSandal => {
    return beliPromise(kembalianSandal, tas);
  })
  .then(kembalianTas => {
    return beliPromise(kembalianTas, kaos);
  })
  .then(kembalianKaos => {
    return beliPromise(kembalianKaos, jaket);
  })
  .then(kembalianJaket => {
    return beliPromise(kembalianJaket, topi);
  })
  .then(kembalianTopi => {
    console.log(`Kembalian membeli sandal, tas, kaos, jaket dan topi adalah ${kembalianTopi}`);
  })
  .catch(error => {
    console.log(error);
  })

console.log('halo :)')