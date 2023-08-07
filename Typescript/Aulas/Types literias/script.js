"use strict";
function mostrarTexto(texto, alinhamento) {
    return `<div style = "text-align: ${alinhamento}"> ${texto}</div>`;
}
mostrarTexto('Bonieky', 'left');
mostrarTexto('Bonieky', 'right');
mostrarTexto('Bonieky', 'center');
//Nova Função
function configurar(props) {
}
configurar({
    width: 300,
    height: 500
});
configurar('auto');
