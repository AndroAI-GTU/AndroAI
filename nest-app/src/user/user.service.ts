import { Injectable } from '@nestjs/common';
import { UserFormDataDto } from './dto/user-formdata.dto';
import axios from 'axios';

/* prompt dosyası burada oluşturulacak */

@Injectable()
export class UserService 
{
	promptGenerator(body: UserFormDataDto): string 
	{
	    // Burada 'body' parametresini kullanarak gerekli işlemleri yapacağız.
	    const appName = body.appName || 'DefaultApp';
	    return `Generated prompt with app name: ${appName}`;
	}

	async callGPTAPI(prompt: string): Promise<string> 
	{
    	const apiKey = process.env.OPENAI_API_KEY; // .env dosyasından API anahtarını alıyoruz
    	const response = await axios.post(
      		'https://api.openai.com/v1/chat/completions',
      		{
        		model: 'gpt-4',
        		messages: [{ role: 'user', content: prompt }],
      		},
      		{
        		headers: {
          			Authorization: `Bearer ${apiKey}`,
          			'Content-Type': 'application/json',
        		},
      		}
    	);
    	return response.data.choices[0].message.content;
  	}
}
