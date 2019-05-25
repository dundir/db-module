from db import ConnectionManager,SessionManager
import models

#Setup Connection to DB
conn = ConnectionManager()

#connect('dbname = thedb', defaults temp.db)
conn.connect()

#Create Session, pass connection
session=SessionManager(conn).session

#Query tablename customers - select *
def query():
   query = session.query(models.Customers).all()
   return query

def addData():
  data = models.Customers(name = 'Ravi Kumar', address = 'Station Road', email = 'blah@email.com')
  session.add(data)
  session.commit()
  return

def printq():
  for row in query():
    print ("id: ",row.id, "Name: ",row.name, "Address:",row.address, "Email:",row.email)
