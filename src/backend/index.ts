import express from 'express'
const app = express()

const PORT = 8080

app.get('/api', (req, res) => {
    res.send('Hello from Custard! 🍮')
})

app.listen(PORT, () => {
    console.log(`Example app listening on port ${PORT}`)
})