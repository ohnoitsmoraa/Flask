from app import app
from model import db, User

# Ceating an app context
with app.app_context():
    db.session.add(User(username='Danger', email='admin@gmail.com', password='!!!', age=45))
    db.session.add(User(username='CBK', email='pass@gmail.com', password='MONEY', age=50))
    db.session.add(User(username='Joy', email='sifa@gmail.com', password='SISTER', age=26))

    db.session.commit()
    
    print("Database created successfully!")
