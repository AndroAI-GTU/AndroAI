import { Body, Controller, HttpStatus, Post, Req, Res } from '@nestjs/common';
import { UserService } from './user.service';
import { Response } from 'express';
import { FileSystemStoredFile, FormDataRequest, MemoryStoredFile } from 'nestjs-form-data';
import { UserFormDataDto } from './dto/user-formdata.dto';

@Controller('user')
export class UserController {
    constructor(private readonly userService: UserService) {}
    
    @Post('query')
    @FormDataRequest()
    postQuery(
        @Body() body: UserFormDataDto, 
        @Res() response: Response): void{
        response.status(HttpStatus.CREATED).json({
            FormDataReceived: body,
            FileLocation: body.appIcon.path.toString(),
        });
    } 
}
