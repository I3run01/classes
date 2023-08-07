let info = ['Bonieky Lacerda', 'Bonieky', 'Lacerdar', '@Bonieky']
let info02 = ['Bonieky Lacerda', 'Bonieky', 'Lacerdar', '@Bonieky']

//Pegar as Variáveis
let [nomeCompleto, nome, sobrenome, instagram ] = info

//Pegar Algumas variáveis
let [nomeCompleto02, , , instagram02 ] = info02

console.log(nomeCompleto, nome, sobrenome, instagram )
console.log(nomeCompleto02, instagram02 )

//A descontrução do Array é feita na ordem