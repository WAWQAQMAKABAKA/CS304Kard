select cid, idol.name as idname, album.name as aname, group.name as gname
from card
inner join `group` using (gid)
inner join idol using (idid)
inner join album using (aid)
where cid = 10;
