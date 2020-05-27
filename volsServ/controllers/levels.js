const { runSQLAndSend, runSQLDontSend} = require('./commonController')

module.exports.getAll = (req, res) => {
    let sql = `SELECT * FROM level`
    runSQLAndSend(sql, res)
}

module.exports.getData = (req, res) => {
    let sql = `SELECT 
        level_name
    FROM
        level
    WHERE
        level_id = ${req.params['id']}`

    runSQLAndSend(sql, res)

}

module.exports.insert = (req, res) => {
    let sql = `INSERT INTO 
        level (level_name)
    VALUES 
        ("${req.body.level_name}")`

    runSQLDontSend(sql, res)
}

module.exports.update = (req, res) => {
    let sql = `UPDATE
        level
    SET
        level_name = "${req.body.level_name}"
    WHERE
        level.level_id = ${req.params['id']}`

    runSQLDontSend(sql, res)
}

module.exports.delete = (req, res) => {
    let sql = `DELETE FROM
        level
    WHERE
        level.level_id = ${req.params['id']}`

    runSQLDontSend(sql, res)
}