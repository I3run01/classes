let cartao = '1234567812341234'

let numeroSeg = cartao.slice(12)
console.log(numeroSeg.padStart(16, '*'))
