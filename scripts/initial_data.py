
from django.contrib.auth.models import User

from brewer.models import Source, Ingredient, Recipe, Procedure

import datetime

admin = User.objects.create_user(username="admin", email="noreply@micbase.com", password="purpleTeam",
    first_name="admin", last_name="admin")
admin.save()

user_1 = User.objects.create_user(username="farquharson", email="farquharsonWWW@gmail.com", password="purpleTeam",
    first_name="Deborah", last_name="Farquharson")
user_1.save()


user_2 = User.objects.create_user(username="acramond", email="aCramond@sina.com", password="purpleTeam",
    first_name="Amee", last_name="Cramond")
user_2.save()


user_3 = User.objects.create_user(username="gtoroosian", email="gToroosian@u.northwestern.edu", password="purpleTeam",
    first_name="Greg", last_name="Toroosian")
user_3.save()


user_4 = User.objects.create_user(username="rydbeck", email="rRydbeck@fgcu.edu", password="purpleTeam",
    first_name="Rachael", last_name="Rydbeck")
user_4.save()

user_5 = User.objects.create_user(username="adulany", email="aDulany@gmail.com", password="purpleTeam",
    first_name="Andrew", last_name="Dulany")
user_5.save()

source_1 = Source(variety="Grains", name="Weyermann Pale Wheat Malt")
source_1.save()
source_2 = Source(variety="Grains", name="German Pilsner Malt")
source_2.save()
source_3 = Source(variety="Yeast", name="Wyeast 3068 Weihenstephan Wheat")
source_3.save()
source_4 = Source(variety="Hops", name="Hallertau")
source_4.save()
source_5 = Source(variety="Priming Sugar", name="Priming Sugar")
source_5.save()
source_6 = Source(variety="Fruit", name="Peaches")
source_6.save()
source_7 = Source(variety="Grains", name="Rahr 2-Row Pale")
source_7.save()
source_8 = Source(variety="Grains", name="Belgian Caramel Pils")
source_8.save()
source_9 = Source(variety="Grains", name="Briess Special Roast")
source_9.save()
source_10 = Source(variety="Grains", name="Belgian Biscuit malt")
source_10.save()
source_11 = Source(variety="Grains", name="English Chocolate Malt")
source_11.save()
source_12 = Source(variety="Yeast", name="Wyeast 1272 American Ale Yeast II")
source_12.save()
source_13 = Source(variety="Hops", name="Willamette (60-min)")
source_13.save()
source_14 = Source(variety="Hops", name="US Goldings (30-min)")
source_14.save()

source_16 = Source(variety="Grains", name="English Maris Otter")
source_16.save()

source_18 = Source(variety="Grains", name="Briess Caramel 120")
source_18.save()
source_19 = Source(variety="Grains", name="Belgian Biscuit")
source_19.save()

source_21 = Source(variety="Yeast", name="Wyeast 1945 NB NeoBritannia")
source_21.save()
source_22 = Source(variety="Hops", name="US Fuggle")
source_22.save()