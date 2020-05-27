const express = require('express');
const router = express.Router();
const volCtrl = require('../controllers/volunteers')

router.use((req, res, next) => {
    console.log(`route: ${req.originalUrl}; method: ${req.method}`);
    next();
})

router.get('/all', volCtrl.getAll)
router.get('/:id/name', volCtrl.getName)
router.get('/:id/events', volCtrl.getEvents)
router.get('/:id', volCtrl.getData)
router.get('/all/names', volCtrl.getAllNames)
router.get('/:id/events/count', volCtrl.totalEvents)
router.post('', volCtrl.insert)
router.put('/:id', volCtrl.update)
router.delete('/:id', volCtrl.delete)


module.exports = router;
