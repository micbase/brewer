from django import forms
from brewer.models import Source, Recipe, Ingredient, Procedure

class RecipeForm(forms.Form):
    def save(self):
        recipe = Recipe.objects.get(pk=self.recipe_id)
        recipe.note = self.cleaned_data['note']
        recipe.save()
        return recipe

    class Meta:
        model = Recipe
        exclude = ['name','inote','created','changed']
        widgets = {
                'note': forms.Textarea(attrs={
                    'class':'form-control',
                    'placeholder':'Enter Comments'
                    })
                }

class IngredientForm(forms.Form):
    def save(self):
        ingredient = Ingredient.objects.get(pk=self.recipe_id)
        ingredient.note = self.cleaned_data['note']
        ingredient.save()
        return ingredient

    class Meta:
        model = Ingredient
        exclude = ['recipe', 'source', 'amount', 'unit', 'created', 'changed']
        widgets = {
                'note': forms.TextInput(attrs={
                    'class':'form-control',
                    'placeholder':'Enter Comments'
                    })
                }

class ProcedureForm(forms.Form):
    def save(self):
        procedure = Procedure.objects.get(pk=self.recipe_id)
        procedure.note = self.cleaned_data['note']
        procedure.save()
        return procedure

    class Meta:
        model = Procedure
        exclude = ['title', 'tag', 'content', 'created', 'changed']
        widgets = {
                'note': forms.TextInput(attrs={
                    'class':'form-control',
                    'placeholder':'Enter Comments'
                    })
                }
"""
class CreateTopicForm(forms.ModelForm):

    def __init__(self, course, author, *args, **kwargs):
        super(CreateTopicForm, self).__init__(*args, **kwargs)
        self.instance.course = course
        self.instance.author = author

    class Meta:
        model = Topic
        exclude = ['author', 'course', 'status']
        widgets = {
                'title': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Topic Title'
                    }),
                'content': forms.Textarea(attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Topic Content'
                    })
                }"""
