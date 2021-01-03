var fs = require('fs');
var http = require('http');
var express = require('express');
var app = express();

app.set('view engine', 'ejs');

app.use(express.static(__dirname));

app.get('/', function(req, res) {
  res.sendFile(__dirname + "/index.html")
});

app.get('/blog', function(req, res) {
  res.sendFile(__dirname + "/blog.html")
});

app.get('/category', function(req, res) {
  res.sendFile(__dirname + "/category.html")
});

app.listen(3000, '127.0.0.1');
console.log("Порт 3000 работает...")
