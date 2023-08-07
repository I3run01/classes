function adicionarInfo(info) {
    let novasInfo = {
        ...info,
        status: 0,
        token: 'sjghsi',
        data_cadastro: '.....'
    }

    return novasInfo
}

let antigainfo = {nome: 'Bonieky', sobrenome: 'Lacerda'}
let novasinfo = adicionarInfo(info)
console.log(novasinfo)