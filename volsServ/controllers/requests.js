const {runSQLAndSend, runSQLDontSend} = require('./commonController')

module.exports.getAll = (req, res) => {
    let sql = `SELECT
        request.request_id,
        request.request_event_name,
        request.request_event_date,
        employee.emp_name,
        organization.org_name,
        center.center_name,
        level.level_name
    FROM
        request,
        employee,
        center,
        level,
        organization
    WHERE
        request.manager_id = employee.emp_id 
        AND request.organization_id = organization.organization_id 
        AND request.center_id = center.center_id 
        AND request.level_id = level.level_id`

    runSQLAndSend(sql, res)
}

module.exports.insert = (req, res) => {
    let insert_data = req.body
    console.log(insert_data)
    let sql = `INSERT INTO request(
        request_event_name,
        request_event_date,
        manager_id,
        organization_id,
        center_id,
        level_id
    )
    VALUES(
        "${insert_data.request_event_name}",
        "${insert_data.request_event_date}",
        "${insert_data.request_manager}",
        "${insert_data.request_organization}",
        "${insert_data.request_center}",
        "${insert_data.request_level}"
    )`

    runSQLDontSend(sql, res)
}

module.exports.update = (req, res) => {
    let update_data = req.body
    console.log(update_data)
    let sql = `UPDATE
    request
    SET
        request_event_name = "${update_data.request_event_name}",
        request_event_date = "${update_data.request_event_date}",
        manager_id = "${update_data.request_manager}",
        organization_id = "${update_data.request_organization}",
        center_id = "${update_data.request_center}",
        level_id = "${update_data.request_level}"
    WHERE
        request.request_id = ${req.params['id']}`

    runSQLDontSend(sql, res)
}

module.exports.delete = (req, res) => {
    let sql = `DELETE FROM 
        request 
    WHERE 
        request.request_id = ${req.params['id']}`

    runSQLDontSend(sql, res)
}

module.exports.getData = (req, res) => {
    let sql = `SELECT
        request.request_id,
        request.request_event_name,
        request.request_event_date,
        employee.emp_name,
        organization.org_name,
        center.center_name,
        level.level_name
    FROM
        request,
        employee,
        center,
        level,
        organization
    WHERE
        request.manager_id = employee.emp_id 
        AND request.organization_id = organization.organization_id 
        AND request.center_id = center.center_id 
        AND request.level_id = level.level_id
        AND request.request_id = ${req.params['id']}`

    runSQLAndSend(sql, res)
}