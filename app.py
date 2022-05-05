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

# For pic folder
app.config['CARDPIC'] = 'cardpic'
app.config['UPLOADS'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 1*1024*1024 # 1 MB

@app.route('/')
def index():
    if 'uid' not in session:
        return redirect(url_for('login'))
    else:
        conn = dbi.connect()
        cards = dbact.get_most_popular_cards(conn)
        cards = dbact.filepath_generator(cards, app.config['CARDPIC'], 'cid', '.JPG')
        return render_template('index.html', cards = cards, uid=session.get('uid'), usrname=session.get('username'))

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        conn = dbi.connect()
        uid = request.form.get('uid')
        if dbact.check_uid(conn, uid):
            session['uid'] = uid
            session['username'] = dbact.get_username(conn, uid)
        else:
            flash("Please log in with a valid user ID!")
        return redirect(url_for('index'))

@app.route('/buy/', methods=['GET', 'POST'])
def buy():
    if request.method == 'GET':
        conn = dbi.connect()
        groups = dbact.get_all_groups(conn)
        uid = session.get('uid')
        if uid == None:
            flash('Please log in first!')
            return redirect(url_for('login'))
        else:
            return render_template('buy_group.html', groups = groups, uid=uid, usrname=session.get('username'))
    else:
        gid = request.form.get('group')
        return redirect(url_for('buy_group', gid = gid))

@app.route('/buy/g<gid>', methods=['GET','POST'])
def buy_group(gid):
    if request.method == 'GET':
        conn = dbi.connect()
        albums = dbact.get_albums(conn, gid)
        uid = session.get('uid')
        if uid == None:
            flash('Please log in first!')
            return redirect(url_for('login'))
        else:
            return render_template('buy_album.html', gid = gid, albums = albums, uid=uid, usrname=session.get('username'))
    else:
        aid = request.form.get('album')
        return redirect(url_for('buy_album', aid = aid))

@app.route('/buy/a<aid>', methods = ['GET', 'POST'])
def buy_album(aid):
    if request.method == 'GET':
        conn = dbi.connect()
        cards = dbact.get_available_albumcards(conn, aid)
        cards = dbact.filepath_generator(cards, app.config['CARDPIC'],'cid', '.JPG')
        uid = session.get('uid')
        if uid == None:
            flash('Please log in first!')
            return redirect(url_for('login'))
        else:
            return render_template('buy_cards.html', aid = aid, cards = cards, uid=uid, usrname=session.get('username'))
    else:
        cid = request.form.get('card')
        return redirect(url_for('buy_card', cid = cid))

@app.route('/buy/c<cid>', methods=['GET','POST'])
def buy_card(cid):
    if request.method == 'GET':
        conn = dbi.connect()
        items = dbact.get_available_carditem(conn, cid)
        items = dbact.filepath_generator(items, app.config['UPLOADS'], 'itid', '.jpg')
        uid = session.get('uid')
        if uid == None:
            flash('Please log in first!')
            return redirect(url_for('login'))
        else:
            return render_template('buy_items.html', cid = cid, items = items, uid=uid, usrname=session.get('username'))
    else:
        itid = request.form.get('item')
        return redirect(url_for('buy_item', itid = itid))

@app.route('/buy/it<itid>', methods=['GET','POST'])
def buy_item(itid):
    if request.method == 'GET':
        conn = dbi.connect()
        item = dbact.get_item_info(conn, itid)
        item = dbact.filepath_generator(item, app.config['UPLOADS'], 'itid', '.jpg')
        item = item[0]
        uid = session.get('uid')
        if uid == None:
            flash('Please log in first!')
            return redirect(url_for('login'))
        else:
            return render_template('buy_item_info.html', itid = itid, item = item, uid=uid, usrname=session.get('username'))
    else:
        conn = dbi.connect()
        dbact.update_buy_card(conn, itid, boughtby=session.get('uid'))
        cid = dbact.itid_to_cid(conn, itid)
        dbact.change_card_count(conn, cid, False)
        return redirect(url_for("success"))

@app.route('/sell/', methods=['GET', 'POST'])
def sell():
    if request.method == 'GET':
        conn = dbi.connect()
        groups = dbact.get_all_groups(conn)
        uid = session.get('uid')
        if uid == None:
            flash('Please log in first!')
            return redirect(url_for('login'))
        else:
            return render_template('sell_group.html', groups = groups, uid=uid, usrname=session.get('username'))
    else:
        gid = request.form.get('group')
        return redirect(url_for('sell_group', gid = gid))

@app.route('/sell/g<gid>', methods=['GET','POST'])
def sell_group(gid):
    if request.method == 'GET':
        conn = dbi.connect()
        albums = dbact.get_albums(conn, gid)
        idols = dbact.get_idols(conn, gid)
        uid = session.get('uid')
        if uid == None:
            flash('Please log in first!')
            return redirect(url_for('login'))
        else:
            return render_template('sell_album.html', gid = gid, albums = albums, idols = idols, uid=uid, usrname=session.get('username'))
    else:
        aid = request.form.get('album')
        idid = request.form.get('idol')
        return redirect(url_for('sell_album', aid = aid, idid = idid))

@app.route('/sell/a<aid>/id<idid>', methods = ['GET', 'POST'])
def sell_album(aid, idid):
    if request.method == 'GET':
        conn = dbi.connect()
        cards = dbact.get_idol_albumcards(conn, aid, idid)
        cards = dbact.filepath_generator(cards, app.config['CARDPIC'],'cid', '.JPG')
        uid = session.get('uid')
        if uid == None:
            flash('Please log in first!')
            return redirect(url_for('login'))
        else:
            return render_template('sell_cards.html', aid = aid, idid = idid, cards = cards, uid=uid, usrname=session.get('username'))
    else:
        cid = request.form.get('card')
        return redirect(url_for('sell_card', cid = cid))

@app.route('/sell/c<cid>', methods=['GET','POST'])
def sell_card(cid):
    if request.method == 'GET':
        conn = dbi.connect()
        card = dbact.get_card_info(conn, cid)
        uid = session.get('uid')
        if uid == None:
            flash('Please log in first!')
            return redirect(url_for('login'))
        else:
            return render_template('sell_item_info.html', card = card, uid=uid, usrname=session.get('username'))
    else:
        description = request.form.get('description')
        price = request.form.get('price')
        conn = dbi.connect()
        itid = dbact.update_sell_card(conn, cid, session.get('uid'), price, description)
        dbact.change_card_count(conn, cid, True)
        return redirect(url_for("upload_pic", cid = cid, itid = itid))

@app.route('/sell/c<cid>/it<itid>', methods=['GET','POST'])
def upload_pic(cid, itid):
    if request.method == "GET":
        conn = dbi.connect()
        card = dbact.get_card_info(conn, cid)
        uid = session.get('uid')
        if uid == None:
            flash('Please log in first!')
            return redirect(url_for('login'))
        else:
            return render_template('sell_upload_pic.html', itid = itid, card = card, uid=uid, usrname=session.get('username'))
    else:
        try:
            f = request.files['pic']
            pathname = os.path.join(app.config['UPLOADS'], str(itid) + ".jpg")
            f.save(os.path.join("static", pathname))

            conn = dbi.connect()
            card = dbact.get_card_info(conn, cid)
            item = dbact.get_item_info(conn, itid)
            return render_template("sell_review_info.html", item = item[0], card = card, pathname = pathname, uid=session.get('uid'), usrname=session.get('username'))

        except Exception as err:
            flash('Upload failed {why}'.format(why=err))
            return redirect(url_for("upload_pic", cid=cid, itid = itid))
        
@app.route('/success', methods=['GET', "POST"])
def success():
    uid = session.get('uid')
    if uid == None:
        flash('Please log in first!')
        return redirect(url_for('login'))
    else:
        return render_template('transaction_success.html', uid=uid, usrname=session.get('username'))

@app.before_first_request
def init_db():
    dbi.cache_cnf()
    # set this local variable to 'wmdb' or your personal or team db
    db_to_use = 'kard_db' 
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
