import { Body, Controller, HttpStatus, Post, Req, Res } from '@nestjs/common';
import { UserService } from './user.service';
import { Response } from 'express';
import { FileSystemStoredFile, FormDataRequest, MemoryStoredFile } from 'nestjs-form-data';
import { UserFormDataDto } from './dto/user-formdata.dto';
import * as fs from 'fs';
import * as path from 'path';
import axios from 'axios';


@Controller('user')
export class UserController 
{
    constructor(private readonly userService: UserService) {}
    
    @Post('create-app')
    async postQuery(@Body() body: any, @Res() response: Response) 
    {
        try 
        {
            const prompt = this.userService.promptGenerator(body);

            // GPT API'ye POST isteği
            const gptResponse = await this.userService.callGPTAPI(prompt);

            // GPT'den gelen yanıtı generate.py olarak kaydet
            const userId = body.userId;
            const srcPath = path.join(`/files_to_compile/${userId}`, 'generate.py');
            const dstPath = path.join(`/apk_files/${userId}`);
            
            // Dosya dizinlerini oluştur
            fs.mkdirSync(path.dirname(srcPath), { recursive: true });
            fs.writeFileSync(srcPath, gptResponse);  // GPT yanıtını dosya olarak kaydet

            // Android Builder'a POST isteği gönder
            const androidBuilderUrl = 'http://android-builder:5500/build';
            const buildResponse = await axios.post(androidBuilderUrl, 
            {
                src_path: srcPath,
                dst_path: dstPath
            });

            // APK'nın yolu dönecek
            return response.status(HttpStatus.OK).json({
                message: 'App created successfully',
                apkPath: path.join(dstPath, 'app-debug.apk')
            });

        } 

        catch (error) 
        {
            return response
                .status(HttpStatus.INTERNAL_SERVER_ERROR)
                .json({ error: error.message });
        }
    }
    // @Post('query')
    // @FormDataRequest()
    // postQuery(
    //     @Body() body: UserFormDataDto, 
    //     @Res() response: Response): Promise<void> {

    //     const prompt = this.userService.promptGenerator(body);
        
    //     /* Gpt API ına prompt kullanarak istek atılacak */

    //     /* Gpt API ından dönen veriler file olarak /files_to_compile 
    //         klasörünün içine bir numara verilerek kaydedilecek.
    //         Örneğin:
    //         /files_to_compile/{usr_id}/
    //     */
        
    //     /* Son olarak android-builder a istek atılacak.
    //         İsteğin içeriği dosya yolunu tutmalı. 
    //         Örnek komut:
    //             response = await fetch(`http://android-builder:5500/build`,{
    //                 method: "POST",
    //                 body: JSON.stringify({
    //                     path: "/files_to_compile/usr_id"
    //                 }),
    //                 headers: {
    //                     "Content-type": "application/json"
    //                 }
    //             });
    //     */

    //     /* android-builderdan apk file ın yolu geri döndülcek.
    //         Örneğin:
    //         let apk_file_path = ""
    //         if (response.ok){
    //             res = response.json();
    //             apk_file_path = res.path;
    //         }
    //     */

    //     /* apk file "apk_file_path" değişkeni kullanılarak 
    //         response olarak döndürülecek 
    //     */

    //     response.status(HttpStatus.CREATED).json({
    //         FormDataReceived: body,
    //         FileLocation: body.appIcon.path.toString(),
    //     });
    // } 
}
