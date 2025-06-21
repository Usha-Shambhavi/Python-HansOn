#1. Create a table by name as contact and must have all the attributes as we have in API
#2. Fetch all the data using GET method from the API
#3. Insert all the data into database

import requests as rq
import oracledb

# Connect to Oracle DB

oracledb.init_oracle_client(lib_dir=r"C:\Users\Lenovo\Downloads\instantclient-basic-windows.x64-19.22.0.0.0dbru\instantclient_19_22")

servername = "localhost:1521/XE"
username = "usha"
password ="usha"

connection = oracledb.connect(user=username, password =password, dsn=servername) #dsn = Database Server Name
cursor = connection.cursor()

cursor.execute(
    """CREATE TABLE Contacts (ID NUMBER PRIMARY KEY,
    NAME       VARCHAR2(100),
    COMPANY    VARCHAR2(100),
    USERNAME   VARCHAR2(50),
    EMAIL      VARCHAR2(100),
    ADDRESS    VARCHAR2(150),
    ZIP        VARCHAR2(20),
    STATE      VARCHAR2(50),
    COUNTRY    VARCHAR2(50),
    PHONE      VARCHAR2(30),
    PHOTO      VARCHAR2(200))
""")

connection.commit()

# Connect to URL

endpointurl = "https://fake-json-api.mock.beeceptor.com/users"
response = rq.get(endpointurl)
print("Response Code: ",response.status_code)

if response.status_code == 200:
    print("Successful")
    data = response.json()
    print("data in json: ",data)


    for d in data:
        #print("inside data element d", d['country'])

        #cursor.execute("insert into EMP (EMPNO,ENAME) VALUES(:1,:2)",(d['id'],d['name']))
        #ename = d['name']
        
    
        cursor.execute("insert into Contacts (ID,NAME,COMPANY,USERNAME,EMAIL,ADDRESS,ZIP,STATE,COUNTRY,PHONE,PHOTO) " \
        "VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10,:11)",
         (d['id'],d['name'],d['company'],d['username'],d['email'],d['address'],d['zip'],d['state'],d['country'],d['phone'],d['photo']))
        #id	name	company	username	email	address	zip	state	country	phone	photo

        connection.commit()
        print()
else:
    print("Not Successfull!")