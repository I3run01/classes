"use strict";
let idade = 90;
idade = document.getElementById('idade').innerHTML;
function mostraridade(idade) {
    if (typeof idade == 'string')
        console.log(idade.toLocaleUpperCase());
    else
        console.log(idade);
}
mostraridade('noventa');
mostraridade(90);
