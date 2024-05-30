const express = require('express');
const bodyParser = require('body-parser');

const app = express();
const port = 3000;

app.use(bodyParser.json());

app.post('/average', (req, res) => {
    const numbers = req.body.numbers;

    if (!numbers || !Array.isArray(numbers) || numbers.length === 0) {
        return res.status(400).json({ error: 'Invalid input. Please provide an array of numbers.' });
    }

    const sum = numbers.reduce((acc, num) => acc + num, 0);
    const average = sum / numbers.length;

    res.json({ average });
});

app.listen(port, () => {
    console.log(`Average calculator microservice listening at http://localhost:${port}`);
});
