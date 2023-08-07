function loadPosts() {
    document.querySelector('#post').innerHTML = 'Carregando...'
    fetch('https://jsonplaceholder.typicode.com/posts')
        .then((resultado)=>{
            return resultado.json()
        })
        .then((json)=> {
            console.log(json)
            document.querySelector('#post').innerHTML = json.length + ' posts'
        })
        .catch(()=>{
            console.log('Deu problema')
        })
}

