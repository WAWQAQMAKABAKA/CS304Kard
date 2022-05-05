use kard_db;

load data local infile 'group-list.csv'
into table `group`
fields terminated by ',' 
lines terminated by '\n'
ignore 1 lines;

load data local infile 'album-list.csv'
into table album
fields terminated by ',' 
lines terminated by '\n'
ignore 1 lines;

load data local infile 'idol-list.csv'
into table idol
fields terminated by ',' 
lines terminated by '\n'
ignore 1 lines;

load data local infile 'card-list.csv'
into table card
fields terminated by ',' 
lines terminated by '\n'
ignore 1 lines;

load data local infile 'user-list.csv'
into table user
fields terminated by ',' 
lines terminated by '\n'
ignore 1 lines;

load data local infile 'item-list.csv'
into table item
fields terminated by ',' 
lines terminated by '\n'
ignore 1 lines;

-- alter table card add avg_price float;


-- update card join
--         (select item.cid as cid, avg(sell.price) as avg_price
--         from item inner join sell on item.itid = sell.itid) as a
--         on card.cid = a.cid
--     set card.avg_price = a.avg_price;