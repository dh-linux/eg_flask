import os
from flask import Flask, session, redirect, url_for, abort, render_template, flash, request
from connMySQL import connMySQL

######################################
# use connMySQL:
#cursor = connMySQL().cursor()
#sql = "select * from entries limit 10"
#try:
#    cursor.execute(sql)
#    data = cursor.fetchall()
#    print data
#except Exception, e:
#    print e
#    sys.exit()
######################################

# static

#os.urandom(12)

app = Flask(__name__)
app.secret_key = '\x9e\xa3$\x07h^[`\x99m'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        flash("GET Successed visit!")
    else:
        flash("NOT GET!")
    return render_template('index.html')

if __name__ == '__main__':
    #app.run(host='192.168.221.128', port=80)
    app.run(host='0.0.0.0', port=8080)
