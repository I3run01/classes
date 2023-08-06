let pessoa = {
    nome: 'Bonieky',
    sobrenome: 'Lacerda',
    idade: 90,
    social: {
        facebook: 'b7web',
        instagram: 'Bonieky'
    },
    nomeCompleto: function() {
        return `${this.nome} ${this.sobrenome}`
    }
}

let {nome: pessoaNome, sobrenome, idade, sexo} = pessoa

console.log(pessoaNome, sobrenome, idade , sexo = 'Masc')
