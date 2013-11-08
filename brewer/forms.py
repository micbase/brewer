from django import forms
from brewer.models import Source, Recipe, Ingredient, Procedure

class RecipeForm(forms.Form):
    note = forms.CharField()

    def __init__(self, recipe_id, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        self.recipe_id = recipe_id

    def save(self):
        recipe = Recipe.objects.get(pk=self.recipe_id)
        recipe.note = self.cleaned_data['note']
        recipe.save()
        return recipe


class IngredientForm(forms.Form):
    note = forms.CharField()

    def save(self):
        ingredient = Ingredient.objects.get(pk=self.recipe_id)
        ingredient.note = self.cleaned_data['note']
        ingredient.save()
        return ingredient


class ProcedureForm(forms.Form):
    note = forms.CharField()

    def save(self):
        procedure = Procedure.objects.get(pk=self.recipe_id)
        procedure.note = self.cleaned_data['note']
        procedure.save()
        return procedure
