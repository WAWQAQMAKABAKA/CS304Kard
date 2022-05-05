use mt1_db;

drop table if exists buy;
drop table if exists sell;
drop table if exists item;
drop table if exists user;
drop table if exists card;
drop table if exists idol;
drop table if exists album;
drop table if exists `group`;

CREATE TABLE `group` (
    gid int not null,
    name varchar(50),
    PRIMARY KEY (gid)
)
ENGINE=InnoDB;

CREATE TABLE album (
    aid int not null,
    gid int not null,
    name varchar(50),
    PRIMARY KEY (aid),
    foreign key (gid) references `group`(gid) 
        on update restrict
        on delete restrict
)
ENGINE=InnoDB;

CREATE TABLE idol (
    idid int not null,
    gid int not null,
    name varchar(50),
    PRIMARY KEY (idid),
    foreign key (gid) references `group`(gid) 
        on update restrict
        on delete restrict
)
ENGINE=InnoDB;

CREATE TABLE card (
    cid int not null,
    count int not null,
    gid int not null,
    aid int not null,
    idid int not null,
    PRIMARY KEY (cid),
    foreign key (gid) references `group`(gid) 
        on update restrict
        on delete restrict,
    foreign key (aid) references album(aid) 
        on update restrict
        on delete restrict,
    foreign key (idid) references idol(idid) 
        on update restrict
        on delete restrict
)
ENGINE=InnoDB;

CREATE TABLE user (
    uid int not null,
    name varchar(50),
    phnum char(10),
    address varchar(100) not null,
    PRIMARY KEY (uid)
)
ENGINE=InnoDB;

CREATE TABLE item (
    itid int not null,
    cid int not null,
    status enum('available','sold'),
    description varchar(100),
    PRIMARY KEY (itid),
    foreign key (cid) references card(cid) 
        on update restrict
        on delete restrict
)
ENGINE=InnoDB;

CREATE TABLE sell (
    uid int not null,
    itid int not null,
    price int not null,
    PRIMARY KEY (uid,itid),
    foreign key (uid) references user(uid) 
        on update restrict
        on delete restrict,
    foreign key (itid) references item(itid) 
        on update restrict
        on delete restrict
)
ENGINE=InnoDB;

CREATE TABLE buy (
    uid int not null,
    itid int not null,
    price int not null,
    PRIMARY KEY (uid, itid),
    foreign key (uid) references user(uid) 
        on update restrict
        on delete restrict,
    foreign key (itid) references item(itid) 
        on update restrict
        on delete restrict
)
ENGINE=InnoDB;
