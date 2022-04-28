import cs304dbi as dbi


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
