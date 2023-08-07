let lista = ['Ovo', 'Farinha', 'Corante', 'Massa']
let lista02 = ['Ovo', 'Farinha', 'Corante', 'Massa']
let lista03 = ['Prato', 'Liquidificador', 'Forno']
let lista04 = ['Ovo', 'Farinha', 'Corante', 'Massa']
let lista05 = ['Ovo', 'Farinha', 'Corante', 'Massa']

lista.splice(1, 1)
/* 1 par -> Qual item será removido
   2 par -> Quantos itens a partir dele tamém serão removidos */

lista02.splice(1) // Vai apagar do primeiro item para frente

resp = lista.concat(lista03) //Vai concatenar lista com lista 2

lista04.sort() // Coloca em ordem alfabética ou crescente

lista05.reverse() //Inverte a ordem da lista -> pode ser usado para deixar em ordem decrescente


console.log(lista)
console.log(lista02)
console.log(resp)
console.log(lista04)
console.log(lista05)
