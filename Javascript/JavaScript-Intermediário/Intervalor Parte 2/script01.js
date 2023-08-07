let timer

//Tempo para rodar a função
function rodar() {
    timer = setTimeout(function() {
        document.querySelector('.demo').innerHTML = 'Rodou'
    
    }, 5000)
    
    /* 1º Par - Função que vai rodar
       2º Par - Tempo que vai esperar até rodar a função
    
       Obs - O SetTimeOut vai rodar uma vez só a função
    */
}

function parar() {
    clearTimeout(timer)
}

