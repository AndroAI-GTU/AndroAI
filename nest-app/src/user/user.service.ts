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
        const generalExplaining = body.generalExplaining || 'General explanation not provided';

        /* Process the name, content and link of each activity */
	    let activityDetails = '';

	    if (body.activities && body.activities.length > 0) 
	    {
	        body.activities.forEach((activity, index) => 
	        {
	            activityDetails += `- Activity ${index + 1}: ${activity.name}\n  Content: ${activity.content}\n\n`;
	        });
	    } 

	    else 
	    {
	        activityDetails = 'No activities provided.\n\n';
	    }
	    const activityLinks = body.activities
	    	.flatMap(activity => activity.links)
  			.join(', ') || 'No links provided';

	    let activityLinksDetails = '';

	    if (Array.isArray(activityLinks) && activityLinks.length > 0) 
	    {
	        activityLinks.forEach(link => 
	        {
	            activityLinksDetails += `- ${link}\n`;
	        });
	    } 

	    else 
	    {
	        activityLinksDetails = 'No links provided.\n';
	    }

        /* prompt generating process : */
        const prompt = `
		I need you to create an Android project based on the specifications I provide. Please strictly follow these rules to ensure the project is functional and meets my requirements.
		- The top priority is that you don't write any additional message other than the Python script, so your answer to me will be just a Python script and it will be complete and error-free as follows. You need to be extremely careful with this point.
		- Also, there should be absolutely no markdown elements in your code, your answer to me should follow Python syntax. If I compile it with a Python interpreter, I should not get any syntax errors.
		
		### Rules:
		1. Do not include any additional messages or comments other than the code I request. Only write the code.
		2. Ensure all files are consistent with each other.
		3. The project must be fully functional and capable of being compiled directly via Gradle from the command line. It should not require an IDE (e.g., Android Studio) or manual adjustments.
		4. I will manually add the following files after the project structure is created:
		   - \`/gradle/wrapper/gradle-wrapper.jar\`
		   - \`/gradle/wrapper/gradle-wrapper.properties\`
		   All other files must be written by you.
		5. Ensure that the files required for a typical Android project are present and correctly configured, including but not limited to:
		   - \`build.gradle\`, \`settings.gradle\`, and \`gradle.properties\`
		   - \`AndroidManifest.xml\` for declaring the application's components
		   - XML layout files for each activity
		   - Necessary resource files such as strings, colors, and themes.

		### Project Specifications:
		- **Application Name**: The application will be named "${appName}".
		- **Package Name**: Use the package \`com.androai.${appName.toLowerCase()}\` across the entire project.
		- **Activities**: There will be ${body.activities ? body.activities.length : 0} activities in the application. Here are the details:
		${activityDetails}

		- **Activity Links**: Define the navigation between activities as:
		${activityLinksDetails}

		- **General Explanation**: ${generalExplaining}

		### Code Requirements:
		Use the following template to organize and create the project structure:

		\`\`\`python
		import os

		project_structure = {
		    "src": {
		        "androidTest": {
		            "java": {
		                "com": {
		                    "androai": {
		                        "${appName.toLowerCase()}": {
		                            "ExampleInstrumentedTest.java": ""
		                        }
		                    }
		                }
		            }
		        },
		        "main": {
		            "AndroidManifest.xml": "",
		            "java": {
		                "com": {
		                    "androai": {
		                        "${appName.toLowerCase()}": {
		                            "MainActivity.java": "",
		                            // Other activities...
		                        }
		                    }
		                }
		            },
		            "res": {
		                "layout": {
		                    "activity_main.xml": "",
		                    // Other layouts...
		                }
		            }
		        },
		        "test": {
		            "java": {
		                "com": {
		                    "androai": {
		                        "${appName.toLowerCase()}": {
		                            "ExampleUnitTest.java": ""
		                        }
		                    }
		                }
		            }
		        }
		    },
		    "build.gradle": "",
		    "settings.gradle": "",
		    "proguard-rules.pro": "",
		    "gradle.properties": ""
		}

		def create_project_structure(base_path, structure):
		    for name, content in structure.items():
		        path = os.path.join(base_path, name)
		        if isinstance(content, dict):
		            os.makedirs(path, exist_ok=True)
		            create_project_structure(path, content)
		        else:
		            with open(path, 'w') as file:
		                file.write(content)

		def main():
		    project_name = "MyAndroidApp"
		    base_path = os.path.join(os.getcwd(), project_name)
		    os.makedirs(base_path, exist_ok=True)
		    create_project_structure(base_path, project_structure)

		if __name__ == '__main__':
		    main()
		\`\`\`

		### Output Expectations:
		1. All activities, layouts, and XML configurations must be correctly specified.
		2. Files to be included:
		   - All \`.java\` files for the activities.
		   - All \`.xml\` layout files for activities.
		   - \`AndroidManifest.xml\`, \`build.gradle\`, and other required configurations.

		### Additional Notes:
		1. Clearly define activity navigation using links such as:
		   - MainActivity -> SignActivity
		   - SignActivity -> PostActivity
		2. Avoid leaving any file empty. If content is not explicitly specified, use placeholders.
		3. Ensure activity links and resource files are configured correctly in \`AndroidManifest.xml\`.
		4. I will handle adding the Gradle wrapper files (\`gradle-wrapper.jar\` and \`gradle-wrapper.properties\`) after the project structure is generated.

		When this script is executed, the output should be a directory named \`MyAndroidApp\` containing a fully functional Android project.
		`;

		return prompt;
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
	        		model: 'gpt-4-0613',
	        		messages: [
	        			{ 
	        				role: 'system', 
        					content: `You are a coding assistant. Your task is to generate code strictly according to user instructions. Do not add any explanation or additional text beyond the requested code.`
	        			},
	        			{ role: 'user', content: prompt }
	        		]
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
