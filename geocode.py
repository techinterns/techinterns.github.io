import googlemaps, pprint, json
from app import db
from app.models import User

def main():
    p = pprint.PrettyPrinter()
    maps = googlemaps.Client(key='AIzaSyAGdyZJS03riT_kwIXBkBlLCsgds2yxcAc')
    users = User.query.all()
    addrs = {}
    for u in users:
        addr = str(u.home_address) + ' ' + str(u.home_city) + ', '+ str(u.home_state)
        name = str(u.first_name) + ' ' + str(u.last_name)
        res = maps.geocode(addr)
        loc = res[0]['geometry']['location'] #loc dict
        addrs[name] = loc
    p.pprint(addrs)

if __name__ == '__main__':
    main()