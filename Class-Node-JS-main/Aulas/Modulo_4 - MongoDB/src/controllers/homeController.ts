import { Request, Response } from 'express';

import { Product } from '../models/Product';
import  User  from '../models/User'

export const home = async (req: Request, res: Response)=>{

    /*
        gt = Greater then
        gte = Greater then or Equal
        lt = Less then
        lte = Less then or equal
    */

    //Pega todos os usuários e coloca em um Array
    let usuarios = await User.find({})

    //~Achar um usuário - TESTADO
    let usuario = await User.findOne({
        email: 'suporte@b7web.com.br',
        age: 90
    })

    //Achar o usuário pelo ID
    let usuario02 = await User.findById('629e8a24f6292723ded118a0')

    //Achar usuário dentro de uma pasta 
    let usuario03 = await User.find({
        "name.firstname": 'Paulo'
    })
    
    //usuários com interesses em tecnologias
    let usuario04 = await User.find({
        interests: 'tecnologia'
    })
    
    //usuários com mais de 18 anos
    let usuario05 = await User.find({
        age: { $gt:18 } //Greater 
    })

    //Maiores de 18 em ordem de idade ascendente

    let usuario06 = await User.find({
        age: {$gt: 18}
    }).sort( {age: 1}) //-1 é descendente

    //Maiores que 18 em ordemo pelo firstname
    let usuario07 = await User.find({
        age: {$gt:18}
    }).sort({ 'name.firstname': 1, 'name.lastname': 1})

    //limitando os usuários
    let usuario08 = await User.find({
        age: {$gt: 18}
    }).limit(2)

    //Limitando os usuários e pulando dados
    let usuario09 = await User.find({
        age: {$gt: 18}
    }).skip(2).limit(2)

    console.log(usuario09)

    //~criando um novo usuário método 1 - TESTADO
    let newUser = await User.create({
        name: {firstName: 'Monaliza', lastName: 'Fernandes'},
        email: 'mono@paris.org',
        age: 200,
        interests: ['arte', 'pizza']
    })
    await newUser.save()

    //Criando usuário com o método 2
    let newUser02 = new User()
    newUser02.name = { firstName: 'André', lastName: 'Soares'}
    newUser02.email = 'andre@hotmail.com'
    newUser02.age = 25
    newUser02.interests = ['programação', 'skate']
    let resultado = await newUser02.save()

    console.log(resultado)

    //Atualizar vários dados
    await User.updateMany(
        {age: {$lt: 18} }, //parametros
        {age: 18} //novo valor
    )

    //Atualizar vários de uma pessoa só
    await User.updateMany(
        {email: 'Carlito31@gmail.com' }, //parametros
        {age: 105} //novo valor
    )

    //Atualizar vários de uma pessoa só
    let fulana = await User.findOne({ email: 'fulana@hotmail.com.br'})
    if(fulana) {
        fulana.name.firstName = 'Fulana'
        fulana.name.lastName = 'Tal'
        fulana.age = 40
        await fulana.save()
    }

    //~Atualizar vários dados de uma pessoa só - Método 02: TESTADO
    let fulanaM2 = await User.findOne({ email: 'fulana@hotmail.com.br'})
    if(fulanaM2) {
        await User.updateOne(
            {email: 'fulana@hotmail.com.br'},
            {
                $set: {
                    'name.firstName': 'Fulana',
                    'name.lastName' : 'Tal',
                    'age': 40
                }
            }
        )
        //...Código...
    }
    
    //Deletando dados do mondoDB
    await User.findOneAndDelete({ email: 'mono@paris.org'})

    //Deletando dados do mondoDB
    let Paulo = await User.findOne({email: 'andre@hotmail.com'})
    if(Paulo) Paulo.remove()
    



    
    //------------------------------------

    let age: number = 90;
    let showOld: boolean = false;

    if(age > 50) {
        showOld = true;
    }

    let list = Product.getAll();
    let expensiveList = Product.getFromPriceAfter(12);

    res.render('pages/home', {
        name: 'Bonieky',
        lastName: 'Lacerda',
        showOld,
        products: list,
        expensives: expensiveList,
        frasesDoDia: []
    });
};

export const exercicio04 =async (req:Request, resp: Response) => {
    const usuario = await User.find({})

    resp.render('pages/exercicioM4', {
     usuario
    })
}

export const exercicioM4_req =async (req:Request, resp: Response) => {
    let nome: string = req.body.nome as string
    let sobrenome: string = req.body.sobrenome as string
    let email: string = req.body.email as string
    let idade: number = Number(req.body.idade as string)
    let interesses: string[] = (req.body.interesses as string).split(' ')


    let user = new User()
    user.name = {
        firstName: nome,
        lastName: sobrenome
    }
    user.email = email
    user.age = idade
    user.interests = interesses
    await user.save()


    resp.redirect('/exercicio04')
    
}

export const exAddIdade =async (req:Request, resp: Response) => {
    let id: string = req.params.id as string
    
    let user = await User.findOne({_id: id})
    if(user) {
        user.age ++
        user.save()
    }


    resp.redirect('/exercicio04')
}