import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'itWebsite.settings')

import django

django.setup()
from scotDives.models import DiveSite, DiveClub, Picture, FutureDive, Review, UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from scotDives.models import UserProfile
from django.db.models import Avg


def populate():
    profile_reb = [{"image": "profile_images/rebecca.jpg"}]
    profile_chris = [{"image": "profile_images/christos.jpg"}]
    profile_sad = [{"image": "profile_images/sadita.jpg"}]
    profile_imam = [{"image": "profile_images/imam.jpg"}]
    reviews_fifeness = [
        {"username": "Rebecca",
         "rating": 4,
         "comment": "Went down on a cloudy calm day, excellent visibility, around 12m. Saw some lobsters, "
                    "crabs and found the old boiler out at 15 metres.",
         "date": '2016-10-25 14:30:59'}
    ]
    reviews_may = [
        {"username": "Rebecca",
         "rating": 4,
         "comment": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt "
                    "ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco "
                    "laboris nisi ut aliquip ex ea commodo consequat.",
         "date": '2016-10-25 14:40:59'},
        {"username": "Christos",
         "rating": 5,
         "comment": "Duis aute irure dolor in reprehenderit in "
                    "voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat "
                    "non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
         "date": '2017-10-25 14:40:59'}
    ]
    reviews_kentallen = [
        {"username": "Rebecca",
         "rating": 3,
         "comment": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt "
                    "ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco "
                    "laboris nisi ut aliquip ex ea commodo consequat.",
         "date": '2016-10-25 14:50:59'},
        {"username": "Sadita",
         "rating": 5,
         "comment": "Duis aute irure dolor in reprehenderit in "
                    "voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat "
                    "non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
         "date": '2017-11-25 14:40:59'}
    ]
    reviews_slates = [
        {"username": "Imam",
         "rating": 5,
         "comment": "The lagoon is a great spot for training beginners. Calm, clear and plenty of small creatures "
                    "to keep them entertained",
         "date": '2018-03-25 14:40:59'},
        {"username": "Christos",
         "rating": 5,
         "comment": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt "
                    "ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco "
                    "laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in "
                    "voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat "
                    "non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
         "date": '2017-08-25 14:40:59'}
    ]
    reviews_mull = [
        {"username": "Sadita",
         "rating": 4,
         "comment": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt "
                    "ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco "
                    "laboris nisi ut aliquip ex ea commodo consequat.",
         "date": '2017-10-25 14:50:59'},
        {"username": "Christos",
         "rating": 3,
         "comment": "Duis aute irure dolor in reprehenderit in "
                    "voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat "
                    "non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
         "date": '2016-11-25 14:40:59'}
    ]

    future_dives_reb = [
        {"divesite": "The Slates (Ballachulish)"},
        {"divesite": "Isle of Mull"},
    ]
    future_dives_chris = [
        {"divesite": "Fife Ness"},
        {"divesite": "Kentallen Wall"}
    ]
    future_dives_sad = [
        {"divesite": "Fife Ness"},
        {"divesite": "Isle of May"},
        {"divesite": "The Slates (Ballachulish)"}
    ]
    future_dives_imam = [
        {"divesite": "Fife Ness"},
        {"divesite": "Kentallen Wall"}
    ]
    divesitelist = {"Fife Ness": {"reviews": reviews_fifeness, "latitude": 56.278470, "longitude": -2.591467,
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
                    "Isle of May": {"reviews": reviews_may, "latitude": 56.183826, "longitude": -2.565637,
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
                    "Kentallen Wall": {"reviews": reviews_kentallen, "latitude": 56.663384, "longitude": -5.252388,
                                       "description": "The pier makes this dive site an excellent location for training "
                                                      "beginners. At high tide, simply sit down on the slip wall and slip into"
                                                      " the water. The seabed here is sandy and teeming with small crabs and "
                                                      "large sea snails. Be sure to check out the large boiler near the pier "
                                                      "wall - many a lobster has made it its home. Once you have passed the "
                                                      "pier wall, head in the direction of the green buoy - This will lead you "
                                                      "to the underwater wall. The top of the wall can be found at 15m depth "
                                                      "and extends down to 32m at its base.\n\nDifficulty Level: "
                                                      "Suitable for beginners\n\nDepth: 32m\n\nAvailable Parking: In the Holly"
                                                      " Tree carpark in front of the pier", "image": "images/kentallen.jpg"},
                    "The Slates (Ballachulish)": {"reviews": reviews_slates, "latitude": 56.686069, "longitude": -5.208013,
                                                  "description": "There are several entry points here. From the parking "
                                                                 "area, you can walk straight towards the loch and down the slope into "
                                                                 "the water. This area is ideal for training due to its sandy base and "
                                                                 "lack of current. For the second entry point, walk along the grassy "
                                                                 "path leading from the parking area until you reach a sandy slope down "
                                                                 "to the water. This entry point quickly leads to a boulder reef at "
                                                                 "around 20m depth.\n\nDifficulty Level: Sports Diver and above \n\nDepth: "
                                                                 ">50m\n\nAvailable Parking: On site in front of first entry point",
                                                  "image": "images/slates.jpg"},
                    "Isle of Mull": {"reviews": reviews_mull, "latitude": 56.459406, "longitude": -6.028123,
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
        "Rebecca": {"profile": profile_reb, "future_dives": future_dives_reb, "first_name": "Rebecca", "last_name": "McGinn", "email": "1105308M@student.gla.ac.uk", "password": make_password("RMGlasgow")},
        "Christos": {"profile": profile_chris, "future_dives": future_dives_chris, "first_name": "Christos", "last_name": "Karangelis", "email": "2345191K@student.gla.ac.uk", "password": make_password("CKGlasgow")},
        "Sadita": {"profile": profile_sad, "future_dives": future_dives_sad, "first_name": "Sadita", "last_name": "Ahmed", "email": "2304007A@student.gla.ac.uk", "password": make_password("SAGlasgow")},
        "Imam": {"profile": profile_imam, "future_dives": future_dives_imam, "first_name": "Imam", "last_name": "Reiza", "email": "2274277R@student.gla.ac.uk", "password": make_password("IRGlasgow")},
        }

    pic = {
        "slates.jpg": {"description": "View from The Slates", "location": "The Slates"},
        "fifeness.jpg": {"description": "Fife Ness at low tide", "location": "Fife Ness"},
        "islemull.jpg": {"description": "Shuna Wreck", "location": "Sound of Mull"},
        "scotland.jpg": {"description": "View over Isle of Mull", "location": "Isle of Mull"},
        "IMG_0002.jpg": {"description": "View over Kentallen Pier", "location": "Kentallen Wall"},
    }
    for username, user_data in users.items():
        username = add_user(username, user_data["first_name"], user_data["last_name"], user_data["email"],
                            user_data["password"])
        for u in user_data["profile"]:
            add_profile(username, u["image"])

    for divesite, divesite_data in divesitelist.items():
        c = add_site(divesite, divesite_data["latitude"], divesite_data["longitude"],
                     divesite_data["description"], divesite_data["image"])
        for r in divesite_data["reviews"]:
            add_reviews(divesite, r["username"], r["rating"], r["comment"], r["date"])
        add_avg_rating(divesite)

    for d in DiveSite.objects.all():
        for r in Review.objects.filter(divesite=d):
            print(" - {0} - {1}".format(str(d), str(r)))

    for diveclub, diveclub_data in diveclublist.items():
        d = add_club(diveclub, diveclub_data["telephone"], diveclub_data["latitude"], diveclub_data["longitude"],
                     diveclub_data["address"])
    for d in DiveClub.objects.all():
        print(" - {0}".format(str(d)))

    for username, user_data in users.items():
        for f in user_data["future_dives"]:
            add_future_dives(username, f["divesite"])

    for u in User.objects.all():
        for f in FutureDive.objects.filter(user=u):
            print(" - {0} - {1}".format(str(u), str(f)))
        for up in UserProfile.objects.filter(user=u):
            print(" - {0} - {1}".format(str(u), str(up.picture)))

    for h in User.objects.all():
        print(" - {0}".format(str(h)))

    for pic, pic_data in pic.items():
        pic = add_picture(pic, pic_data["description"], pic_data["location"])


def add_site(name, latitude, longitude, description, image):
    s = DiveSite.objects.get_or_create(name=name)[0]
    s.latitude = latitude
    s.longitude = longitude
    s.description = description
    s.image = image
    s.save()
    return s


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


def add_picture(pic, description, location):
    pic = Picture.objects.get_or_create(pic=pic)[0]
    pic.description = description
    pic.location = location
    pic.save()
    return pic


def add_future_dives(username, divesite):
    dive = DiveSite.objects.get(name=divesite)
    user = User.objects.get(username=username)
    future_dive = FutureDive.objects.get_or_create(user=user, divesite=dive)
    return future_dive


def add_reviews(site, username, rate, comment, date):
    user = User.objects.get(username=username)
    divesite = DiveSite.objects.get(name=site)
    r = Review.objects.get_or_create(user=user, divesite=divesite)[0]
    r.rating = rate
    r.comment = comment
    r.date = date
    r.save()
    return r


def add_avg_rating(divesite):
    s = DiveSite.objects.get(name=divesite)
    avg_rating = Review.objects.filter(divesite=s).aggregate(Avg('rating'))
    s.rating = avg_rating['rating__avg']
    s.save()
    return s


def add_profile(username, image):
    profile = UserProfile.objects.get_or_create(user=username)[0]
    profile.picture = image
    profile.save()
    return profile


if __name__ == '__main__':
    print("Starting scotDives population script...")
    populate()



