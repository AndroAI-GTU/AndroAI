import { Body, Controller, HttpStatus, Post, Req, Res } from '@nestjs/common';
import { UserService } from './user.service';
import { Response } from 'express';
import { FileSystemStoredFile, FormDataRequest, MemoryStoredFile } from 'nestjs-form-data';
import { UserFormDataDto } from './dto/user-formdata.dto';
import * as fs from 'fs';
import * as path from 'path';
import axios from 'axios';
import { Logger } from '@nestjs/common'


@Controller('user')
export class UserController 
{
    constructor(private readonly userService: UserService) {}

    private readonly logger = new Logger(UserController.name);
    
    @Post('create-app')
    async postQuery(@Body() body: any, @Res() response: Response) 
    {
        this.logger.log(`Received app creation request with data: ${JSON.stringify(body)}`);

        try 
        {
            const prompt = this.userService.promptGenerator(body);

            const gptResponse = await this.userService.callGPTAPI(prompt);

            /* Save the response from GPT as genProjectStructure.py */
            const userId = body.userId;
            this.logger.log(`Received User ID: ${userId}`);

            const baseDir = '/volumes/files_to_compile';
            const userDir = path.join(baseDir, userId);

            if (!fs.existsSync(userDir)) 
            {
                this.logger.log(`Creating directory: ${userDir}`);
                fs.mkdirSync(userDir, { recursive: true });
            }
            const promptFilePath = path.join(userDir, 'prompt.txt');

            fs.writeFileSync(promptFilePath, prompt);
            this.logger.log(`Prompt successfully written to: ${promptFilePath}`);

            const userSourceCodeFolder = path.join(`/volumes/files_to_compile/${userId}`);
            const srcPath = path.join(userSourceCodeFolder, 'genProjectStructure.py');

            if (!fs.existsSync(userSourceCodeFolder)) 
            {
                this.logger.log(`Creating directory: ${userSourceCodeFolder}`);
                fs.mkdirSync(userSourceCodeFolder, { recursive: true });
            }

            /* Write GPT response to file */
            try 
            {
                fs.writeFileSync(srcPath, gptResponse);
                this.logger.log(`File successfully created: ${srcPath}`);
            } 

            catch (error) 
            {
                this.logger.error(`Error writing to file ${srcPath}: ${error.message}`);
                throw error;
            }

            /* Verify if the file has been created */
            if (fs.existsSync(srcPath)) 
            {
                this.logger.log(`File successfully created and verified: ${srcPath}`);
            } 

            else 
            {
                this.logger.error(`File verification failed: ${srcPath} does not exist.`);
                throw new Error(`File creation failed for ${srcPath}`);
            }

            /*________________________________________________________________________________
            |                                                                                 |
            |   Send a POST request to Android Builder:                                       |
            |                                                                                 |
            | - as a result of this request the android-builder service will run generate.py  |
            | - then the android project created by this file will be compiled.               |
            _________________________________________________________________________________*/

            const androidBuilderUrl = 'http://android-builder:5500/build';
            const dstPath = path.join(`/volumes/apk_files/${userId}`);

            this.logger.log(`Sending POST request to ${androidBuilderUrl} with src_path: ${srcPath} and dst_path: ${dstPath}`);

            if (!fs.existsSync(srcPath)) 
            {
                throw new Error(`Source file ${srcPath} not found before making a request to Android Builder.`);
            }

            try
            {
                const buildResponse = await axios.post(
                    androidBuilderUrl, 
                    {
                        src_path: srcPath,
                        dst_path: dstPath,
                        user_id: userId
                    },
                    {
                        timeout: 30000
                    }
                );       
                this.logger.log(`Build response: ${JSON.stringify(buildResponse.data)}`);       
            }

            catch (error) 
            {
                this.logger.error(`Axios request failed: ${error.message}`, error.response ? error.response.data : error.stack);
                throw error;
            }

            /* return apk's path */
            return response.status(HttpStatus.OK).json(
            {
                message: 'App created successfully',
                apkPath: path.join(dstPath, 'app-debug.apk')
            });
        } 

        catch (error) 
        {
            this.logger.error(`Error processing app creation request: ${error.message}`, error.stack);

            return response
                .status(HttpStatus.INTERNAL_SERVER_ERROR)
                .json({ error: error.message });
        }
    }
}
