import { Injectable } from '@nestjs/common';
import { UserFormDataDto } from './dto/user-formdata.dto';
import axios from 'axios';

/* Prompt file will be created here */

@Injectable()
export class UserService 
{
	promptGenerator(body: UserFormDataDto): string 
	{
	    /* Here we will do the necessary operations using the 'body' parameter. */
	    const appName = body.appName || 'DefaultApp';
	    return `Generated prompt with app name: ${appName}`;
	} 
	/* --------> 
		build here using similar logic to promptGenerator.py 
		in the outermost directory.
	*/

	async callGPTAPI(prompt: string): Promise<string> 
	{
    	const apiKey = process.env.OPENAI_API_KEY; /* Get the API key from the .env file */

    	console.log("API Key is loaded: ", apiKey ? "Yes" : "No");

    	try
    	{
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

    	catch (error)
    	{
    		console.error("Error in GPT API call:", error.response ? error.response.data : error.message);
    		throw new Error("GPT API call failed");
    	}
  	}
}
