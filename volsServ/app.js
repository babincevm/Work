require('dotenv').config()
const express = require('express');

const app = express();
app.use(express.json());

app.use((req, res, next) => {
    res.header('Access-Control-Allow-Origin', '*');
    res.header('Access-Control-Allow-Methods', '*');
    res.header('Access-Control-Allow-Headers', '*');
    next();
});

const port = process.env.PORT || 5000
const host = process.env.HOST || 'localhost'

app.use('/center', require('./routes/centers'))
app.use('/volunteer', require('./routes/volunteers'))
app.use('/organization', require('./routes/organizations'));
app.use('/event', require('./routes/events'));
app.use('/request', require('./routes/requests'))
app.use('/level', require('./routes/levels'))
app.use('/request', require('./routes/requests'))
app.use('/manager', require('./routes/manager'))

// 404 handler
app.use((req, res) => {
    console.log(404)
    res.status(404).send('Wrong path');
});

app.listen(port, host, () => {
    console.log(`Server started at http://${host}:${port}`)
})


