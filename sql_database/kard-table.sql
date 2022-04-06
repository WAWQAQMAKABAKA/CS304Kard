use mt1_db;

drop table if exists sell;
drop table if exists items;
drop table if exists users;
drop table if exists cards;
drop table if exists idols;
drop table if exists albums;
drop table if exists groups;

CREATE TABLE groups (
    gid int not null,
    name varchar(50),
    PRIMARY KEY (gid)
)
ENGINE=InnoDB;

CREATE TABLE albums (
    aid int not null,
    gid int not null,
    name varchar(50),
    PRIMARY KEY (aid),
    foreign key (gid) references groups(gid) 
        on update restrict
        on delete restrict
)
ENGINE=InnoDB;

CREATE TABLE idols (
    idid int not null,
    gid int not null,
    name varchar(50),
    PRIMARY KEY (idid),
    foreign key (gid) references groups(gid) 
        on update restrict
        on delete restrict
)
ENGINE=InnoDB;

CREATE TABLE cards (
    cid int not null,
    count int not null,
    gid int not null,
    aid int not null,
    idid int not null,
    PRIMARY KEY (cid),
    foreign key (gid) references groups(gid) 
        on update restrict
        on delete restrict,
    foreign key (aid) references albums(aid) 
        on update restrict
        on delete restrict,
    foreign key (idid) references idols(idid) 
        on update restrict
        on delete restrict
)
ENGINE=InnoDB;

CREATE TABLE users (
    uid int not null,
    name varchar(50),
    phnum char(10),
    address varchar(100) not null,
    PRIMARY KEY (uid)
)
ENGINE=InnoDB;

CREATE TABLE items (
    itid int not null,
    cid int not null,
    status enum('available','sold'),
    description varchar(100),
    PRIMARY KEY (itid),
    foreign key (cid) references cards(cid) 
        on update restrict
        on delete restrict
)
ENGINE=InnoDB;

CREATE TABLE sell (
    uid int not null,
    itid int not null,
    price int not null,
    buy int,
    PRIMARY KEY (uid,itid),
    foreign key (uid) references users(uid) 
        on update restrict
        on delete restrict,
    foreign key (itid) references items(itid) 
        on update restrict
        on delete restrict,
    foreign key (buy) references users(uid) 
        on update restrict
        on delete restrict
)
ENGINE=InnoDB;
