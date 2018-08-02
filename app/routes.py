import googlemaps, json
from flask import redirect, url_for, render_template, flash, request, jsonify
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.models import User, Car
from app.forms import LoginForm, RegisterForm, EditSettingsForm

@app.route('/')
@app.route('/index')
@app.route('/map')
@login_required
def map():
    return render_template('mapView.html', users=User.query.all())

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('map'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.get(form.email.data)
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('map')
        return redirect(next_page)
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('map'))
    form = RegisterForm()
    if form.validate_on_submit():
        u = User(first_name=str(form.firstName.data), last_name=str(form.lastName.data), email=str(form.email.data),
                 contact_number=str(form.contactNumber.data), gender=str(form.gender.data), home_address=str(form.street.data),
                 home_city=str(form.city.data), home_state=str(form.state.data), gender_preferred=str(form.genderPreferred.data))
        u.set_password(str(form.password.data))

        if form.work.data == 'ballDrive':
            u.work_address = '2330 Ball Drive'
            u.work_city = 'St. Louis'
            u.work_state = 'MO'
        elif form.work.data == 'riderTrail':
            u.work_address = '3470 Rider Trail'
            u.work_city = 'Earth City'
            u.work_state = 'MO'
        else:
            u.work_address = '11432 Lackland Rd'
            u.work_city = 'St. Louis'
            u.work_state = 'MO'
        
        if form.car.data == 'yes':
            c = Car(email=str(form.email.data), num_seats=str(form.numberOfSeats.data), mpg=str(form.mpg.data), manufacturer=str(form.manufacturer.data),
                    model=str(form.model.data), license_plate_num=str(form.number.data))
            db.session.add(c)
            u.cars = [c]

        db.session.add(u)
        db.session.commit()

        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/forgot')
def reset_pass():
    return render_template('reset.html')

@app.route('/edit_settings', methods=['GET', 'POST'])
@login_required
def edit_settings():
    form = EditSettingsForm()
    if form.validate_on_submit():
        current_user.first_name = str(form.firstName.data)
        current_user.last_name = str(form.lastName.data)
        current_user.email = str(form.email.data)
        current_user.contact_number = str(form.contactNumber.data)
        current_user.gender = str(form.gender.data)
        current_user.home_address = str(form.street.data)
        current_user.home_city = str(form.city.data)
        current_user.home_state = str(form.state.data)
        current_user.gender_preferred = str(form.genderPreferred.data)
        if form.password.data is not None:
            current_user.set_password(str(form.password.data))

        if form.work.data == 'ballDrive':
            current_user.work_address = '2330 Ball Drive'
            current_user.work_city = 'St. Louis'
            current_user.work_state = 'MO'
        elif form.work.data == 'riderTrail':
            current_user.work_address = '3470 Rider Trail'
            current_user.work_city = 'Earth City'
            current_user.work_state = 'MO'
        else:
            current_user.work_address = '11432 Lackland Rd'
            current_user.work_city = 'St. Louis'
            current_user.work_state = 'MO'

        if form.car.data == 'yes':
            current_user.cars.num_seats = str(form.numberOfSeats.data)
            current_user.cars.mpg = str(form.mpg.data)
            current_user.cars.manufacturer = str(form.manufacturer.data)
            current_user.cars.model = str(form.model.data)
            current_user.cars.license_plate_num = str(form.number.data)

        db.session.commit()
        return redirect(url_for('map'))

    elif request.method == 'GET':
        form.firstName.data = current_user.first_name
        form.lastName.data = current_user.last_name
        form.email.data = current_user.email
        form.contactNumber.data = current_user.contact_number
        form.gender.data = current_user.gender
        form.street.data = current_user.home_address
        form.city.data = current_user.home_city
        form.state.data = current_user.home_state
        form.genderPreferred.data = current_user.gender_preferred

        if current_user.work_address == '2330 Ball Drive':
            form.work.data == 'ballDrive'
        elif current_user.work_address == '3470 Rider Trail':
            form.work.data == 'riderTrail'
        elif current_user.work_address == '11432 Lackland Rd':
            form.work.data == 'westPortPlace'

        if current_user.car is not None:
            form.car.data = 'yes'
            form.numberOfSeats.data = current_user.cars.num_seats
            form.mpg.data = current_user.cars.mpg
            form.manufacturer.data = current_user.cars.manufacturer
            form.model.data = current_user.cars.model
            form.number.data = current_user.cars.license_plate_num

    return render_template("user.html", form=form)

@app.route('/addresses')
def addresses():
    maps = googlemaps.Client(key='AIzaSyAGdyZJS03riT_kwIXBkBlLCsgds2yxcAc')
    users = User.query.all()
    addrs = {}
    for u in users:
        addr = str(u.home_address) + ' ' + str(u.home_city) + ', '+ str(u.home_state)
        name = str(u.first_name) + ' ' + str(u.last_name)
        res = maps.geocode(addr)
        loc = res[0]['geometry']['location'] #loc dict
        addrs[name] = loc
    return json.dumps(addrs)