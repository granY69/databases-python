from mysqlConnection import DatabaseConnection

db_connection = DatabaseConnection("dannys_diner")
cursor, db = db_connection.connection()

#read operation
query = "select * from staff;"
cursor.execute(query)
fetch_result = cursor.fetchall()

print("**"*(2**5))
for data in fetch_result:
    print("Name: ", data[1])
    print("Address: ", data[2])
    print("City: ", data[2])
print("**"*(2**5))

#create operation
query = "create table staff (id int, name varchar(255), address varchar(255), city varchar(255));"
cursor.execute(query)

#insert
name_list = [("Seemab", "St# 03", "Attock"), ("Salman", "St# 09", "Okara"), ("Hassan", "St# 13", "Gujranwala")]
query = "insert into staff(name, address, city) values(%s, %s, %s);"
for name, address, city in name_list:
    values = (name, address, city)
    cursor.execute(query, values)
db.commit()

# delete
query = "delete from staff where id=%s"
value = (2,)
cursor.execute(query, value)
db.commit()

#update
query = "update staff set name=%s where id=%s;"
value = ("Muhammad Abdullah", 3)
cursor.execute(query, value)

#close the db connection
db_connection.close_connection()