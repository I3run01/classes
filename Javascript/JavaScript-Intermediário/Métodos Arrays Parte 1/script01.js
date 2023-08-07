let lista = ['Ovo', 'Farinha', 'Corante', 'Massa']
let listaex2 = ['Ovo', 'Farinha', 'Corante', 'Massa']
let listaex3 = ['Ovo', 'Farinha', 'Corante', 'Massa']
let listaex4 = ['Ovo', 'Farinha', 'Corante', 'Massa']
let listaex5 = ['Ovo', 'Farinha', 'Corante', 'Massa']
let listaex6 = ['Ovo', 'Farinha', 'Corante', 'Massa']


let res = lista.toString() //Junta tudo m uma String, separados por uma virgula
let res2 = lista.join('-') //Junta todos os itens, separados por - ou qualquer elemento que eu colocar na função
let res3 = lista.indexOf('Corante') // Procura a posição do corante, se não achar, retorna -1
listaex2.pop() //Remove o último item do meu Array
listaex3.shift() //Remove o primeiro item do meu Array
listaex4.push('prato')
listaex5[1] = 'Massa' // O indíce com a farinha passa a conter massa
listaex6[4] = 'Liquidificador' //Se o indice não existir, ele adiciona com o valor informado

console.log(res)
console.log(res2)
console.log(res3)
console.log(listaex2)
console.log(listaex3)
console.log(listaex4)
console.log(listaex5)
console.log(listaex6)