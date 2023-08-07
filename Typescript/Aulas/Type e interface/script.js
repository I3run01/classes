"use strict";
let anos = 90;
function resumo(usuario) {
    return `Olá ${usuario.nome}, você tem ${usuario.idade} anos`;
}
resumo({
    nome: 'Bonieky',
    idade: 90
});
