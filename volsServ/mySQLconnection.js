const mysql = require('mysql2')
const db_options = {
    'host': process.env.DB_HOST,
    'user': process.env.DB_USER,
    'database': process.env.DB_DATABASE,
    'password': process.env.DB_PASSWORD,
    'port': process.env.DB_PORT
}

const conn = mysql.createConnection(db_options)

conn.connect( err => {
    if (err) {
        console.log(err.message)
        return process.exit(1)
    }
    console.log('DB connected successfully')
})

module.exports = {conn}
