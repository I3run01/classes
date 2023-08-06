//Void não permite retorno

const qualquer = (valor: string): void => {
    console.log('Dentro da função')
}

//Excessão 
type Qualquercoisa = () => void

const algo: Qualquercoisa = () => {
    return 'bla bla bla'
}