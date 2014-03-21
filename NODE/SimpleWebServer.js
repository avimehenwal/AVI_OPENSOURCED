var http = require('http');

http.createServer(function (request, response) {
	console.log('in CreateServer EventLoop');
	response.writeHead(200, {'Çontent-Type': 'text/plain'});
	response.end('Hello World\n');
 }).listen(8123);

console.log('Server running at http://127.0.0.1:8123');
