let data = new Date()

let ano = data.getFullYear()
let mes = data.getMonth() //Janeiro - 0
let dia_da_semana = data.getDay() //Domingo - 0
let dia_do_mes = data.getDate()
let hora = data.getHours()
let minutos = data.getMinutes()
let segundo = data.getSeconds()
let Milissegundos = data.getMilliseconds()
let Milissegundos_desde_1970 = data.getTime() //Milissegundo desde 1970
let Agora_desde_1970 = Date.now()

console.log(ano)
console.log(mes)
console.log(dia_da_semana)
console.log(dia_do_mes)
console.log(hora)
console.log(minutos)
console.log(segundo)
console.log(Milissegundos)
console.log(Milissegundos_desde_1970)
console.log(Agora_desde_1970)