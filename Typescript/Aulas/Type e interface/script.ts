type Idade = string| number

let anos: Idade = 90

//Fim - Inicio de matéria

//Type não muda
type user = {
    nome: string,
    idade: number
}

//Interface muda
interface user02 {
    nome: string,
    idade: number,
}

interface user02 {
    dade: number,  
}

function resumo(usuario: user) {
    return `Olá ${usuario.nome}, você tem ${usuario.idade} anos`
}

resumo(
    {
        nome: 'Bonieky',
        idade: 90
    }
)

