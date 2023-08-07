function mostrarTexto(
    texto: string,
    alinhamento: 'left'| 'right'| 'center'
)

{
    return `<div style = "text-align: ${alinhamento}"> ${texto}</div>`
}

mostrarTexto('Bonieky', 'left')
mostrarTexto('Bonieky', 'right')
mostrarTexto('Bonieky', 'center')

//Nova Função

function configurar(props: {width: number, height: number} | 'auto') 
{

}

configurar({
    width: 300,
    height: 500
})
configurar('auto')
