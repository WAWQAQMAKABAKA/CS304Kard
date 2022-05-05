import cs304dbi as dbi
import os

def get_all_groups(conn):
    """This function gets all idol groups in the grouop table

    Args:
        conn: connection to our database

    Returns:
        list: a list of dictionary objects, each with keys gid and name
    """    
    curs = dbi.dict_cursor(conn)
    sql = '''
        select *
        from `group`
        order by name;
    '''
    curs.execute(sql)
    groups = curs.fetchall()

    return groups

def get_albums(conn, gid):
    """This function returns all the albums of a given group

    Args:
        conn: conneciton to our database
        gid (int): gid of the given group

    Returns:
        list: a list of dictionary objects, each with keys aid and name
    """    
    curs = dbi.dict_cursor(conn)
    sql = '''
        select aid, name
        from album
        where gid = %s
        order by aid;
    '''
    curs.execute(sql, [gid])
    albums = curs.fetchall()

    return albums

def get_idols(conn, gid):
    """This function returns all the idols of a given group

    Args:
        conn: conneciton to our database
        gid (int): gid of the given group

    Returns:
        list: a list of dictionary objects, each with keys idid and name
    """    
    curs = dbi.dict_cursor(conn)
    sql = '''
        select idid, name
        from idol
        where gid = %s
        order by idid;
    '''
    curs.execute(sql, [gid])
    idols = curs.fetchall()

    return idols


def get_all_albumcards(conn, aid):
    """This function gets all cards of a given album

    Args:
        conn: connection to our database
        aid (int): the aid of the given album

    Returns:
        list: a list of dictionary objects, each with keys cid, count, and idid
    """    
    curs = dbi.dict_cursor(conn)
    sql = '''
        select cid, count, idol.name as name
        from card
        inner join idol using (idid)
        where aid = %s
        order by idid;
    '''
    curs.execute(sql, [aid])
    cards = curs.fetchall()

    return cards

def get_idol_albumcards(conn, aid, idid):
    """This function gets all cards of a given album of a given idol

    Args:
        conn: connection to our database
        aid (int): the aid of the given album
        idid (int): the idid of the given idol

    Returns:
        list: a list of dictionary objects, each with keys cid, count, name
    """    
    curs = dbi.dict_cursor(conn)
    sql = '''
        select cid, count, idol.name as name
        from card
        inner join idol using (idid)
        where aid = %s and idid = %s
        order by idid;
    '''
    curs.execute(sql, [aid, idid])
    cards = curs.fetchall()

    return cards

def get_available_albumcards(conn, aid):
    """This function returns all available cards (count >0) of a given album

    Args:
        conn: connection to our database
        aid (int): the aid of a given album

    Returns:
        list: a list of dictionary objects, each with keys cid, count, and idid
    """    
    curs = dbi.dict_cursor(conn)
    sql = '''
        select cid, count, idol.name as name
        from card
        inner join idol using (idid)
        where aid = %s and count > 0
        order by count desc;
    '''
    curs.execute(sql, [aid])
    cards = curs.fetchall()

    return cards

def get_available_carditem(conn, cid):
    """This function returns all available card items of a given card

    Args:
        conn: connection to our database
        cid (int): the cid of a given card

    Returns:
        list: a list of dictionary objects, each with keys itid and price
    """    
    curs = dbi.dict_cursor(conn)
    sql = '''
        select itid, price
        from item
        where status = 'available' and cid = %s
        order by price;
    '''
    curs.execute(sql, [cid])
    items = curs.fetchall()

    return items

def get_item_info(conn, itid):
    """This function returns all the info of a given item

    Args:
        conn: connection to our database
        itid (int): the itid of a given item

    Returns:
        list: a list of dictionary objects, each with keys itid, price, upby, description
    """    
    curs = dbi.dict_cursor(conn)
    sql = '''
        select itid, price, upby, description
        from item
        where itid = %s;
    '''
    curs.execute(sql, [itid])
    item = curs.fetchall()

    return item

def get_card_info(conn, cid):
    """This function returns all relevant information of a given card

    Args:
        conn: connection to our database
        cid (int): the cid of a given card

    Returns:
        dict: a dictionary object, with keys cid, idname, aname, gname
    """    
    curs = dbi.dict_cursor(conn)
    sql = '''
        select cid, idol.name as idname, album.name as aname, group.name as gname
        from card
            inner join `group` using (gid)
            inner join idol using (idid)
            inner join album using (aid)
        where cid = %s;
    '''
    curs.execute(sql, [cid])
    card = curs.fetchone()

    return card

def update_sell_card(conn):
    curs = dbi.dict_cursor(conn)
    sql = '''
    
    '''
    curs.execute(sql, [nm, filename, filename])
    conn.commit()

def filepath_generator(lists, path, file_name, file_type):
    """This function generates a relative path to the file of the given file_type in the given path for each dictionary object in the list

    Args:
        cards (list): a list of dictionary objects
        path (str): path to the folder that contains the file
        file_name (str): key name for which the value is the filename
        file_type (str): file type, eg. '.JPG'

    Returns:
        list: a list of updated dictionary objects
    """    

    for l in lists:
        l['path'] = os.path.join(path, str(l[file_name]) + file_type)
    
    return lists