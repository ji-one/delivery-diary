const mysql = require('mysql');
const { init } = require('../app');

const dbInfo = {
  host:'localhost'
  ,user:'root'
  ,password:'*a1s2d3f4g5'
  ,database:'board'
}

let dbcon = {
	init:function() {
		return mysql.createConnection(dbInfo);
	},
	conn:function(con) {
		con.connect(function(err){
			if(err) {
				console.log("mysql connection error :"+err);
				setTimeout(function(){init()}, 2000);

			} else {
				console.log("mysql connection sucessfully");
			}
		})
	}
}

module.exports = dbcon; //모듈 등록