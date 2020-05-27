const express = require('express');
const router = express.Router();
const centerCtrl = require('../controllers/center')

router.use((req, res, next) => {
    console.log(`route: ${req.originalUrl}; method: ${req.method}` );
    next();
})

router.get('/all', centerCtrl.getAll)
router.get('/all/names', centerCtrl.getAllNames)
router.get('/:id/name', centerCtrl.getName)
router.get('/:id', centerCtrl.getData)
router.get('/:id/volunteers', centerCtrl.getVolunteers)
router.get('/:id/organizations', centerCtrl.getOrganizations)
router.get('/:id/events', centerCtrl.getEvents)
router.get('/:id/volunteers/total', centerCtrl.getVolunteersTotal)
router.get('/:id/organizations/total', centerCtrl.getOrganizationsTotal)
router.get('/:id/events/total', centerCtrl.getEventsTotal)
router.post('/', centerCtrl.insert)
router.put('/:id', centerCtrl.update)
router.delete('/:id', centerCtrl.delete)

module.exports = router