let pessoa = {
    nome: 'Bonieky',
    sobrenome: 'Lacerda',
    idade: 90,
    social: {
        facebook: {
            nomeface: 'Bonieky',
            url: '@faceBonieky'
        },
        instagram: {
            url: '@Bonieky',
            seguidores: 1000
        }
    },
}

//Criando o nome completo a partir de um objeto
function pegarNomeCompleto(obj) {
    return `Siga ${obj.nome} ${obj.sobrenome} em ${obj.social.instagram.url}`
}

nomeCompleto = pegarNomeCompleto(pessoa)
console.log(nomeCompleto)

//Criando variáveis para o meu objeto
let {nome, idade,social: {facebook}, social: {instagram: {url: instagram, seguidores}}} = pessoa

console.log(nome, idade, instagram, seguidores, facebook)