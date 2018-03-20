import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'itWebsite.settings')

import django

django.setup()
from scotDives.models import DiveSite, DiveClub
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from scotDives.models import UserProfile


def populate():
    divesitelist = {"Fife Ness": {"rating": 4.5, "latitude": 56.278470, "longitude": -2.591467,
                                  "description": "Two possible entry points. The first is directly in front of the "
                                                 "parking spaces. This ‘lagoon’ is usually very calm, clear and "
                                                 "makes an excellent training location. Lots of fish and crabs can "
                                                 "be spotted hiding in the rocks on either side of this lagoon. "
                                                 "Also plenty of golf balls from the local course! \nFor the second "
                                                 "entry point, turn right from the carpark (facing the water) and "
                                                 "follow the grassy path up the hillock which leads to a narrow "
                                                 "channel which allows easy access at high tide. \n\nDifficulty "
                                                 "Level: All levels, suitable for training beginners \n\nDepth: 15m "
                                                 "\n\nAvailable Parking: On site in front of first entry point",
                                  "image": "images/fifeness.jpg"},
                    "Isle of May": {"rating": 2.5, "latitude": 56.183826, "longitude": -2.565637,
                                    "description": "To reach the May Isle, you can either take your own boat and "
                                    			"dock at one of the two inlets, or hop on the May Princess ferry for "
                                    			"a slower transfer. The Isle is home to hundreds of puffins who will "
                                    			"pierce the water around you as you descend. This is an excellent "
                                    			"location if you want to try diving with seals. The resident seals "
                                    			"will enjoy nipping at your fins when you move further out from the "
                                    			"Isle. \n\nDifficulty Level: Suitable for Sports Diver and higher \n\n"
                                          "Depth: >40m "
                                                 "\n\nAvailable Parking: Parking available at harbour in Anstruther",
                                                 "image": "images/isleofman.jpg"},
                    "Kentallen Wall": {"rating": 3, "latitude": 56.663384, "longitude": -5.252388,
                                       "description": "a descritopn  for Kentallen Wall\n\nDifficulty Level: "
                                                "??????????????????????? \n\nDepth: ?????????m"
                                                 "\n\nAvailable Parking: In the Holly Tree carpark in front of the pier",
                                                "image": "images/kentallenwall.jpg"},
                    "The Slates (Ballachulish)": {"rating": 2, "latitude": 56.686069, "longitude": -5.208013,
                                                  "description": "There are several entry points here. From the parking "
                                                  "area, you can walk straight towards the loch and down the slope into "
                                                  "the water. This area is ideal for training due to its sandy base and "
                                                  "lack of current. For the second entry point, walk along the grassy "
                                                  "path leading from the parking area until you reach a sandy slope down "
                                                  "to the water. This entry point quickly leads to a boulder reef at "
                                                  "around 20m depth.\n\nDifficulty Level: ??????????????????????? \n\nDepth: "
                                                 "\n\nAvailable Parking: On site in front of first entry point",
                                                 "image": "images/isleofman.jpg"},
                    "Isle of Mull": {"rating": 3.5, "latitude": 56.459406, "longitude": -6.028123,
                                 "description": "You are guaranteed to encounter a plethora of marine life while diving in "
                                                "the Sound of Mull. Nudibranchs, anemones, sunstars, deadmen’s fingers are "
                                                " just a few of the creatures you will come across while diving in this "
                                                " stretch of water. The Shuna wreck is a must-see, as it is teeming with "
                                                "marine life. The wreck can be founda at 30m but be aware of the silty seabed"
                                                "- it is very easy to disturb visibility down here.\n\nDifficulty Level: "
                                                "The shore dives on the Isle of Mull are suitable for all levels. It is "
                                                "recommended that only Sports Divers and above should attempt to visit the "
                                                "Shuna wreck, given its depth. \n\nDepth: >40m\n\nAvailable Parking: "
                                                "Plenty of locations across the island.", "image": "images/islemull.jpg"}
                    }

    diveclublist = {
        "Aquatron Dive Centre": {"telephone": '0141 429 7575', "latitude": 55.856376, "longitude": -4.244666, "address": "Glasgow"},
        "Scottish Sub Aqua Club": {"telephone": '0800 228 9099', "latitude": 55.968677, "longitude": -3.192192, "address": "Edinburgh"},
        "Divebunker": {"telephone": '01592 874380', "latitude": 56.066473, "longitude": -3.229619, "address": "Burntisland"},
        "Marine Quest": {"telephone": '0189 075 2444', "latitude": 55.873526, "longitude": -2.092201, "address": "Eyemouth"},
        "Cupar Sub Aqua Club": {"telephone": '01334 471457', "latitude": 56.317979, "longitude": -3.010441, "address": "Cupar"},
        }

    users = {
        "Rebecca": {"first_name": "Rebecca", "last_name": "McGinn", "email": "1105308M@student.gla.ac.uk", "password": make_password("RMGlasgow")},
        "Christos": {"first_name": "Christos", "last_name": "Karangelis", "email": "2345191K@student.gla.ac.uk", "password": make_password("CKGlasgow")},
        "Sadita": {"first_name": "Sadita", "last_name": "Ahmed", "email": "2304007A@student.gla.ac.uk", "password": make_password("SAGlasgow")},
        "Imam": {"first_name": "Imma", "last_name": "Reiza", "email": "2274277R@student.gla.ac.uk", "password": make_password("IRGlasgow")},
        }

    for divesite, divesite_data in divesitelist.items():
        c = add_site(divesite, divesite_data["rating"], divesite_data["latitude"], divesite_data["longitude"],
                     divesite_data["description"], divesite_data["image"])

    for c in DiveSite.objects.all():
        print(" - {0} - {1}".format(str(c), str(c.image)))

    for diveclub, diveclub_data in diveclublist.items():
        d = add_club(diveclub, diveclub_data["telephone"], diveclub_data["latitude"], diveclub_data["longitude"],
                     diveclub_data["address"])

    for d in DiveClub.objects.all():
        print(" - {0}".format(str(d)))

    for username, user_data in users.items():
        username = add_user(username, user_data["first_name"], user_data["last_name"], user_data["email"], user_data["password"])

    for h in User.objects.all():
        print(" - {0}".format(str(h)))

def add_site(name, rating, latitude, longitude, description, image):
    c = DiveSite.objects.get_or_create(name=name)[0]
    c.rating = rating
    c.latitude = latitude
    c.longitude = longitude
    c.description = description
    c.image = image
    c.save()
    return c

def add_club(name, telephone, latitude, longitude, address):
    d = DiveClub.objects.get_or_create(name=name)[0]
    d.telephone = telephone
    d.latitude = latitude
    d.longitude = longitude
    d.address = address
    d.save()
    return d

def add_user(username, first_name, last_name, email, password):
    username = User.objects.get_or_create(username=username)[0]
    username.first_name = first_name
    username.last_name = last_name
    username.email = email
    username.password = password
    username.save()
    return username


if __name__ == '__main__':
    print("Starting scotDives population script...")
    populate()

