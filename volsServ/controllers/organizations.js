const {runSQLAndSend, runSQLDontSend, runDupKeysSQL} = require('./commonController')

module.exports.getAll = (req, res) => {
    let sql = `SELECT 
        organization.organization_id, 
        organization.org_name, 
        organization.org_email
    FROM 
        organization`
    runSQLAndSend(sql, res)
}

module.exports.getName = (req, res) => {
    let sql = `SELECT
        organization.org_name
    FROM
        organization
    WHERE
        organization.organization_id = ${req.params['id']}`

    runSQLAndSend(sql, res)
}

module.exports.getData = (req, res) => {
    let sql = `SELECT
        *
    FROM
        organization
    WHERE
        organization.organization_id = ${req.params['id']}`

    runSQLAndSend(sql, res)
}

module.exports.getAllNames = (req, res) => {
    let sql = `SELECT 
        organization.organization_id, organization.org_name
    FROM 
        organization;`
    runSQLAndSend(sql ,res)
}

module.exports.getEvents = (req, res) => {
    let sql = `SELECT 
        event.event_id,
        event.event_name
    FROM
        event
    WHERE
         event.organization_id = ${req.params['id']}`

    runSQLAndSend(sql, res)
}

module.exports.insert = (req, res) => {
    let insert_data = req.body
    let sql = `INSERT INTO 
        organization 
        (org_name, org_email)
    VALUES
    (
        "${insert_data.org_name}", 
        "${insert_data.org_email}"
    )`

    runSQLDontSend(sql, res)
}

module.exports.update = (req, res) => {
    let update_data = req.body
    let sql = `UPDATE
        organization
    SET
        org_name = "${update_data.org_name}",
        org_email = "${update_data.org_email}"
    WHERE
        organization.organization_id = ${req.params['id']}`

    runSQLDontSend(sql, res)
}

module.exports.delete = (req, res) => {
    let sql = `DELETE
    FROM
        organization
    WHERE
        organization.organization_id = ${req.params['id']}`

    runSQLDontSend(sql, res)
}

module.exports.getCountedEvents = (req, res) => {
    let sql = `SELECT 
        COUNT (event.event_name) AS counted_events
    FROM
        event
    WHERE
         event.organization_id = ${req.params['id']}`

    runSQLAndSend(sql, res)
}