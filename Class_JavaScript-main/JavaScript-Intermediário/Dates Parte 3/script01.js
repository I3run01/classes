let data01 = new Date()
let data02 = new Date()

data01.setFullYear(2018) // Troca a data para 2018
data01.setMonth(9) //Troca o mês para Outubro
data02.setDate( data02.getDate() + 5) //Data atual + 5 dias // Vale para horas, segundos...

console.log(data01)
console.log(data02)