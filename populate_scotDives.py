 import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'itWebsite.settings')

import django
django.setup()
from scotDives.models import DiveSite


def populate():

    divesitelist = {"Fife Ness": {"rating": 4.5},
                    "Isle of Man": {"rating": 2.5},
                    "Kentallen Wall": {"rating": 3},
                    "The Slates (Ballachulish)": {"rating": 2},
                    "SS Afton": {"rating": 3.5}
                    }

    for divesite, divesite_data in divesitelist.items():
        c = add_site(divesite, divesite_data["rating"])

    for c in DiveSite.objects.all():
            print(" - {0}".format(str(c)))


def add_site(name, rating):
    c = DiveSite.objects.get_or_create(name=name)[0]
    c.rating = rating
    c.save()
    return c


if __name__ == '__main__':
    print("Starting scotDives population script...")
    populate()