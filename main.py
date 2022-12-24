from flask import *
import sqlite3,os
import datetime

con=sqlite3.connect("keytext")
con.execute("CREATE TABLE IF NOT EXISTS main(date INTEGER, name TEXT, data TEXT)")
con.close()
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def new():
    dd = datetime.datetime.now().strftime("%c")
    if request.method=='POST':
        name=request.form['author']
        data=request.form['data']
        with sqlite3.connect("keytext") as con:
            cur=con.cursor()
            cur.execute("INSERT INTO main (date, name, data) VALUES (?,?,?)",(dd,name,data))
            con.commit()
    return render_template('new.html')

@app.route('/all')
def all():
    con = sqlite3.connect("keytext")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from main")
    rows = cur.fetchall()
    return render_template("all.html",rows=rows)

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
