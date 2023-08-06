let nome = 'Bonieky Lacerda Leal'

let const1 = nome.length //->Tamanho da string
let const2 = nome.indexOf('Lacerda') //A onde começa o lacerda - > Se não achar, retorna -1

console.log(const1)
console.log(const2)

//Condicional se tem ou não Lacerda na String
if(nome.indexOf('ghef') > -1 ) {
    console.log('Achou')

}

else  console.log('Não achou')