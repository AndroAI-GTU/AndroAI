import { Body, Controller, HttpStatus, Post, Req, Res } from '@nestjs/common';
import { UserService } from './user.service';
import { Response } from 'express';

@Controller('user')
export class UserController {
    constructor(private readonly userService: UserService) {}
    
    /*
    example front:
    <form id="upload-form">
        <input type="text" name="feat1" placeholder="Feature 1" />
        <input type="text" name="feat2" placeholder="Feature 2" />
        <input type="text" name="feat3" placeholder="Feature 3" />
        <input type="text" name="feat4" placeholder="Feature 4" />
        <input type="text" name="feat5" placeholder="Feature 5" />
        <button type="submit" onclick="fetchApi(event)">Upload</button>
      </form>
    <script> 
        async function fetchApi(event) {
            event.preventDefault();
            const form = document.getElementById('upload-form');
            try {
                const data = {
                    feat1: form.elements.feat1.value,
                    feat2: form.elements.feat2.value,
                    feat3: form.elements.feat3.value,
                    feat4: form.elements.feat4.value,
                    feat5: form.elements.feat5.value,
                }
                const res = await fetch("http://localhost:5000/user/query", {
                    method: "POST",
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(data),
                });

                if (!res.ok) {
                    throw new Error(`HTTP error! status: ${res.status}`);
                }

                const openRes = await res.json();
                console.log(openRes);
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        }
    </script>
    */
    @Post('query')
    postQuery(
        @Body() body: any, 
        @Res() response: Response): void{
        console.log(body);
        response.status(HttpStatus.CREATED).json({Result: "Done with " + body.feat1 + " " + body.feat2 + " " + body.feat3 + " " + body.feat4 + " " + body.feat5 + "."});
    } 
}
