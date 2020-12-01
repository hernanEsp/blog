from flask import Flask, render_template, redirect, request, url_for, session
from flask_mysqldb import MySQL, MySQLdb
import bcrypt

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'blogdb'
mysql = MySQL(app)

@app.route('/')
def layout():
    return render_template('home.html')

@app.route('/register', methods=["GET", "POST"])
def register():
	if request.method == 'GET':
		return render_template("register.html")
	else: 
		name = request.form['name']
		email = request.form['email']
		password = request.form['password']
		pass_hase = password.encode()
		sal = bcrypt.gensalt()
		hash_password = bcrypt.hashpw(pass_hase, sal)

		cur = mysql.connection.cursor()
		cur.execute("INSERT INTO users (name,email,password) VALUES (%s,%s,%s), (name,email,hash_password)")
		mysql.connection.commit()
		session['name'] = name
		session['email'] = email
		return redirect(url_for("home"))	

if __name__ == '__main__':
    app.run(debug=True)