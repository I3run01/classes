function loadPosts() {
    fetch('https://jsonplaceholder.typicode.com/posts')  //Requisição
        .then(r=> r.json())  //Abre a a versão em JSON  
        .then( j=> montarBlog(j) ) //Joga o Json na função que preciso
        .catch( e=> console.log('Deu problema')) //Se erro
}

function montarBlog(lista) {
    let html = ''

    for( let i in lista) {
        html += `<h3> ${lista[i].title} </h3>`
        html += lista[i].body + '<br/>'
        html += '<hr/>'
    }

    document.querySelector('#post02').innerHTML = html
}