from flask import (Flask, render_template, make_response, url_for, request,
                   redirect, flash, session, send_from_directory, jsonify)
from werkzeug.utils import secure_filename
app = Flask(__name__)

# one or the other of these. Defaults to MySQL (PyMySQL)
# change comment characters to switch to SQLite

import cs304dbi as dbi
# import cs304dbi_sqlite3 as dbi
import  db_interaction as dbact

import random

app.secret_key = 'your secret here'
# replace that with a random key
app.secret_key = ''.join([ random.choice(('ABCDEFGHIJKLMNOPQRSTUVXYZ' +
                                          'abcdefghijklmnopqrstuvxyz' +
                                          '0123456789'))
                           for i in range(20) ])

# This gets us better error messages for certain common request errors
app.config['TRAP_BAD_REQUEST_ERRORS'] = True

@app.route('/')
def index():
    # if 'uid' not in session:
    #     return render_template('login.html')
    # else:
    return render_template('base.html')

@app.route('/login/', methods=['POST'])
def login():
    uid = request.form.get('uid')
    session['uid'] = uid
    return redirect(url_for('index'))


@app.route('/buy/', methods=['GET', 'POST'])
def buy():
    if request.method == 'GET':
        conn = dbi.connect()
        groups = dbact.get_all_groups(conn)
        return render_template('buy_group.html', groups = groups)
    else:
        gid = request.form.get('group')
        return redirect(url_for('buy_group', gid = gid))

@app.route('/buy/g<gid>', methods=['GET','POST'])
def buy_group(gid):
    if request.method == 'GET':
        conn = dbi.connect()
        albums = dbact.get_albums(conn, gid)
        return render_template('buy_album.html', gid = gid, albums = albums)
    else:
        aid = request.form.get('album')
        return redirect(url_for('buy_album', aid = aid))

@app.route('/buy/a<aid>', methods = ['GET', 'POST'])
def buy_album(aid):
    if request.method == 'GET':
        conn = dbi.connect()
        cards = dbact.get_albumcards(conn, aid)

        return render_template('buy_cards.html', cards = cards)
    else:
        # next phase
        pass



@app.route('/sell/', methods=['GET', 'POST'])
def sell():
    if request.method == 'GET':
        conn = dbi.connect()
        groups = dbact.get_all_groups(conn)
        return render_template('sell_group.html', groups = groups)
    else:
        gid = request.form.get('group')
        return redirect(url_for('sell_group', gid = gid))

@app.route('/sell/g<gid>', methods=['GET','POST'])
def sell_group(gid):
    if request.method == 'GET':
        conn = dbi.connect()
        albums = dbact.get_albums(conn, gid)
        return render_template('sell_album.html', gid = gid, albums = albums)
    else:
        aid = request.form.get('album')
        return redirect(url_for('sell_album', aid = aid))

@app.route('/sell/a<aid>', methods = ['GET', 'POST'])
def sell_album(aid):
    if request.method == 'GET':
        conn = dbi.connect()
        cards = dbact.get_albumcards(conn, aid)
        return render_template('sell_cards.html', cards = cards)
    else:
        # next phase
        pass




@app.before_first_request
def init_db():
    dbi.cache_cnf()
    # set this local variable to 'wmdb' or your personal or team db
    db_to_use = 'yc5_db' 
    dbi.use(db_to_use)
    print('will connect to {}'.format(db_to_use))

if __name__ == '__main__':
    import sys, os
    if len(sys.argv) > 1:
        # arg, if any, is the desired port number
        port = int(sys.argv[1])
        assert(port>1024)
    else:
        port = os.getuid()
    app.debug = True
    app.run('0.0.0.0',port)
