const express = require('express');
const router = express.Router();
const reqCtrl = require('../controllers/requests')

router.use((req, res, next) => {
    console.log(`route: ${req.originalUrl}; method: ${req.method}` );
    next();
})

router.get('/all', reqCtrl.getAll)
router.get('/:id', reqCtrl.getData)
router.post('/', reqCtrl.insert)
router.put('/:id', reqCtrl.update)
router.delete('/:id', reqCtrl.delete)

module.exports = router