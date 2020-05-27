const express = require('express');
const router = express.Router();
const eventsCtrl = require('../controllers/events')

router.use((req, res, next) => {
    console.log(`route: ${req.originalUrl}; method: ${req.method}` );
    next();
})

router.get('/all', eventsCtrl.getAll)
router.get('/:id/name', eventsCtrl.getName)
router.get('/:id/volunteers', eventsCtrl.getVolunteers)
router.get('/:id', eventsCtrl.getData)
router.get('/:id/volunteers/counted', eventsCtrl.getCountedVolunteers)
router.get('/all/names', eventsCtrl.getAllNames)
router.post('/', eventsCtrl.insert)
router.put('/:id', eventsCtrl.update)
router.delete('/:id', eventsCtrl.delete)

module.exports = router