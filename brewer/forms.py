from django import forms
from brewer.models import Recipe, Ingredient, Procedure, Source


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

    def __init__(self, ingredient_id, *args, **kwargs):
        super(IngredientForm, self).__init__(*args, **kwargs)
        self.ingredient_id = ingredient_id

    def save(self):
        ingredient = Ingredient.objects.get(pk=self.ingredient_id)
        ingredient.note = self.cleaned_data['note']
        ingredient.save()
        return ingredient


class ProcedureForm(forms.Form):
    note = forms.CharField()

    def __init__(self, procedure_id, *args, **kwargs):
        super(ProcedureForm, self).__init__(*args, **kwargs)
        self.procedure_id = procedure_id

    def save(self):
        procedure = Procedure.objects.get(pk=self.procedure_id)
        procedure.note = self.cleaned_data['note']
        procedure.save()
        return procedure


class CreateRecipeForm(forms.Form):
    recipe_name = forms.CharField(required=True)
    source_name = forms.CharField(required=True)
    source_variety = forms.CharField(required=True)
    amount = forms.CharField(required=True)
    unit = forms.CharField(required=True)
    procedure_title = forms.CharField(required=True)
    procedure_tag = forms.CharField(required=True)
    procedure_content = forms.CharField(required=True)

    def __init__(self, user, *args, **kwargs):
        super(CreateRecipeForm, self).__init__(*args, **kwargs)
        self.user = user

    def clean_source_variety(self):
        source_variety = self.cleaned_data['source_variety']
        return source_variety.split(',')

    def clean_source_name(self):
        source_name = self.cleaned_data['source_name']
        return source_name.split(',')

    def clean_amount(self):
        amount = self.cleaned_data['amount']
        return amount.split(',')

    def clean_unit(self):
        unit = self.cleaned_data['unit']
        return unit.split(',')

    def clean_procedure_title(self):
        procedure_title = self.cleaned_data['procedure_title']
        return procedure_title.split(',')

    def clean_procedure_tag(self):
        procedure_tag = self.cleaned_data['procedure_tag']
        return procedure_tag.split(',')

    def clean_procedure_content(self):
        procedure_content = self.cleaned_data['procedure_content']
        return procedure_content.split(',')

    def clean(self):
        try:
            a = len(self.cleaned_data['source_name'])
            b = len(self.cleaned_data['source_variety'])
            c = len(self.cleaned_data['amount'])
            d = len(self.cleaned_data['unit'])
            e = len(self.cleaned_data['procedure_title'])
            f = len(self.cleaned_data['procedure_tag'])
            g = len(self.cleaned_data['procedure_content'])
        except KeyError:
            return forms.ValidationError('error')

        if a != b or a != c or a != d:
            return forms.ValidationError('error')
        if e != f or e != g:
            return forms.ValidationError('error')

        return self.cleaned_data

    def save(self):
        recipe_name = self.cleaned_data['recipe_name']
        source_name = self.cleaned_data['source_name']
        source_variety = self.cleaned_data['source_variety']
        ingredient_amount = self.cleaned_data['amount']
        ingredient_unit = self.cleaned_data['unit']
        procedure_title = self.cleaned_data['procedure_title']
        procedure_tag = self.cleaned_data['procedure_tag']
        procedure_content = self.cleaned_data['procedure_content']

        new_recipe = Recipe(
            name=recipe_name,
            brewer=self.user,
        )
        new_recipe.save()

        for i in range(len(source_name)):
            new_source, created = Source.objects.get_or_create(
                            variety=source_variety[i],
                            name=source_name[i]
                            )
            new_source.save()

            new_ingredient = Ingredient(
                                recipe=new_recipe,
                                source=new_source,
                                amount=ingredient_amount[i],
                                unit=ingredient_unit[i],
                                )
            new_ingredient.save()

        for i in range(len(procedure_title)):
            new_procedure = Procedure(
                                recipe=new_recipe,
                                title=procedure_title[i],
                                tag=procedure_tag[i],
                                content=procedure_content[i],
                                )
            new_procedure.save()

        return new_recipe.id
