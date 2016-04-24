var express = require('express'),
	app = express(),
	server = require('http').createServer(app),
	io = require('socket.io').listen(server),
	nicknames = [];

app.use('/static', express.static(__dirname + '/public'));
var PythonShell = require('python-shell');

server.listen(3000);

app.get('/', function(req, res) {
	res.sendFile(__dirname + '/index.html');
});

io.sockets.on('connection', function(socket) {
	var pyshell = new PythonShell('../neural_network/classifier.py', 
	                           {pythonPath : 'python3', mode : 'text'});

	pyshell.on('message', function(message){
		console.log(message);
		io.sockets.emit('new message', {msg: message, nick: socket.nickname});
	});

	pyshell.on('error', function(err){
		console.log(err);
	});

	socket.on('new user', function(data, callback) {
		if (nicknames.indexOf(data) != -1) {
			callback(false);
		} else {
			callback(true);
			socket.nickname = data;
			nicknames.push(socket.nickname);
		}
	});

	socket.on('send message', function(data) {
	    var msg = data.trim();
	    if(msg !== '') {
	      pyshell.send(msg);
	    }
		//io.sockets.emit('new message', {msg: data, nick: socket.nickname});
	});

	socket.on('disconnect', function(data){
		if(!socket.nickname) return;
		nicknames.splice(nicknames.indexOf(socket.nickname), 1);
	});
});

