import React from 'react';

import Paper from '@mui/material/Paper';
import TextField from '@mui/material/TextField';
import Box from '@mui/material/Box';
import LinearProgress from '@mui/material/LinearProgress';

// import use state
import { useState } from 'react';

// function handle submit 



export default function ChatBox() {
    const [answer, setAnswer] = useState("I am AI, I can answer your questions");

    // create a variable to store state so user cannot press enter multiple times
    const [isPending, setIsPending] = useState(false);


    async function handleSubmit(event) {
        event.preventDefault();
        console.log(event);

        const message = event.target.value;
        console.log(message);
        const API_ROOT = 'http://localhost:8000';





        // curl -X 'POST' \
        //   'http://localhost:8000/api/chat?message=xd' \
        //   -H 'accept: application/json' \
        //   -d ''
        // mode: 'no-cors',
        // method: 'POST',
        setIsPending(true);


        const response = await fetch(`${API_ROOT}/api/chat`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
            },
            body: JSON.stringify({ prompt: message })
        });
        const data = await response.json();
        console.log(data);
        setIsPending(false);
        setAnswer(data.response);



    }
    return (
        // Display paper centered in the screen with width 500px
        <Paper sx={{ width: 500, margin: 'auto', marginTop: 2, padding: 2 }}>
            <h1>ChatBox</h1>



            <form onSubmit={handleSubmit}>

                <TextField
                    id="outlined-multiline-static"
                    label="Message"
                    placeholder="Type your message here"
                    multiline
                    rows={4}
                    fullWidth
                    variant="outlined"
                    onKeyDown={(event) => {
                        // ignore keypresses if the user is holding down the shift key
                        if (event.shiftKey) {
                            return;
                        }
                        if (event.key === 'Enter' && !isPending) {
                            handleSubmit(event);
                        }
                    }}
                />
            </form>

            {/* Place for the answer, rendered conditionally  */}
            {isPending && <LinearProgress />}
            {answer && (
                <Box sx={{ bgcolor: 'grey.300', p: 2, mt: 2 }}>
                    {answer}
                </Box>
            )}




        </Paper>
    );
}