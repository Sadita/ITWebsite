import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'itWebsite.settings')

import django

django.setup()
from scotDives.models import DiveSite, DiveClub


def populate():
    divesitelist = {"Fife Ness": {"rating": 4.5, "latitude": 55.355163, "longitude": -3.378207,
                                  "description": "a descritopn for Fife Ness"},
                    "Isle of Man": {"rating": 2.5, "latitude": 56.174592, "longitude": -5.083394,
                                    "description": "a descritopn  for Isle of Man"},
                    "Kentallen Wall": {"rating": 3, "latitude": 56.385906, "longitude": -2.974244,
                                       "description": "a descritopn  for Kentallen Wall"},
                    "The Slates (Ballachulish)": {"rating": 2, "latitude": 55.432373, "longitude": -3.156804,
                                                  "description": "a descritopn  for The Slates"},
                    "SS Afton": {"rating": 3.5, "latitude": 55.341912, "longitude": -4.733811,
                                 "description": "a descritopn  for SS Afton"}
                    }

    diveclublist = {
        "Club 1.1": {"telephone": 134324, "latitude": 55.355163, "longitude": -3.378207, "address": "address1"},
        "Club 2.1": {"telephone": 234324, "latitude": 56.174592, "longitude": -5.083394, "address": "address2"},
        "Club 3.1": {"telephone": 334324, "latitude": 56.385906, "longitude": -2.974244, "address": "address3"},
        }

    for divesite, divesite_data in divesitelist.items():
        c = add_site(divesite, divesite_data["rating"], divesite_data["latitude"], divesite_data["longitude"],
                     divesite_data["description"])

    for c in DiveSite.objects.all():
        print(" - {0}".format(str(c)))

    for diveclub, diveclub_data in diveclublist.items():
        d = add_club(diveclub, diveclub_data["telephone"], diveclub_data["latitude"], diveclub_data["longitude"],
                     diveclub_data["address"])

    for d in DiveClub.objects.all():
        print(" - {0}".format(str(d)))


def add_site(name, rating, latitude, longitude, description):
    c = DiveSite.objects.get_or_create(name=name)[0]
    c.rating = rating
    c.latitude = latitude
    c.longitude = longitude
    c.description = description
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