
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from brewer.models import Source, Ingredient, Recipe, Procedure


class RegisterForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Your Username'
        }))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Your Password'
        }))
    email = forms.EmailField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Your Email Address'
        }))
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Your First Name'
        }))
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Your Last Name'
        }))

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_username(self):
        count = User.objects.filter(
            username__exact=self.cleaned_data['username']).count()
        if count >= 1:
            raise forms.ValidationError("This username has been taken")
        else:
            return self.cleaned_data['username']

    def clean_email(self):
        count = User.objects.filter(
            email__exact=self.cleaned_data['email']).count()
        if count >= 1:
            raise forms.ValidationError("This email has been used")
        else:
            return self.cleaned_data['email']

    def save(self):
        User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
            email=self.cleaned_data['email'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            )
        user = authenticate(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
        )
        recipe_1 = Recipe(name="Bavarian Hefeweizen", inote="Fruit 4lbs of Fresh Peaches", note="Loved this beer for summer and beginning fall. Rated it an 8 out of 10. Friends want to try a fruit version and suggested peach.", brewer=user)
        recipe_1.save()

        recipe_2 = Recipe(name="Irish Red Ale", inote="", note="", brewer=user)
        recipe_2.save()

        recipe_3 = Recipe(name="Nut Brown Ale", inote="", note="", brewer=user)
        recipe_3.save()

        source_1 = Source.objects.get(variety="Grains", name="Weyermann Pale Wheat Malt")

        source_2 = Source.objects.get(variety="Grains", name="German Pilsner Malt")

        source_3 = Source.objects.get(variety="Yeast", name="Wyeast 3068 Weihenstephan Wheat")

        source_4 = Source.objects.get(variety="Hops", name="Hallertau")

        source_5 = Source.objects.get(variety="Priming Sugar", name="Priming Sugar")

        source_6 = Source.objects.get(variety="Fruit", name="Peaches")

        source_7 = Source.objects.get(variety="Grains", name="Rahr 2-Row Pale")

        source_8 = Source.objects.get(variety="Grains", name="Belgian Caramel Pils")

        source_9 = Source.objects.get(variety="Grains", name="Briess Special Roast")

        source_10 = Source.objects.get(variety="Grains", name="Belgian Biscuit malt")

        source_11 = Source.objects.get(variety="Grains", name="English Chocolate Malt")

        source_12 = Source.objects.get(variety="Yeast", name="Wyeast 1272 American Ale Yeast II")

        source_13 = Source.objects.get(variety="Hops", name="Willamette (60-min)")

        source_14 = Source.objects.get(variety="Hops", name="US Goldings (30-min)")


        source_16 = Source.objects.get(variety="Grains", name="English Maris Otter")


        source_18 = Source.objects.get(variety="Grains", name="Briess Caramel 120")

        source_19 = Source.objects.get(variety="Grains", name="Belgian Biscuit")


        source_21 = Source.objects.get(variety="Yeast", name="Wyeast 1945 NB NeoBritannia")

        source_22 = Source.objects.get(variety="Hops", name="US Fuggle")



        ingredient_1 = Ingredient(amount=5.5, unit="lbs", note="", source=source_1, recipe=recipe_1)
        ingredient_1.save()
        ingredient_2 = Ingredient(amount=4, unit="lbs", note="", source=source_2, recipe=recipe_1)
        ingredient_2.save()
        ingredient_3 = Ingredient(amount=0.0, unit="", note="", source=source_3, recipe=recipe_1)
        ingredient_3.save()
        ingredient_4 = Ingredient(amount=0.75, unit="oz", note="", source=source_4, recipe=recipe_1)
        ingredient_4.save()
        ingredient_5 = Ingredient(amount=0.25, unit="oz", note="", source=source_4, recipe=recipe_1)
        ingredient_5.save()
        ingredient_6 = Ingredient(amount=0.5, unit="oz", note="", source=source_5, recipe=recipe_1)
        ingredient_6.save()
        ingredient_7 = Ingredient(amount=7.5, unit="lbs", note="", source=source_7, recipe=recipe_2)
        ingredient_7.save()
        ingredient_8 = Ingredient(amount=0.75, unit="lbs", note="", source=source_8, recipe=recipe_2)
        ingredient_8.save()
        ingredient_9 = Ingredient(amount=0.25, unit="lbs", note="", source=source_9, recipe=recipe_2)
        ingredient_9.save()
        ingredient_10 = Ingredient(amount=0.125, unit="lbs", note="", source=source_10, recipe=recipe_2)
        ingredient_10.save()
        ingredient_11 = Ingredient(amount=0.125, unit="lbs", note="", source=source_11, recipe=recipe_2)
        ingredient_11.save()
        ingredient_12 = Ingredient(amount=0.0, unit="", note="", source=source_12, recipe=recipe_2)
        ingredient_12.save()
        ingredient_13 = Ingredient(amount=0.75, unit="oz", note="", source=source_13, recipe=recipe_2)
        ingredient_13.save()
        ingredient_14 = Ingredient(amount=0.75, unit="oz", note="", source=source_14, recipe=recipe_2)
        ingredient_14.save()
        ingredient_15 = Ingredient(amount=0.5, unit="oz", note="", source=source_5, recipe=recipe_2)
        ingredient_15.save()
        ingredient_16 = Ingredient(amount=7.5, unit="lbs", note="", source=source_16, recipe=recipe_3)
        ingredient_16.save()
        ingredient_17 = Ingredient(amount=0.25, unit="lbs", note="", source=source_11, recipe=recipe_3)
        ingredient_17.save()
        ingredient_18 = Ingredient(amount=0.25, unit="lbs", note="", source=source_18, recipe=recipe_3)
        ingredient_18.save()
        ingredient_19 = Ingredient(amount=0.25, unit="lbs", note="", source=source_19, recipe=recipe_3)
        ingredient_19.save()
        ingredient_20 = Ingredient(amount=0.25, unit="lbs", note="", source=source_9, recipe=recipe_3)
        ingredient_20.save()
        ingredient_21 = Ingredient(amount=0.0, unit="", note="", source=source_21, recipe=recipe_3)
        ingredient_21.save()
        ingredient_22 = Ingredient(amount=1.0, unit="oz", note="", source=source_22, recipe=recipe_3)
        ingredient_22.save()
        ingredient_23 = Ingredient(amount=0.5, unit="oz", note="", source=source_5, recipe=recipe_3)
        ingredient_23.save()

        procedure_1 = Procedure(title="BREWING DAY", tag="Yeast", content="Incubate Yeast ", note="", recipe=recipe_1)
        procedure_1.save()

        procedure_2 = Procedure(title="BREWING DAY", tag="Boil", content="2.5 gallons of Water", note="", recipe=recipe_1)
        procedure_2.save()

        procedure_3 = Procedure(title="BREWING DAY", tag="Mash/Grains", content="Mash for 90 minutes at 153C", note="", recipe=recipe_1)
        procedure_3.save()

        procedure_4 = Procedure(title="BREWING DAY", tag="Hop Boil", content="Add .75oz Hallertau at 45mins", note="", recipe=recipe_1)
        procedure_4.save()

        procedure_5 = Procedure(title="BREWING DAY", tag="Hop Boil 2", content="Add .25oz Hallertau at 15mins", note="remember to still the swirl the grain to help clear the beer", recipe=recipe_1)
        procedure_5.save()

        procedure_6 = Procedure(title="BREWING DAY", tag="Cool Wort", content="Cool Wort to 78C - 100C.", note="", recipe=recipe_1)
        procedure_6.save()

        procedure_7 = Procedure(title="FERMENTATION: (weeks 1-2)", tag="Fermentation", content="Ferment for 10 days at 68F. ", note="", recipe=recipe_1)
        procedure_7.save()

        procedure_8 = Procedure(title="FERMENTATION: (weeks 1-2)", tag="Secondary", content="No secondary fermentation.", note="add 4lbs of peaches to the secondary fermenation", recipe=recipe_1)
        procedure_8.save()

        procedure_9 = Procedure(title="BOTTLING DAY: (2 weeks)", tag="Bottle", content="Mix priming sugar and add to beer before bottling.", note="", recipe=recipe_1)
        procedure_9.save()

        procedure_10 = Procedure(title="BOTTLING DAY: (2 weeks)", tag="Condition", content="Store bottles at room temperature.", note="", recipe=recipe_1)
        procedure_10.save()

        procedure_11 = Procedure(title="DRINK: (2 weeks)", tag="Enjoy", content="Beer ready to serve.", note="", recipe=recipe_1)
        procedure_11.save()

        procedure_12 = Procedure(title="BREWING DAY", tag="Yeast", content="Incubate Yeast ", note="", recipe=recipe_2)
        procedure_12.save()

        procedure_13 = Procedure(title="BREWING DAY", tag="Boil", content="2.5 gallons of Water", note="", recipe=recipe_2)
        procedure_13.save()

        procedure_14 = Procedure(title="BREWING DAY", tag="Mash/Grains", content="Sacch Rest for 60 minutes at 153C", note="", recipe=recipe_2)
        procedure_14.save()

        procedure_15 = Procedure(title="BREWING DAY", tag="Mash/Grains", content="Mashout for 10 minutes at 170", note="", recipe=recipe_2)
        procedure_15.save()

        procedure_16 = Procedure(title="BREWING DAY", tag="Hop Boil", content="Add 0.75 oz Willamette 60 mins", note="", recipe=recipe_2)
        procedure_16.save()

        procedure_17 = Procedure(title="BREWING DAY", tag="Hop Boil 2", content="Add 0.75 oz US Goldings at 30 mins", note="", recipe=recipe_2)
        procedure_17.save()

        procedure_18 = Procedure(title="BREWING DAY", tag="Cool Wort", content="Cool Wort to 78C", note="", recipe=recipe_2)
        procedure_18.save()

        procedure_19 = Procedure(title="FERMENTATION: (weeks 1-2)", tag="Fermentation", content="Ferment for 1-2 weeks at 60-72F ", note="", recipe=recipe_2)
        procedure_19.save()

        procedure_20 = Procedure(title="FERMENTATION: (weeks 1-2)", tag="Secondary", content="Ferment for 2 weeks", note="", recipe=recipe_2)
        procedure_20.save()

        procedure_21 = Procedure(title="BOTTLING DAY: (2 weeks)", tag="Bottle", content="Mix priming sugar and add to beer before bottling.", note="", recipe=recipe_2)
        procedure_21.save()

        procedure_22 = Procedure(title="BOTTLING DAY: (2 weeks)", tag="Condition", content="Store bottles at room temperature.", note="", recipe=recipe_2)
        procedure_22.save()

        procedure_23 = Procedure(title="DRINK: (2 weeks)", tag="Enjoy", content="Beer ready to serve.", note="", recipe=recipe_2)
        procedure_23.save()

        procedure_24 = Procedure(title="BREWING DAY", tag="Yeast", content="Incubate Yeast ", note="", recipe=recipe_3)
        procedure_24.save()

        procedure_25 = Procedure(title="BREWING DAY", tag="Boil", content="2.5 gallons of Water", note="", recipe=recipe_3)
        procedure_25.save()

        procedure_26 = Procedure(title="BREWING DAY", tag="Mash/Grains", content="Sacch Rest for 60 minutes at 154C", note="", recipe=recipe_3)
        procedure_26.save()

        procedure_27 = Procedure(title="BREWING DAY", tag="Mash/Grains", content="Mashout for 10 minutes at 170", note="", recipe=recipe_3)
        procedure_27.save()

        procedure_28 = Procedure(title="BREWING DAY", tag="Hop Boil", content="Add 1.0 oz US Fuggle 60 mins", note="", recipe=recipe_3)
        procedure_28.save()

        procedure_29 = Procedure(title="BREWING DAY", tag="Cool Wort", content="Cool Wort to 78C", note="", recipe=recipe_3)
        procedure_29.save()

        procedure_30 = Procedure(title="FERMENTATION: (weeks 1-2)", tag="Fermentation", content="Ferment for 1 week at 66-74F.", note="", recipe=recipe_3)
        procedure_30.save()

        procedure_31 = Procedure(title="FERMENTATION: (weeks 1-2)", tag="Secondary", content="Ferment for 1 week", note="", recipe=recipe_3)
        procedure_31.save()

        procedure_32 = Procedure(title="BOTTLING DAY: (2 weeks)", tag="Bottle", content="Mix priming sugar and add to beer before bottling.", note="", recipe=recipe_3)
        procedure_32.save()

        procedure_33 = Procedure(title="BOTTLING DAY: (2 weeks)", tag="Condition", content="Store bottles at room temperature.", note="", recipe=recipe_3)
        procedure_33.save()

        procedure_34 = Procedure(title="DRINK: (2 weeks)", tag="Enjoy", content="Beer ready to serve.", note="", recipe=recipe_3)
        procedure_34.save()

        return user


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Your Username'
        }))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Your Password'
        }))

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.user = None
        for key, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean(self):
        self.user = authenticate(
            username=self.cleaned_data.get('username', None),
            password=self.cleaned_data.get('password', None),
        )
        if self.user and self.user.is_active:
            return self.user
        else:
            self._errors['login'] = "Login fails, username and password do not match"
            forms.ValidationError("Login Error")

    def save(self):
        return self.user
