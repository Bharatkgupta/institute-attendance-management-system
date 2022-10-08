dbConfig = {
     'user': 'bharat',  # use your admin name
     'password': "bharatsql",  # use your admin password
     'host': '127.0.0.1',  # IP address of localhost
     'database': 'attendance', # your database (comment this line when running dbcreate.py)
     'raise_on_warnings': True,
}

import mysql.connector
from mysql.connector import errorcode
try:
  cnx = mysql.connector.connect(**dbConfig)
  print(cnx)
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cnx.close()