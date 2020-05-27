const {conn} = require('../mySQLconnection')
const {sendJSONResponse, runSQLAndSend, runSQLDontSend} = require('./commonController')

module.exports.getAll = (req, res) => {
    let sql = `SELECT
        manager.manager_id,
        employee.emp_name,
        employee.emp_phone,
        employee.emp_email,
        employee.emp_bdate,
        employee.emp_gender,
        center.center_name
    FROM
        manager
    LEFT JOIN employee ON manager.manager_id = employee.emp_id
    LEFT JOIN center ON employee.center_id = center.center_id`

    runSQLAndSend(sql, res)
}

module.exports.getNames = (req, res) => {
    let sql = `SELECT
        manager.manager_id,
        employee.emp_name
    FROM
        manager
    LEFT JOIN employee ON manager.manager_id = employee.emp_id`

    runSQLAndSend(sql, res)
}

module.exports.insert = (req, res) => {
    let insert_data = req.body
    // Запись в таблицу EMPLOYEE
    let sql = `INSERT INTO 
        employee 
        (emp_name, emp_phone, emp_email, emp_bdate, emp_gender, center_id) 
    VALUES (
        "${insert_data.manager_name}", 
        "${insert_data.manager_phone}", 
        "${insert_data.manager_email}", 
        "${insert_data.manager_bdate}", 
        "${insert_data.manager_gender}",
        "${insert_data.manager_center}"
    )`
    conn.query(sql, (err, result) => {
        if (err) {
            console.log(err)
            return sendJSONResponse(res, 500)
        }
        // Запись emp_id, полученного при записи в таблицу employee,
        // в таблицу manager
        conn.query(`INSERT INTO 
            manager (manager_id) 
        VALUES 
            ("${result['insertId']}")`, err => {
            if (err) {
                console.log(err)
                return sendJSONResponse(res, 500)
            }
            sendJSONResponse(res, 200)
        })

    })
}

module.exports.update = (req, res) => {
    let update_data = req.body
    let sql = `UPDATE
        employee
    SET
        emp_name = "${update_data.manager_name}",
        emp_phone = "${update_data.manager_phone}",
        emp_email = "${update_data.manager_email}",
        emp_bdate = "${update_data.manager_bdate}",
        emp_gender = "${update_data.manager_gender}",
        center_id = "${update_data.manager_center}"
    WHERE
        employee.emp_id = ${req.params['id']}`

    runSQLDontSend(sql, res)
}

module.exports.delete = (req, res) => {
    let sql = `DELETE FROM 
        employee 
    WHERE 
        employee.emp_id = ${req.params['id']}`

    runSQLDontSend(sql, res)
}

module.exports.getData = (req, res) => {
    let sql = `SELECT
        manager.manager_id,
        employee.emp_name,
        employee.emp_phone,
        employee.emp_email,
        employee.emp_bdate,
        employee.emp_gender,
        center.center_name
    FROM
        manager
    LEFT JOIN employee ON manager.manager_id = employee.emp_id
    LEFT JOIN center ON employee.center_id = center.center_id
    WHERE
        employee.emp_id = ${req.params['id']}`

    runSQLAndSend(sql, res)
}

module.exports.VIEInsert = (req, res) => {
    let insert_data = req.body
    let sql = `INSERT INTO
        volunteer_in_event (volunteer_id, event_id)
    VALUES
        (
        "${insert_data.volunteer_id}",
        "${insert_data.event_id}")`

    runSQLDontSend(sql, res)
}

module.exports.VIEDelete = (req, res) => {
    let delete_data = req.body

    let sql = `DELETE
    FROM
        volunteer_in_event
    WHERE
        volunteer_id = ${delete_data.volunteer_id}
    AND
        event_id = ${delete_data.event_id}`

    runSQLDontSend(sql, res)
}

module.exports.auth = (req, res) => {
    let auth = req.body
    if (auth.login === 'admin' && auth.password === 'admin') {
        return res.status(200).send(true)
    }
    res.status(409).send(false)
}