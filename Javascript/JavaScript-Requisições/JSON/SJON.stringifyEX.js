let busca = {input: 'bon'}
let buscaString = JSON.stringify(busca)

let resultado = '{"lista": ["Bonieky","bonieky lacerda","bonito"]}'
let resultadoJSON = JSON.parse(resultado)

console.log(buscaString)
console.log(resultadoJSON)