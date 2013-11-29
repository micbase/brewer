
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



source_7=Source(variety="Grains", name="Rahr 2-Row Pale")
source_7.save()
source_8=Source(variety="Grains", name="Belgian Caramel Pils")
source_8.save()
source_9=Source(variety="Grains", name="Briess Special Roast")
source_9.save()
source_10=Source(variety="Grains", name="Belgian Biscuit malt")
source_10.save()
source_11=Source(variety="Grains", name="English Chocolate Malt")
source_11.save()
source_12=Source(variety="Yeast", name="Wyeast 1272 American Ale Yeast II")
source_12.save()
source_13=Source(variety="Hops", name="Willamette (60-min)")
source_13.save()
source_14=Source(variety="Hops", name="US Goldings (30-min)")
source_14.save()
source_15=Source(variety="Priming Sugar", name="Priming Sugar ")
source_15.save()


source_16=Source(variety="Grains", name="English Maris Otter")
source_16.save()
source_17=Source(variety="Grains", name="English Chocolate Malt")
source_17.save()
source_18=Source(variety="Grains", name="Briess Caramel 120")
source_18.save()
source_19=Source(variety="Grains", name="Belgian Biscuit")
source_19.save()
source_20=Source(variety="Grains", name="Briess Special Roast")
source_20.save()
source_21=Source(variety="Yeast", name="Wyeast 1945 NB NeoBritannia")
source_21.save()
source_22=Source(variety="Hops", name="US Fuggle")
source_22.save()
source_23=Source(variety="Priming Sugar", name="Priming Sugar ")
source_23.save()


recipe_1 = Recipe(name="Bavarian Hefeweizen", inote="Fruit 4lbs of Fresh Peaches", note="Loved this beer for summer and beginning fall. Rated it an 8 out of 10. Friends want to try a fruit version and suggested peach.", brewer=user_1)
recipe_1.save()

recipe_2 = Recipe(name="Irish Red Ale", inote="", note="", brewer=user_2)
recipe_2.save()

recipe_3 = Recipe(name="Nut Brown Ale", inote="", note="", brewer=user_3)
recipe_3.save()


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

ingredient_7=Ingredient(amount=7.5, unit="lbs", note="", source=source_7, recipe=recipe_2)
ingredient_7.save()
ingredient_8=Ingredient(amount=0.75, unit="lbs", note="", source=source_8, recipe=recipe_2)
ingredient_8.save()
ingredient_9=Ingredient(amount=0.25, unit="lbs", note="", source=source_9, recipe=recipe_2)
ingredient_9.save()
ingredient_10=Ingredient(amount=0.125, unit="lbs", note="", source=source_10, recipe=recipe_2)
ingredient_10.save()
ingredient_11=Ingredient(amount=0.125, unit="lbs", note="", source=source_11, recipe=recipe_2)
ingredient_11.save()
ingredient_12=Ingredient(amount=0.0, unit="", note="", source=source_12, recipe=recipe_2)
ingredient_12.save()
ingredient_13=Ingredient(amount=0.75, unit="oz", note="", source=source_13, recipe=recipe_2)
ingredient_13.save()
ingredient_14=Ingredient(amount=0.75, unit="oz", note="", source=source_14, recipe=recipe_2)
ingredient_14.save()
ingredient_15=Ingredient(amount=0.5, unit="oz", note="", source=source_15, recipe=recipe_2)
ingredient_15.save()

ingredient_16=Ingredient(amount=7.5, unit="lbs", note="", source=source_16, recipe=recipe_3)
ingredient_16.save()
ingredient_17=Ingredient(amount=0.25, unit="lbs", note="", source=source_17, recipe=recipe_3)
ingredient_17.save()
ingredient_18=Ingredient(amount=0.25, unit="lbs", note="", source=source_18, recipe=recipe_3)
ingredient_18.save()
ingredient_19=Ingredient(amount=0.25, unit="lbs", note="", source=source_19, recipe=recipe_3)
ingredient_19.save()
ingredient_20=Ingredient(amount=0.25, unit="lbs", note="", source=source_20, recipe=recipe_3)
ingredient_20.save()
ingredient_21=Ingredient(amount=0.0, unit="", note="", source=source_21, recipe=recipe_3)
ingredient_21.save()
ingredient_22=Ingredient(amount=1.0, unit="oz", note="", source=source_22, recipe=recipe_3)
ingredient_22.save()
ingredient_23=Ingredient(amount=0.5, unit="oz", note="", source=source_23, recipe=recipe_3)
ingredient_23.save()



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



procedure_12 = Procedure(title="BREWING DAY", tag="Yeast", content="Incubate Yeast ", note="", recipe = recipe_2)
procedure_12.save()

procedure_13 = Procedure(title="BREWING DAY", tag="Boil", content="2.5 gallons of Water", note="", recipe = recipe_2)
procedure_13.save()

procedure_14 = Procedure(title="BREWING DAY", tag="Mash/Grains", content="Sacch Rest for 60 minutes at 153C", note="", recipe = recipe_2)
procedure_14.save()

procedure_15 = Procedure(title="BREWING DAY", tag="Mash/Grains", content="Mashout for 10 minutes at 170", note="", recipe = recipe_2)
procedure_15.save()

procedure_16 = Procedure(title="BREWING DAY", tag="Hop Boil", content="Add 0.75 oz Willamette 60 mins", note="", recipe = recipe_2)
procedure_16.save()

procedure_17 = Procedure(title="BREWING DAY", tag="Hop Boil 2", content="Add 0.75 oz US Goldings at 30 mins", note="", recipe = recipe_2)
procedure_17.save()

procedure_18 = Procedure(title="BREWING DAY", tag="Cool Wort", content="Cool Wort to 78C", note="", recipe = recipe_2)
procedure_18.save()

procedure_19 = Procedure(title="FERMENTATION: (weeks 1-2)", tag="Fermentation", content="Ferment for 1-2 weeks at 60-72F ", note="", recipe = recipe_2)
procedure_19.save()

procedure_20 = Procedure(title="FERMENTATION: (weeks 1-2)", tag="Secondary", content="Ferment for 2 weeks", note="", recipe = recipe_2)
procedure_20.save()

procedure_21 = Procedure(title="BOTTLING DAY: (2 weeks)", tag="Bottle", content="Mix priming sugar and add to beer before bottling.", note="", recipe = recipe_2)
procedure_21.save()

procedure_22 = Procedure(title="BOTTLING DAY: (2 weeks)", tag="Condition", content="Store bottles at room temperature.", note="", recipe = recipe_2)
procedure_22.save()

procedure_23 = Procedure(title="DRINK: (2 weeks)", tag="Enjoy", content="Beer ready to serve.", note="", recipe = recipe_2)
procedure_23.save()


procedure_24 = Procedure(title="BREWING DAY", tag="Yeast", content="Incubate Yeast ", note="", recipe = recipe_3)
procedure_24.save()

procedure_25 = Procedure(title="BREWING DAY", tag="Boil", content="2.5 gallons of Water", note="", recipe = recipe_3)
procedure_25.save()

procedure_26 = Procedure(title="BREWING DAY", tag="Mash/Grains", content="Sacch Rest for 60 minutes at 154C", note="", recipe = recipe_3)
procedure_26.save()

procedure_27 = Procedure(title="BREWING DAY", tag="Mash/Grains", content="Mashout for 10 minutes at 170", note="", recipe = recipe_3)
procedure_27.save()

procedure_28 = Procedure(title="BREWING DAY", tag="Hop Boil", content="Add 1.0 oz US Fuggle 60 mins", note="", recipe = recipe_3)
procedure_28.save()

procedure_29 = Procedure(title="BREWING DAY", tag="Cool Wort", content="Cool Wort to 78C", note="", recipe = recipe_3)
procedure_29.save()

procedure_30 = Procedure(title="FERMENTATION: (weeks 1-2)", tag="Fermentation", content="Ferment for 1 week at 66-74F.", note="", recipe = recipe_3)
procedure_30.save()

procedure_31 = Procedure(title="FERMENTATION: (weeks 1-2)", tag="Secondary", content="Ferment for 1 week", note="", recipe = recipe_3)
procedure_31.save()

procedure_32 = Procedure(title="BOTTLING DAY: (2 weeks)", tag="Bottle", content="Mix priming sugar and add to beer before bottling.", note="", recipe = recipe_3)
procedure_32.save()

procedure_33 = Procedure(title="BOTTLING DAY: (2 weeks)", tag="Condition", content="Store bottles at room temperature.", note="", recipe = recipe_3)
procedure_33.save()

procedure_34 = Procedure(title="DRINK: (2 weeks)", tag="Enjoy", content="Beer ready to serve.", note="", recipe = recipe_3)
procedure_34.save()