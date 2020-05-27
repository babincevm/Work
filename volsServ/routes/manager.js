const express = require('express');
const router = express.Router();
const managerCtrl = require('../controllers/managers')

router.use((req, res, next) => {
    console.log(`route: ${req.originalUrl}; method: ${req.method}` );
    next();
})

router.delete('/vol', managerCtrl.VIEDelete)
router.get('/all', managerCtrl.getAll)
router.get('/all/names', managerCtrl.getNames)
router.get('/:id/data', managerCtrl.getData)
router.post('/', managerCtrl.insert)
router.put('/:id', managerCtrl.update)
router.delete('/:id', managerCtrl.delete)
router.post('/vol', managerCtrl.VIEInsert)
router.post('/auth', managerCtrl.auth)

module.exports = router