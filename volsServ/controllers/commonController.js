const {conn} = require('../mySQLconnection')

module.exports.sendJSONResponse = (res, status, content=null) => {
    res.status(status).json(content);
}

module.exports.runSQLAndSend = (sql, res) => {
    conn.query(sql, (err, result) => {
        if (err) {
            console.log(err)
            return this.sendJSONResponse(res, 500)
        }
        this.sendJSONResponse(res, 200, result)
    })
}

module.exports.runSQLDontSend = (sql, res) => {
    conn.query(sql, err => {
        if (err) {
            console.log(err)
            return this.sendJSONResponse(res, 500)
        }
        this.sendJSONResponse(res, 200)
    })
}

module.exports.addVolunteerInEvent = (req, res) => {
    let insert_data = req.body
    let sql = `INSERT INTO 
        volunteer_in_event
    VALUES (
        "${insert_data.volunteer_id}",
        "${insert_data.event_id}"`
    this.runSQLDontSend(sql, res)
}

module.exports.avgLevel = (sql, res) => {
    conn.query(sql, (err, result) => {
        if (err) {
            console.log(err)
            return this.sendJSONResponse(res, 500)
        }
        result = result[0]
        let sql = `SELECT 
            level.level_name
        FROM
            level
        WHERE
            level.level_id = ${Math.round(result.levels_sum / result.levels_total)}`

        this.runSQLAndSend(sql, res)
    })
}