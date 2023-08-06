//Cria Uma data baseada nas informação abaixo: 
let d2 =  new Date(2020, 0, 1, 12, 30, 12)
/* 
Parâmetros:
    1º -> Ano 
    2º -> Mês (Vai do 0 ao 11, Jan -> Dez)
    3º -> Dia (Começa do 1)
    4º ->  Hora
    5º -> Minutos
    6º -> Segundos
*/

//Outra forma de colocar datas
let d3 = new Date('2020-01-01 15:42:17')

//Milissegundos depois de 1970 de Greenwitch
let d4 = new Date(2324245462)


console.log( d2.toString() )
console.log( d3.toString() )
console.log( d4.toString() )