const a = new ArrayBuffer(6); // aqui criamos um array buffer no JS

console.log(a); // 'e uma serie de 0' <00 00 00 00 00 00>

// agora vamos interpretar esse 0 de alguma forma

const a8 = new Uint8Array(a); // unsined 8bit number , ous eja um numero entre 1 e 255

a8[0] = 45;

a8[2] = 45;

console.log(a);
