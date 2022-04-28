import cs304dbi as dbi


def get_all_groups(conn):
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

def get_albumcards(conn, aid):
    curs = dbi.dict_cursor(conn)
    sql = '''
        select cid, count, idid
        from card
        where aid = %s
        order by idid;
    '''
    curs.execute(sql, [aid])
    cards = curs.fetchall()

    return cards