*Kard For K-poppers: Mini-Card Exchange Platform
As k-pop goes viral all over the world, more and more fans get obsessed with the unique “photocard” culture. Every time a k-pop group comes back, they release a new album that includes both the CD and one photocard - an exclusive idol selfie that hasn’t been released on other platforms. K-pop fans are addicted to collecting those small paper cards. Suppose there are n members in one band, and for each member, there are m unique photos. Hence, there are n*m different photo cards that might come with the album. Then there comes the tricky part: the mini card is given at random, so a fan who has a preference for one member is not guaranteed to obtain the card they want. Hence, fans post their cards and the corresponding pricing on Twitter/Instagram and pm each other to negotiate the order. Therefore, we are inspired to design a webpage that can serve as an intermediate platform for people to exchange, buy, or sell k-pop mini-cards until they get their desired photos. 

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
