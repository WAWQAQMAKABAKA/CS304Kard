use yc5_db;

load data local infile 'groups-list.csv'
into table `group`
fields terminated by ',' 
lines terminated by '\n'
ignore 1 lines;

load data local infile 'albums-list.csv'
into table album
fields terminated by ',' 
lines terminated by '\n'
ignore 1 lines;

load data local infile 'idols-list.csv'
into table idol
fields terminated by ',' 
lines terminated by '\n'
ignore 1 lines;

load data local infile 'cards-list.csv'
into table card
fields terminated by ',' 
lines terminated by '\n'
ignore 1 lines;

insert into user(uid,name,phnum,address)
values
    (1,'Claire','3392130056','Unit 4813'),
    (2,'Michelle','7817085206','Unit 5727'),
    (3,'Helen','1234567890','Unit 1234'),
    (4,'Scott','2345678901','106 Central Street'),
    (5,'Emily','3456789012','21 Wellesley College Rd'),
    (6,'Nina','2035023283','Mcafee 121'),
    (7,'Malika','6174547280','TCW 120'),
    (8,'Sophia','6692530695','TCW 125'),
    (9,'Breanna','7577273530','Bates 307'),
    (10,'Jolina','6469196104','Freeman 210');

load data local infile 'items-list.csv'
into table item
fields terminated by ',' 
lines terminated by '\n'
ignore 1 lines;

load data local infile 'sell-list.csv'
into table sell
fields terminated by ',' 
lines terminated by '\n'
ignore 1 lines;

load data local infile 'buy-list.csv'
into table buy
fields terminated by ',' 
lines terminated by '\n'
ignore 1 lines;

alter table card add avg_price float;


-- update card join
--         (select item.cid as cid, avg(sell.price) as avg_price
--         from item inner join sell on item.itid = sell.itid) as a
--         on card.cid = a.cid
--     set card.avg_price = a.avg_price;