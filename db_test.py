from app import db
from app.models import User

print(User.query.all())