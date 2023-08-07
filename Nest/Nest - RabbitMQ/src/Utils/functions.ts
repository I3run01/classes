import {fromByteArray} from 'base64-js'
import * as fs from 'fs';
import {get} from 'https';
import { createTransport } from 'nodemailer';
import * as amqp from 'amqplib';

export let reqresUserRequest = async (id:string) => {  
    let response = await fetch(`https://reqres.in/api/users/${id}`)
    let json = await response.json()
  
    return json.data
}

export async function encodeImageToBase64(filePath: string): Promise<string> {
  try {
    // Read the file from the file system
    const data = await fs.promises.readFile(filePath);

    // Convert the file data to a base64 string
    const base64Data = fromByteArray(data);

    // Construct the data URL
    const mimeType = 'image/' + filePath.split('.').pop(); // Assumes the file extension determines the MIME type
    const dataUrl = `data:${mimeType};base64,${base64Data}`;

    // Return the base64 encoded string
    return dataUrl;
  } catch (error) {
    throw error;
  }
}

export async function saveImageFromUrl(url: string, filePath: string): Promise<void> {
    return new Promise<void>(async (resolve, reject) => {
        try {
            const fullURL = new URL(url)
            const localPath = fs.createWriteStream(filePath)

            const response = await new Promise<any>((resolve, reject) => {
                get(fullURL, resolve).on('error', reject)
            })

            if (response.statusCode !== 200) {
                reject(new Error(`Failed to download image: HTTP status code ${response.statusCode}`))
                return
            }

            response.pipe(localPath)

            localPath.on('finish', () => {
                localPath.close(() => {
                    resolve()
                })
            })
        } catch (error) {
            reject(error)
        }
    })
}

export function deleteImage(filename: string): void {
    try {
      // Check if the file exists
      if (fs.existsSync(filename)) {
        // Delete the file
        fs.unlinkSync(filename);
        console.log(`${filename} deleted successfully`);
      } else {
        console.log(`${filename} does not exist`);
      }
    } catch (error) {
      console.error(`Error deleting ${filename}: ${error.message}`);
    }
}

export function deleteImageFromID(id:string) {
    let imageRouter = './uploads/images/img' + id + '.jpg'
    deleteImage(imageRouter)
}

export function sendEmail(email: string, subject: string, text: string): void {
    const transporter = createTransport({
      service: 'gmail',
      auth: {
        user: 'ex3mple3mail@gmail.com',
        pass: '15151212',
      },
    });
  
    const mailOptions = {
      from: 'ex3mple3mail@gmail.com',
      to: email,
      subject: subject,
      text: text,
    };
  
    transporter.sendMail(mailOptions, (error, info) => {
      if (error) {
        console.log(error);
      } else {
        console.log('Email sent: ' + info.response);
      }
    });
}

export async function createRabbitEvent(message: string, routingKey: string): Promise<void> {
  const connection: amqp.Connection = await amqp.connect('amqp://localhost');
  const channel: amqp.Channel = await connection.createChannel();

  await channel.bindQueue('myQueue','hello.world', 'hello.world')

  channel.publish('exchangeName', routingKey, Buffer.from(message));

  console.log(`Sent RabbitMQ message with routing key "${routingKey}" and body "${message}"`);

  await channel.close();
  await connection.close();

}