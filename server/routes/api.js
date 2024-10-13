const express = require("express");
const { processRequest } = require("../controller/process");
const router = express.Router();

router.post("/process", processRequest);

module.exports = router;
