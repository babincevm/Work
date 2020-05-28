const {conn} = require('../mySQLconnection')
const {sendJSONResponse, runSQLAndSend, runSQLDontSend, addVolunteerInEvent} = require('./commonController')


module.exports.getAll = (req, res) => {
    let sql = `SELECT
        volunteer.volunteer_id,
        employee.emp_name,
        employee.emp_phone,
        employee.emp_email,
        employee.emp_bdate,
        employee.emp_gender,
        center.center_name
    FROM
        volunteer
    LEFT JOIN employee ON volunteer.volunteer_id = employee.emp_id
    LEFT JOIN center ON employee.center_id = center.center_id`

    runSQLAndSend(sql, res)
}

module.exports.getName = (req, res) => {
    let sql = `SELECT emp_name FROM employee WHERE emp_id = ${req.params['id']}`
    runSQLAndSend(sql, res)
}

module.exports.getData = (req, res) => {
    let sql = `SELECT
        volunteer.volunteer_id,
        employee.emp_name,
        employee.emp_phone,
        employee.emp_email,
        employee.emp_bdate,
        employee.emp_gender,
        center.center_name
    FROM
        volunteer
    LEFT JOIN employee ON volunteer.volunteer_id = employee.emp_id
    LEFT JOIN center ON employee.center_id = center.center_id
    WHERE
        employee.emp_id = ${req.params['id']}`

    runSQLAndSend(sql, res)
}

module.exports.insert = (req, res) => {
    let insert_data = req.body
    // Запись в таблицу EMPLOYEE
    let sql = `INSERT INTO 
    employee 
    (emp_name, emp_phone, emp_email, emp_bdate, emp_gender, center_id) 
    VALUES (
        "${insert_data.vol_name}", 
        "${insert_data.vol_phone}", 
        "${insert_data.vol_email}", 
        "${insert_data.vol_bdate}", 
        "${insert_data.vol_gender}",
        "${insert_data.vol_center}"
    )`
    conn.query(sql, (err, result) => {
        if (err) {
            console.log(err)
            return sendJSONResponse(res, 500)
        }
        // Запись emp_id, полученного при записи в таблицу employee,
        // в таблицу volunteer
        conn.query(`INSERT INTO 
            volunteer (volunteer_id) 
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
        emp_name = "${update_data.vol_name}",
        emp_phone = "${update_data.vol_phone}",
        emp_email = "${update_data.vol_email}",
        emp_bdate = "${update_data.vol_bdate}",
        emp_gender = "${update_data.vol_gender}",
        center_id = "${update_data.vol_center}"
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

module.exports.getEvents = (req, res) => {
    let sql = `SELECT
        event.event_id,
        event.event_name
    FROM
        volunteer_in_event,
        event
    WHERE
        event.event_id = volunteer_in_event.event_id AND volunteer_in_event.volunteer_id = ${req.params['id']}`

    runSQLAndSend(sql, res)
}

module.exports.totalEvents = (req, res) => {
    let sql = `SELECT
    COUNT(event.event_id) AS counted_events
    FROM
    volunteer_in_event,
        event
    WHERE
    event.event_id = volunteer_in_event.event_id AND volunteer_in_event.volunteer_id = ${req.params['id']}`

    runSQLAndSend(sql, res)
}

module.exports.addEvent = (req, res) => {
    addVolunteerInEvent(req, res)
}

module.exports.getAllNames = (req, res) => {
    let sql = `SELECT
        volunteer.volunteer_id,
        employee.emp_name
    FROM
        volunteer, employee
    WHERE 
        volunteer.volunteer_id = employee.emp_id`
    runSQLAndSend(sql, res)
}

module.exports.avgLevel = (req, res) => {
    let sql = `SELECT
        SUM(event.level_id) AS levels_sum,
        COUNT(event.level_id) AS levels_total
    FROM
        volunteer_in_event,
        event
    WHERE
        event.event_id = volunteer_in_event.event_id AND volunteer_in_event.volunteer_id = ${req.params['id']}`

    conn.query(sql, (err, result) => {
        if (err) {
            console.log(err)
            return sendJSONResponse(res, 500)
        }
        result = result[0]
        let sql = `SELECT 
            level.level_name
        FROM
            level
        WHERE
            level.level_id = ${Math.floor(result.levels_sum / result.levels_total)}`

        runSQLAndSend(sql, res)
    })
}