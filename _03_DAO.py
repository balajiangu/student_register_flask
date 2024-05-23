import mysql.connector



def insert_dao(data):
    #step : 1 get connection
    a = mysql.connector.connect(host = "localhost",
                                user = "root",
                                password = "Arvb73@#",
                                database = "final")

    # step : 2 get cursor
    cursor = a.cursor()

    #step : 3 write query
    query = "INSERT INTO stu_10 VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"

    # step : 4 execute query
    values = tuple(data.values())
    cursor.execute(query,values)

    #step : 5 commit
    a.commit()
    a.close()

    return ("data stored successfully!")






def select_dao(x):
    # step : 1 get connection
    a = mysql.connector.connect(host="localhost",
                                user="root",
                                password="Arvb73@#",
                                database="final")

    # step : 2 get cursor
    cursor = a.cursor()

    # step : 3 write query
    query = "SELECT * FROM stu_10"

    #step : 4 execute query
    cursor.execute(query)
    records = cursor.fetchall()
    "The datas are :"
    for i in records:
        x.append(i)
    return(x)
    # step : 5 commit
    a.commit()







def update_dao(key,value,new_key,new_value):
    # step : 1 get connection
    a = mysql.connector.connect(host="localhost",
                                user="root",
                                password="Arvb73@#",
                                database="final")

    # step : 2 get cursor
    cursor = a.cursor()

    # step : 3 write query
    query = "UPDATE stu_10 set {} = '{}' WHERE {} = '{}'".format(new_key,new_value,key[0],value[0])

    # step : 4 execute query
    cursor.execute(query)

    # step : 5 commit
    a.commit()
    return "data updated successfully!"







def delete_dao(delete_key,delete_value):
    # step : 1 get connection
    a = mysql.connector.connect(host="localhost",
                                user="root",
                                password="Arvb73@#",
                                database="final")

    # step : 2 get cursor
    cursor = a.cursor()

    # step : 3 write query
    query = "DELETE FROM stu_10 WHERE {} = '{}'".format(delete_key,delete_value)

    # step : 4 execute query
    cursor.execute(query)

    #step : 5 commit
    a.commit()
    return "Data deleted successfully!"