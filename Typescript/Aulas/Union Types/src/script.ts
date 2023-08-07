let idade: string | number = 90

idade = document.getElementById('idade').innerHTML

function mostraridade(idade: string | number) {
    if(typeof idade == 'string') console.log(idade.toLocaleUpperCase())
    
    else console.log(idade)
}

mostraridade('noventa')
mostraridade(90)