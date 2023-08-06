//Funções

function somar(a, b) {
    return a + b
}

let somar2 = function(a, b) {
    return a + b
}

let somar3 = (a, b) => {
    return a + b 
}

let somar4 = (a, b) => a + b

let dobro = a => a*2

console.log(somar(1,2))
console.log(somar2(2,3))
console.log(somar3(4,7))
console.log(somar4(5,2))
console.log(dobro(2))