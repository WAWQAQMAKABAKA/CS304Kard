A basic app.py with some example routes, a static folder with a css
file in it, and a templates folder with some files.

Basic Setup Codes:
source venv/bin/activate

cd sql_database
dos2unix *.csv
mysql
source kard-table.sql
source kard-load-data.sql

Database Attributes:

Item:
-	itid(item id)
-	cid(card id) ->foreign key reference from table card
-   upby(uid) -> foreign key reference from table user
-   boughtby(uid) -> can be null -> foreign key reference from table user
-   price (float)
-	status (either “available” or “sold”)
-	description(how new it is, condition of the card) 
User:
-	uid(user id)
-	name(username)
-	phnum(phone number)
-	address 
Card:
-	cid(card id)-> jpg name is cid.jpg
-	count(how many are available to sell)
-	gid(group id)->foreign key reference from table group
-	aid(album id)->foreign key reference from table album
-	idid (idol id)->foreign key reference from table idol
Idol:
-	idid(idol id)
-	gid(group id)->foreign key reference from table group
-	name(name of idol)
Album:
-	aid(album id)
-	gid(group id)->foreign key reference from table group
-	name(name of the album)
Group:
-	gid(group id)
-	name(name of the group)

