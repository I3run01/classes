import { Controller } from '@nestjs/common';
import { MessagePattern, Payload, EventPattern } from '@nestjs/microservices';
import { CreateUserDto } from './dto/create-user.dto';
import { UsersService } from './users.service';
import { hash } from 'bcrypt';
import { User } from './entities/user.entity';

@Controller()
export class UsersController {
  constructor(
    private readonly usersService: UsersService,
  ) {}

  @EventPattern('hello.world')
  async handleHelloWorldMessage(@Payload() data: string) {
    console.log(`Received message: ${data}`);
  }

  @MessagePattern({ cmd: 'sum' })
  async accumulate(@Payload() data: number[]): Promise<number> {

    let value = (data || []).reduce((a, b) => a + b)
    console.log(value)  
    return value
  }

  @MessagePattern('createUser')
  async createUser(@Payload() data: {email: string, password: string}): Promise<User> {

    let token = String(await hash(data.email, 10))
    let hashedPassword = String(await hash(data.password, 10))

    const userDTO: CreateUserDto = {
      taskOne: {
        email: data.email,
        password: hashedPassword,
        token: token,
      },
      taskThree: {
        id: null,
        imageRouter: null,
        hash: null,
        imageCode64: null,
      },
    };
    return await this.usersService.create(userDTO);
  }
}
