async function loadPosts() {

    let req = await fetch('https://jsonplaceholder.typicode.com/posts')
    let json = await req.json()
    montarBlog(json)

}

function montarBlog(lista) {
    let html = ''
    console.log(lista)

    for( let i in lista) {
        html += `<h3> ${lista[i].title} </h3>`
        html += lista[i].body + '<br/>'
        html += '<hr/>'
    }

    document.querySelector('#post02').innerHTML = html
}