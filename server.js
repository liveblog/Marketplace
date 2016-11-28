var connect = require('connect');
var serveStatic = require('serve-static');

var app = connect();
app.use(serveStatic("./client"));
app.listen(5500);
