import mysql.connector

# Open database connection
db = mysql.connector.connect(user='root',
                              host='localhost',
                              database='fillthegap')

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = """INSERT INTO universities(name)
   VALUES ('University of South Africa'),
   ('University of Pretoria'),
   ('Stellenbosch University'),
   ('Rhodes University'),
   ('University of the Witwatersrand'),
   ('Cape Peninsula University of Technology'),
   ('Durban University of Technology'),
   ('Tshwane University of Technology'),
   ('Central University of Technology'),
   ('Nelson Mandela Metropolitan University'),
   ('Vaal University of Technology'),
   ('Walter Sisulu University'),
   ('Mangosuthu University of Technology'),
   ('University of Venda'),
   ('University of Zululand'),
   ('North-West University'),
   ('University of Limpopo'),
   ('Fort Hare University'),
   ('University of Mpumalanga'),
   ('Sol Plaatje University'),
   ('University of KwaZulu-Natal'),
   ('National University of Lesotho'),
   ('University of Botswana'),
   ('National University of Science and Technology'),
   ('University of Swaziland'),
   ('Midrand Graduate Institute'),
   ('Regent Business School'),
   ('Rosebank College'),
   ('Boston City Campus & Business College')"""

try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# disconnect from server
db.close()