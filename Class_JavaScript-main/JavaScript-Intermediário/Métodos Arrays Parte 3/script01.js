let lista = [45, 4, 9, 16, 25]
let lista2 = []
let lista3 = []
let lista4 = []

//Comando Map -> Vai alterar todos os itens do meu Array
lista2 = lista.map(function(item){
    return item*2
})

//Comando filter, filtra parte do Array
lista3 = lista.filter(function(item) {
    return item < 20
})

//Veritica se todos os itens correposndem ao critério
resp = lista.every(function(item) {
    return item < 50
})

//Verifica se algum item corresponde ao critério
resp2 = lista.some(function(item) {
    return item > 20
})

console.log(lista2)
console.log(lista3)
console.log(resp)
console.log(resp2)