let nome = 'Bonieky Lacerda Leal'

let resultado = nome.slice(0, 10)  // pega um pedaço da Strng
let resultado2 = nome.slice(10) //pega a partir da decima posição
let resultado3 = nome.slice(-2) //Pega a partir do -2, de trás para frente
let resultado4 = nome.slice(-10, -2 ) //pega da posição -2 até a popsição -10, de trás para frente
let resultado5 = nome.substr(2, 4) //começa na posição 2 e pega 4 caracteres
let resultado6 = nome.substring(2, 6) //da posição 2  até a 6, não funciona com números negativos

console.log(resultado)
console.log(resultado2)
console.log(resultado3)
console.log(resultado4)
console.log(resultado5)
console.log(resultado6)