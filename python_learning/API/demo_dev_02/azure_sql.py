import textwrap
import pyodbc

#specify the driver
driver = '{ODBC Driver 17 for SQL Server}'

server_name = '12.0.2000.8'
database_name = 'AdventureWorksLT'

#cretae our server url
server = '{server_name}.database.windows.net,1433'.format(server_name=server_name)

#define username and password
username = 'adminsqluser'
password = 'Kiras1321!"#$'


#creta the full connection string
connection_string = textwrap.dedent('''
    Driver={driver};
    Server={server};
    Database{database};
    Uid={username};
    Pwd={password};
    Encrypted=no;
    TrustServerCertificate=no;
    Connection Timeout=30;
'''.format(
    driver=driver,
    server=server,
    database=database_name,
    username=username,
    password=password
    ))


cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database_name+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()


#Sample select query
cursor.execute("SELECT @@version;") 
row = cursor.fetchone() 
while row: 
    print(row[0])
    row = cursor.fetchone()


#creata a new pyodbc connection object
#cnxn: pyodbc.Connection = pyodbc.connect(connection_string)

#create a new cursor object from the connection
#crsr: pyodbc.Cursor = cnxn.cursor()

#select_sql = "SELECT * FROM [SalesLT].[Customer]"


#execute select query
#crsr.execute(select_sql)

#grab the data
#print(crsr.fetchall())

#close the connection once we are done
cnxn.close()