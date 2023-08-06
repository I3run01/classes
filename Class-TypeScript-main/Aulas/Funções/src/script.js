"use strict";
function firstLetterUpperCase(name) {
    let firstLetter = name.charAt(0).toUpperCase();
    return firstLetter.substring(1);
}
function somar(n1, n2) {
    return n1 + n2;
}
let nomes = ['Bonieky', 'Pedro', 'Paulo', 90];
nomes.forEach(function (nome) {
    if (typeof nome == 'string') {
        console.log(nome.toUpperCase());
    }
    else {
        console.log(nome);
    }
});
