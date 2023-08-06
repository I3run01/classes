function mostrar() {
    document.getElementById('area2').innerHTML = "Teste"

    let reader = new FileReader()
    let imagem = document.getElementById('imagem').files[0]

    reader.onloadend = () => {
        let img = document.createElement('img')
        img.scr = reader.result
        img.width = 200


        document.getElementById('area').appendChild(img)
    }

    reader.readAsDataURL(imagem)

    
}