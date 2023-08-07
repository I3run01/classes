

lista = [
    {id: 1, nome: 'Bonieky', sobrenome: 'Lacerda'},
    {id: 1, nome: 'Paulo', sobrenome: 'XYZ'},
    {id: 1, nome: 'Fulano', sobrenome: 'Da Silva'},
]

let pessoa = lista.find(function(item) {
    return item.sobrenome == 'XYZ'
})

console.log(pessoa)
