import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'itWebsite.settings')

import django

django.setup()
from scotDives.models import DiveSite, DiveClub


def populate():
    divesitelist = {"Fife Ness": {"rating": 4.5, "latitude": 55.355163, "longitude": -3.378207,
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
                    "Isle of May": {"rating": 2.5, "latitude": 56.174592, "longitude": -5.083394,
                                    "description": "To reach the May Isle, you can either take your own boat and "
                                    			"dock at one of the two inlets, or hop on the May Princess ferry for "
                                    			"a slower transfer. The Isle is home to hundreds of puffins who will "
                                    			"pierce the water around you as you descend. This is an excellent "
                                    			"location if you want to try diving with seals. The resident seals "
                                    			"will enjoy nipping at your fins when you move further out from the "
                                    			"Isle. \n\nDifficulty Level: ??????????????????????? \n\nDepth: >40m "
                                                 "\n\nAvailable Parking: Parking available at harbour in Anstruther",
                                                 "image": "images/isleofman.jpg"},
                    "Kentallen Wall": {"rating": 3, "latitude": 56.385906, "longitude": -2.974244,
                                       "description": "a descritopn  for Kentallen Wall\n\nDifficulty Level: "
                                                "??????????????????????? \n\nDepth: ?????????m"
                                                 "\n\nAvailable Parking: In the Holly Tree carpark in front of the pier",
                                                "image": "images/kentallenwall.jpg"},
                    "The Slates (Ballachulish)": {"rating": 2, "latitude": 55.432373, "longitude": -3.156804,
                                                  "description": "There are several entry points here. From the parking "
                                                  "area, you can walk straight towards the loch and down the slope into "
                                                  "the water. This area is ideal for training due to its sandy base and "
                                                  "lack of current. For the second entry point, walk along the grassy "
                                                  "path leading from the parking area until you reach a sandy slope down "
                                                  "to the water. This entry point quickly leads to a boulder reef at "
                                                  "around 20m depth.\n\nDifficulty Level: ??????????????????????? \n\nDepth: "
                                                 "\n\nAvailable Parking: On site in front of first entry point",
                                                 "image": "images/isleofman.jpg"},
                    "SS Afton": {"rating": 3.5, "latitude": 55.341912, "longitude": -4.733811,
                                 "description": "a descritopn  for SS Afton", "image": "images/ssafton.jpg"}
                    }

    diveclublist = {
        "Club 1.1": {"telephone": 134324, "latitude": 55.355163, "longitude": -3.378207, "address": "address1"},
        "Club 2.1": {"telephone": 234324, "latitude": 56.174592, "longitude": -5.083394, "address": "address2"},
        "Club 3.1": {"telephone": 334324, "latitude": 56.385906, "longitude": -2.974244, "address": "address3"},
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


if __name__ == '__main__':
    print("Starting scotDives population script...")
    populate()

