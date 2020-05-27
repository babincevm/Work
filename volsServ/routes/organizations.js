const express = require('express');
const router = express.Router();
const orgCtrl = require('../controllers/organizations')

router.use((req, res, next) => {
    console.log(`route: ${req.originalUrl}; method: ${req.method}` );
    next();
})

router.get('/all', orgCtrl.getAll)
router.get('/names/all', orgCtrl.getAllNames)
router.get('/:id/name', orgCtrl.getName)
router.get('/:id', orgCtrl.getData)
router.get('/:id/events', orgCtrl.getEvents)
router.get('/:id/events/counted', orgCtrl.getCountedEvents)
router.post('/', orgCtrl.insert)
router.put('/:id', orgCtrl.update)
router.delete('/:id', orgCtrl.delete)

module.exports = router