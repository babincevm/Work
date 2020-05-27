const express = require('express');
const router = express.Router();
const levelCtrl = require('../controllers/levels')

router.use((req, res, next) => {
    console.log(`route: ${req.originalUrl}; method: ${req.method}` );
    next();
})

router.get('/all', levelCtrl.getAll)
router.get('/:id', levelCtrl.getData)
router.post('/', levelCtrl.insert)
router.put('/:id', levelCtrl.update)
router.delete('/:id', levelCtrl.delete)

module.exports = router