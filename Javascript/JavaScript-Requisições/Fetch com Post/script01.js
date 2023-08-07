async function inserirPost() {
    document.querySelector('#posts').innerHTML = 'carregando...'

    let req = await fetch('https://jsonplaceholder.typicode.com/posts', {
        method: 'POST', //Modelo de requisição
        body: JSON.stringify({
            userId: 110,
            id:1000,
            title: 'Titulo de teste',
            body: 'Corpo de teste',
            
        }),
        headers: {
            'Content-Type': 'application/json' //Para criar suas próprias JSON
        }
    })

    let json = await req.json()

    console.log(json)
}

/*
POST = CRIAR
PUT = ATUALIZAR
GET = LISTAR
DELETE = DELETAR
*/