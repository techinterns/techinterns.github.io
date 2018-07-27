from app import db

class User(db.Model):
    first_name = db.Column(db.String(120), nullable=False)
    last_name = db.Column(db.String(120), nullable=False, index=True)
    gender = db.Column(db.String(20), nullable=False, index=True)
    email = db.Column(db.String(120), unique=True, primary_key=True)
    password_hash = db.Column(db.String(128))

    home_address = db.Column(db.String(120), index=True)
    home_city = db.Column(db.String(120), index=True)
    home_state = db.Column(db.String(2), index=True)
    
    work_address = db.Column(db.String(120), index=True)
    work_city = db.Column(db.String(120), index=True)
    work_state = db.Column(db.String(2), index=True)

    gender_preferred = db.Column(db.String(20), index=True)

    signup_status = db.Column(db.String(20), index=True)

    cars = db.relationship('Car', backref='owner', lazy='dynamic')
    status = db.relationship('Daily_status', backref='employee', lazy='dynamic')

    def __repr__(self):
        return 'User {}'.format(self.email)

class Car(db.Model):
    email = db.Column(db.String(120), db.ForeignKey('user.email'), unique=True, primary_key=True)
    num_seats = db.Column(db.Integer, index=True)
    mpg = db.Column(db.Float())
    manufacturer = db.Column(db.String(60))
    model = db.Column(db.String(60))
    license_plate_num = db.Column(db.String(7), unique=True)

    def __repr__(self):
        return 'Car {}'.format(self.email)

class Daily_status(db.Model):
    email = db.Column(db.String(120), db.ForeignKey('user.email'), unique=True, primary_key=True)
    status = db.Column(db.String(20), index=True, nullable=False)

    def __repr__(self):
        return '{}: {}'.format(self.email, self.status)