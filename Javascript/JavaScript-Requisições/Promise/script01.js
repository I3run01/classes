function pegarTemperatura() {
    return new Promise( (resolve, reject)=>{
        console.log('Pegando temperatura...')

        setTimeout(() => {
            resolve('40 na sombra')
        }, 2000);
    })
}


let temp = pegarTemperatura()
temp.then((resultado)=>{
    console.log(resultado)
})
temp.catch((erro)=>{
    console.log('Deu erro')
})
