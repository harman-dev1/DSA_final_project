import mysql.connector 
from mysql.connector import Error
from pyvis import network
net = network.Network()

def passRecord(rec , field):
    item = ""
    coma = 1
    size = len(rec)
    for i in size:
        if rec[i] == ',':
            coma = coma + 1
        elif(coma == field):
            item = item . rec[i]
    return item
def getArray(name):
    list = []
    list = name.split(",")
    return list
       

    

   
try:
    connection = mysql.connector.connect(host='localhost',
                                         database='friendtable',
                                         user='root',
                                         password='')
    sql_select_Query = "select * from friendlist"
    # MySQLCursorDict creates a cursor that returns rows as dictionaries
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    
    # print("Fetching each row using column name")
    name = []
    friend = []
    for row in records:
        name.append(row['name'])
        friend.append(row['friends'])
        net.add_node(row['name'])

        # array = getArray(friend)
   
   
    for (i,j) in zip (name, friend):
        list = []
        if j is not None:
            list = j.split(",")
        if(list is not None):
            for x in list:
                if x is not '':
                    net.add_edge(i , x)
                

except Error as e:
    print("Error reading data from MySQL table", e)

net.show("./mapHTML.html")
