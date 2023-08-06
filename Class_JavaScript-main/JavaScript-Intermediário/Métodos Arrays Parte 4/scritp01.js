let lista = [45, 4, 9, 16, 25]
let lista2 = []
let lista3 = []

//Retorna o primeiro item que satifaça a condição
lista2 = lista.find(function(item) {
    return item == 16
})

//Retorna a posição que satifaça a condição
lista3 = lista.findIndex(function(item) {
    return item == 16
})

console.log(lista2)
console.log(lista3)