function res(usuario: {nome: string, idade?: number}) {
    return `Olá ${usuario.nome} você tem ${usuario.idade} anos`
}

let u = {
    nome: 'Bonieky',
    idade: 90
}

res(u)


//idade?: Passa a ser opcional