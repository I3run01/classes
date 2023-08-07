import { unlink } from 'fs/promises';
import {Request, Response} from 'express'
import sequelize, { Sequelize } from 'sequelize';
import { Op, where } from "sequelize";
import sharp, { Sharp } from 'sharp';

import { Phrase } from '../models/phrase'

export const ping = (req: Request, res: Response) => {
    res.json({pong: true})
}

export const random = (req: Request, res: Response) => {
    let nRand: number = Math.floor( Math.random()*10)
    res.json({number: nRand})
}

export const nome = (req: Request, res: Response) => {
    let nome: string = req.params.nome
    res.json({nome: 'Você enviou o nome ' + nome})
}

export const createPhrase = async (req: Request, res: Response) => {
    let {authorV, txtV} = req.body
    let author = authorV
    let txt = txtV

    let newPhrase = await Phrase.create({ author, txt})

    res.status(201) //retorno para o usuário
    res.json({id: newPhrase.id, author, txt})


}

export const listPhrases = async (req:Request, res: Response) => {
    let list = await Phrase.findAll()

    res.json({list})
}

export const getPhrase =async (req:Request, res: Response) => {
    let { id } = req.params

    let phrase = await Phrase.findByPk(id)
    if(phrase) res.json({phrase})
    else res.json({error:  'Frase não encontrada'})

}

export const updatePhrase =async (req:Request, res: Response) => {
    let { id } = req.params
    let {authorValue, txtValue } = req.body

    
    let phrase = await Phrase.findByPk(id)

    
    if(phrase) {
        phrase.author = authorValue
        phrase.txt = txtValue
        await phrase.save()

        res.json({phrase})

    } else res.json({error: 'Frase não encontrada'}) 
}

export const deletePhrase =async (req:Request, res:Response) => {
    let { id } = req.params

    await Phrase.destroy({where: {id}})
    res.json({})
}

export const randomPhrase = async (req:Request, res:Response) => {
    let phrase = await Phrase.findOne({
        order: [
            Sequelize.fn('RAND')
        ]
    })

    if(phrase) res.json({phrase})
    else res.json({error: 'Não há frases para serem encontradas'})
}

export const uploadFile00 =async (req:Request, res: Response) => {
    //receber o arquivo 
    // req.file ou req.files

    const files = req.files as { 
        avatar: Express.Multer.File[],
        gallary: Express.Multer.File[]
    }

    console.log( 'AVATR',files.avatar)
    console.log('GALLARY', files.gallary)
    
    res.json({})
}

export const uploadFile =async (req:Request, res: Response) => {

    
    if ( req.file ) {
        const filename = `${req.file.filename}`

        await sharp(req.file.path) //pega o arquivo
            .resize(600, 400) //largura //altura
            .toFormat('jpeg') //formato
            .toFile(`./public/media/${filename}`) //local correto

        await unlink( req.file.path )


    
        res.json({ image: `${filename}`})

    } else {
        res.status(400)
        res.json({error: 'Arquivo inválido'})

    }
}

