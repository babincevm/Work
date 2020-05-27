const { runSQLAndSend, runSQLDontSend} = require('./commonController')

module.exports.getAll = (req, res) => {
    let sql = `SELECT 
            event.event_id, 
            event.event_name, 
            event.event_date, 
            level.level_name, 
            organization.org_name, 
            center.center_name
        FROM 
            event
        LEFT JOIN level ON event.level_id = level.level_id
        LEFT JOIN organization ON event.organization_id = organization.organization_id
        LEFT JOIN center ON event.center_id = center.center_id`

    runSQLAndSend(sql, res)
}

module.exports.getName = (req, res) => {
    let sql = `SELECT 
        event.event_name
    FROM 
        event
    WHERE 
        event.event_id = ${req.params['id']}`

    runSQLAndSend(sql, res)
}

module.exports.getData = (req, res) => {
    let sql = `SELECT
        *
    FROM
        event
    WHERE
        event.event_id = ${req.params['id']}`

    runSQLAndSend(sql, res)
}

module.exports.insert = (req, res) => {
    let insert_data = req.body
    let sql = `INSERT INTO event
    (
        event_name,
        event_date,
        level_id,
        organization_id,
        center_id
    )
    VALUES (
        "${insert_data.event_name}", 
        "${insert_data.event_date}", 
        "${insert_data.event_level}", 
        "${insert_data.event_org}", 
        "${insert_data.event_center}"
    )`

    runSQLDontSend(sql, res)
}

module.exports.update = (req, res) => {
    let update_data = req.body
    let sql =`UPDATE
        event
    SET
        event_name = "${update_data.event_name}",
        event_date = "${update_data.event_date}",
        level_id = "${update_data.event_level}",
        organization_id = "${update_data.event_org}",
        center_id = "${update_data.event_center}"
    WHERE
        event.event_id = ${req.params['id']}`

    runSQLDontSend(sql, res)
}

module.exports.delete = (req, res) => {
    let sql = `DELETE FROM 
        event 
    WHERE 
        event.event_id = ${req.params['id']}`

    runSQLDontSend(sql, res)
}

module.exports.getVolunteers = (req, res) => {
    let sql = `SELECT
    employee.emp_id,
    employee.emp_name
    FROM
        volunteer_in_event,
        employee
    WHERE
        volunteer_in_event.volunteer_id = employee.emp_id 
    AND 
        volunteer_in_event.event_id = ${req.params['id']}`

    runSQLAndSend(sql, res)
}

module.exports.getCountedVolunteers = (req, res) => {
    let sql = `SELECT
        COUNT (employee.emp_name) AS counted_volunteers
    FROM
        volunteer_in_event,
        employee
    WHERE
        volunteer_in_event.volunteer_id = employee.emp_id 
    AND 
        volunteer_in_event.event_id = ${req.params['id']}`

    runSQLAndSend(sql, res)
}

module.exports.getAllNames = (req, res) => {
    let sql = `SELECT 
            event.event_id, 
            event.event_name
        FROM 
            event`

    runSQLAndSend(sql, res)
}

