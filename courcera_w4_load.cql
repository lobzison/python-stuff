LOAD CSV FROM "file:///C:/chat_create_team_chat.csv" AS row 
MERGE (u:User {id: toInteger(row[0])}) MERGE (t:Team {id: toInteger(row[1])}) 
MERGE (c:TeamChatSession {id: toInteger(row[2])}) 
MERGE (u)-[:CreatesSession{timeStamp: row[3]}]->(c) 
MERGE (c)-[:OwnedBy{timeStamp: row[3]}]->(t)

LOAD CSV FROM "file:///C:/chat_join_team_chat.csv" AS row 
MERGE (u:User {id: toInteger(row[0])})
MERGE (c:TeamChatSession {id: toInteger(row[1])}) 
MERGE (u)-[:Joins{timeStamp: row[2]}]->(c)

LOAD CSV FROM "file:///C:/chat_leave_team_chat.csv" AS row 
MERGE (u:User {id: toInteger(row[0])})
MERGE (c:TeamChatSession {id: toInteger(row[1])}) 
MERGE (u)-[:Leaves{timeStamp: row[2]}]->(c)

LOAD CSV FROM "file:///C:/chat_item_team_chat.csv" AS row 
MERGE (u:User {id: toInteger(row[0])})
MERGE (c:TeamChatSession {id: toInteger(row[1])}) 
MERGE (i:ChatItem {id: toInteger(row[2])}) 
MERGE (u)-[:CreateChat{timeStamp: row[2]}]->(i)
MERGE (i)-[:PartOf{timeStamp: row[2]}]->(c)

LOAD CSV FROM "file:///C:/chat_mention_team_chat.csv" AS row 
MERGE (i:ChatItem {id: toInteger(row[0])}) 
MERGE (u:User {id: toInteger(row[1])})
MERGE (i)-[:Mentioned{timeStamp: row[2]}]->(u)

LOAD CSV FROM "file:///C:/chat_respond_team_chat.csv" AS row 
MERGE (i:ChatItem {id: toInteger(row[0])}) 
MERGE (i2:ChatItem {id: toInteger(row[1])})
MERGE (i)-[:ResponseTo{timeStamp: row[2]}]->(i2)

--1.1
match p=(a)-[:ResponseTo*]->(b)
return length(p) as l 
order by l DESC
limit 1
--1.2
match p=(a)-[:ResponseTo*]->(b)
where length(p) = 9
WITH p
match m = (u:User)-[:CreateChat]->(t)
where t in nodes(p)
return m
--2.1
match (u:User)-[:CreateChat]-(b)
return u.id, count(u)
order by count(u) DESC
limit 10
--2.2
match (c:ChatItem)-[:PartOf]->(t:TeamChatSession)-[:OwnedBy]-(n)
return n.id, count(n)
order by count(n) DESC
LIMIT 10
--2.3
match (u:User)-[]->(c:ChatItem)-[:PartOf]->(t:TeamChatSession)-[:OwnedBy]-(n)
where n.id in [82, 185, 112]
and u.id in [394, 2067, 209]
return u.id


match (u1:User)-[i:InteractsWith]-(u2:User) 
where u1.id in [209,554,1087]
with  u1, collect(distinct  u2.id)  as  neighbors
match (u3:User)-[i2:InteractsWith]-(u4:User) 
where u3.id in neighbors and u4.id in  neighbors
with  u1, u3, u4, 
neighbors,  size(neighbors) as  k,
case when  count(distinct  i2) > 0 then  1 else  0 end as  value
return  u1.id as  UserId, k,  k*(k - 1),  sum(value)  as  edges,
toFloat(sum(value))/toFloat((k*(k - 1)))  as  coefficient order by  coefficient desc

match (u1:User)-[:CreateChat]->(c:ChatItem)-[:Mentioned]->(u2:User) 
create (u1)-[:InteractsWith]->(u2)

match (u1:User)-[:CreateChat]->(c1:ChatItem)-[:ResponseTo]->(c2:ChatItem)<-[:CreateChat]-(u2:User) 
create (u1)-[:InteractsWith]->(u2)

match (u1:User)-[r:InteractsWith]->(u1:User)  
delete  r

--v4
match (u1:User)-[i:InteractsWith]-(u2:User) 
where u1.id in [209,554,1087]
with  u1, collect(distinct  u2.id)  as  neighbors
match (u3:User)-[i2:InteractsWith]-(u4:User) 
where u3.id in neighbors and u4.id in  neighbors
WITH u1, u3, u4, neighbors, size(neighbors) as n,
case when  count(distinct  i2) > 0 then 1 else  0 end as  weight
return u1.id as  UserId, sum(weight)/toFloat(n*(n-1))
order by sum(weight)/toFloat(n*(n-1)) DESC