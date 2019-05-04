import db
#import models

a = db.data('temp.db')
a.connect()
a.session()

query = a.session.query(db.models.Customers).all()

#c1 = Customers(name = 'Ravi Kumar', address = 'Station Road', email = 'blah@email.com')
#session.add(c1)
#session.commit()

#q = session.query(Customers).all()
# Iterates over all Customer Records
for row in query:
    print ("id: ",row.id, "Name: ",row.name, "Address:",row.address, "Email:",row.email)
