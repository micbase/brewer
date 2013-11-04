
from django.contrib.auth.models import User

from brewer.models import Source, Ingredient, Recipe, Procedure

import datetime

admin = User.objects.create_user(username="admin", email="noreply@micbase.com", password="purpleTeam",
    first_name="admin", last_name="admin")
admin.save()

user_1 = User.objects.create_user(username="farquharson", email="farquharsonWWW@gmail.com", password="purpleTeam",
    first_name="Scott", last_name="Farquharson")
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


source_1=Source(variety="Grains", name="Weyermann Pale Wheat Malt")
source_1.save()

source_2=Source(variety="Grains", name="German Pilsner Malt")
source_2.save()

source_3=Source(variety="Yeast", name="Wyeast 3068 Weihenstephan Wheat")
source_3.save()

source_4=Source(variety="Hops", name="Hallertau")
source_4.save()

source_5=Source(variety="Priming Sugar", name="Priming Sugar ")
source_5.save()

source_6=Source(variety="Fruit", name="Peaches")
source_6.save()


recipe_1 = Recipe(name="Bavarian Hefeweizen", inote="Fruit 4lbs of Fresh Peaches", note="Loved this beer for summer and beginning fall. Rated it an 8 out of 10. Friends want to try a fruit version and suggested peach.", brewer=user_2)
recipe_1.save()


ingredient_1=Ingredient(amount=5.5, unit="lbs", note="", source=source_1, recipe=recipe_1)
ingredient_1.save()
ingredient_2=Ingredient(amount=4, unit="lbs", note="", source=source_2, recipe=recipe_1)
ingredient_2.save()
ingredient_3=Ingredient(amount=0.0, unit="", note="", source=source_3, recipe=recipe_1)
ingredient_3.save()
ingredient_4=Ingredient(amount=0.75, unit="oz", note="", source=source_4, recipe=recipe_1)
ingredient_4.save()
ingredient_5=Ingredient(amount=0.25, unit="oz", note="", source=source_4, recipe=recipe_1)
ingredient_5.save()
ingredient_6=Ingredient(amount=0.5, unit="oz", note="", source=source_5, recipe=recipe_1)
ingredient_6.save()


procedure_1 = Procedure(title="BREWING DAY", tag="Yeast", content="Incubate Yeast ", note="", recipe = recipe_1)
procedure_1.save()

procedure_2 = Procedure(title="BREWING DAY", tag="Boil", content="2.5 gallons of Water", note="", recipe = recipe_1)
procedure_2.save()

procedure_3 = Procedure(title="BREWING DAY", tag="Mash/Grains", content="Mash for 90 minutes at 153C", note="", recipe = recipe_1)
procedure_3.save()

procedure_4 = Procedure(title="BREWING DAY", tag="Hop Boil", content="Add .75oz Hallertau at 45mins", note="", recipe = recipe_1)
procedure_4.save()

procedure_5 = Procedure(title="BREWING DAY", tag="Hop Boil 2", content="Add .25oz Hallertau at 15mins", note="remember to still the swirl the grain to help clear the beer", recipe = recipe_1)
procedure_5.save()

procedure_6 = Procedure(title="BREWING DAY", tag="Cool Wort", content="Cool Wort to 78C - 100C.", note="", recipe = recipe_1)
procedure_6.save()

procedure_7 = Procedure(title="FERMENTATION: (weeks 1-2)", tag="Fermentation", content="Ferment for 10 days at 68F. ", note="", recipe = recipe_1)
procedure_7.save()

procedure_8 = Procedure(title="FERMENTATION: (weeks 1-2)", tag="Secondary", content="No secondary fermentation.", note="add 4lbs of peaches to the secondary fermenation", recipe = recipe_1)
procedure_8.save()

procedure_9 = Procedure(title="BOTTLING DAY: (2 weeks)", tag="Bottle", content="Mix priming sugar and add to beer before bottling.", note="", recipe = recipe_1)
procedure_9.save()

procedure_10 = Procedure(title="BOTTLING DAY: (2 weeks)", tag="Condition", content="Store bottles at room temperature.", note="", recipe = recipe_1)
procedure_10.save()

procedure_11 = Procedure(title="DRINK: (2 weeks)", tag="Enjoy", content="Beer ready to serve.", note="", recipe = recipe_1)
procedure_11.save()



