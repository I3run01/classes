function adicionar(nomes, ...novosNomes) {
    return [...novosNomes, ...nomes]
}

let nomes = ['Bonieky', 'Paulo']
let outros = adicionar(nomes,'Antonio', 'Maria', 'José')

console.log(outros)