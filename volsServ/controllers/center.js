const {runSQLAndSend, runSQLDontSend, runDupKeysSQL} = require('./commonController')

module.exports.getAll = (req, res) => {
    let sql = 'SELECT * FROM center'
    runSQLAndSend(sql, res)
}

module.exports.getName = (req, res) => {
    let sql = `SELECT center_name FROM center WHERE center_id = ${req.params['id']}`
    runSQLAndSend(sql, res)
}

module.exports.getAllNames = (req, res) => {
    let sql = `SELECT
        center_id,
        center_name 
    FROM 
        center`
    runSQLAndSend(sql, res)
}

module.exports.getData = (req, res) => {
    let sql = `SELECT
        *
    FROM
        center
    WHERE
        center.center_id = ${req.params['id']}`

    runSQLAndSend(sql, res)
}

module.exports.insert = (req, res) => {
    let insert_data = req.body
    let sql = `INSERT INTO 
    center (center_name, head_name, center_phone, center_address)
    VALUES 
        ("${insert_data.center_name}", 
        "${insert_data.center_head_name}", 
        "${insert_data.center_phone}", 
        "${insert_data.center_address}")`

    runSQLDontSend(sql, res)
}

module.exports.update = (req,res) => {
    let update_data = req.body
    let sql = `UPDATE
        center
    SET
        center_name = "${update_data.center_name}",
        head_name = "${update_data.center_head_name}",
        center_phone = "${update_data.center_phone}",
        center_address = "${update_data.center_address}"
    WHERE
        center.center_id = ${req.params['id']}`

    runSQLDontSend(sql, res)
}

module.exports.delete = (req, res) => {
    let sql = `DELETE FROM 
        center 
    WHERE 
        center.center_id = ${req.params['id']}`

    runSQLDontSend(sql, res)
}

module.exports.getVolunteers = (req, res) => {
    let sql = `SELECT 
        employee.emp_id,
        employee.emp_name 
    FROM 
        employee, volunteer, center 
    WHERE 
        employee.emp_id = volunteer.volunteer_id 
    AND 
        employee.center_id = center.center_id 
    AND 
        center.center_id = ${req.params['id']}`

    runSQLAndSend(sql, res)
}

module.exports.getOrganizations = (req, res) => {
    let sql = `SELECT DISTINCT
        organization.organization_id,
        organization.org_name
    FROM
        organization,
        event,
        center
    WHERE
        event.center_id = ${req.params['id']}
    AND event.organization_id = organization.organization_id`

    runSQLAndSend(sql, res)
}

module.exports.getEvents = (req, res) => {
    let sql = `SELECT
        event.event_id,
        event.event_name
    FROM
        event,
        center
    WHERE
        event.center_id = center.center_id 
    AND 
        center.center_id = ${req.params['id']}`

    runSQLAndSend(sql, res)
}

module.exports.getVolunteersTotal = (req, res) => {
    let sql = `SELECT 
        COUNT (employee.emp_id) AS volunteers_total
    FROM 
        employee, volunteer, center 
    WHERE 
        employee.emp_id = volunteer.volunteer_id 
    AND 
        employee.center_id = center.center_id 
    AND 
        center.center_id = ${req.params['id']}`

    runSQLAndSend(sql, res)
}

module.exports.getOrganizationsTotal = (req, res) => {
    let sql = `SELECT
        COUNT(*) AS organizations_total
    FROM
        (
        SELECT
            organization.organization_id
        FROM
            organization,
            event,
            center
        WHERE
            event.center_id = ${req.params['id']} AND event.organization_id = organization.organization_id
        GROUP BY
            organization.organization_id
    ) AS list_of_organizations`

    runSQLAndSend(sql, res)
}

module.exports.getEventsTotal = (req, res) => {
    let sql = `SELECT
        COUNT (event.event_id) AS events_total
    FROM
        event,
        center
    WHERE
        event.center_id = center.center_id 
    AND 
        center.center_id = ${req.params['id']}`

    runSQLAndSend(sql, res)
}


