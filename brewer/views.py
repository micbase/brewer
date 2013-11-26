import json

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import (
    FormView,
    ListView,
    TemplateView,
)

from auth.views import LoginRequiredMixin
from brewer.forms import (
    CreateRecipeForm,
    IngredientForm,
    ProcedureForm,
    RecipeForm,
)

from brewer.models import (
    Ingredient,
    Procedure,
    Recipe,
)


class RecipeListView(LoginRequiredMixin, ListView):
    template_name = 'brewer/recipes.html'
    paginate_by = 20

    def get_queryset(self):
        user = self.request.user
        recipe_name = self.request.GET.get("recipe_name", "")
        return Recipe.objects.filter(
            name__icontains=recipe_name,
            brewer=user,
            status=1
        )

    def get_context_data(self, **kwargs):
        context = super(RecipeListView, self).get_context_data(**kwargs)
        context['recipe_name'] = self.request.GET.get("recipe_name", "")
        return context


class JSONResponseMixin(object):
    def render_to_response(self, context):
        "Returns a JSON response containing 'context' as payload"
        return self.get_json_response(self.convert_context_to_json(context))

    def get_json_response(self, content, **httpresponse_kwargs):
        "Construct an `HttpResponse` object."
        return HttpResponse(content,
                                 content_type='application/json',
                                 **httpresponse_kwargs)

    def convert_context_to_json(self, context):
        "Convert the context dictionary into a JSON object"
        # Note: This is *EXTREMELY* naive; in reality, you'll need
        # to do much more complex handling to ensure that arbitrary
        # objects -- such as Django model instances or querysets
        # -- can be serialized as JSON.
        return json.dumps(context)


class RecipeView(LoginRequiredMixin, TemplateView):
    template_name = 'brewer/recipe.html'

    def get_recipe(self):
        recipe_id = self.kwargs['recipe_id']
        return get_object_or_404(Recipe, brewer=self.request.user, pk=recipe_id)

    def get_ingredient(self):
        recipe_id = self.kwargs['recipe_id']
        return Ingredient.objects.filter(recipe_id=recipe_id)

    def get_procedure(self):
        recipe_id = self.kwargs['recipe_id']
        return Procedure.objects.filter(recipe_id=recipe_id).order_by('id')

    def get_context_data(self, **kwargs):
        context = super(RecipeView, self).get_context_data(**kwargs)
        context['recipe'] = self.get_recipe()
        context['ingredient'] = self.get_ingredient()
        context['procedure'] = self.get_procedure()
        return context


class RecipeNoteView(LoginRequiredMixin, JSONResponseMixin, FormView):
    form_class = RecipeForm

    def form_valid(self, form):
        form.save()
        return self.render_to_response({'success': True})

    def get_recipe(self):
        recipe_id = self.kwargs['recipe_id']
        return get_object_or_404(Recipe, brewer=self.request.user, pk=recipe_id)

    def get_note(self):
        recipe = self.get_recipe()
        return recipe.note

    def get_form_kwargs(self):
        kwargs = super(RecipeNoteView, self).get_form_kwargs()
        kwargs['recipe_id'] = self.kwargs['recipe_id']
        return kwargs

    def get_context_data(self, **kwargs):
        context = {}
        context['note'] = self.get_note()
        return context


class IngredientNoteView(LoginRequiredMixin, JSONResponseMixin, FormView):
    form_class = IngredientForm

    def form_valid(self, form):
        form.save()
        return self.render_to_response({'success': True})

    def get_ingredient(self):
        ingredient_id = self.kwargs['ingredient_id']
        return get_object_or_404(Ingredient, pk=ingredient_id)

    def get_note(self):
        ingredient = self.get_ingredient()
        return ingredient.note

    def get_form_kwargs(self):
        kwargs = super(IngredientNoteView, self).get_form_kwargs()
        kwargs['ingredient_id'] = self.kwargs['ingredient_id']
        return kwargs

    def get_context_data(self, **kwargs):
        context = {}
        context['note'] = self.get_note()
        return context


class ProcedureNoteView(LoginRequiredMixin, JSONResponseMixin, FormView):
    form_class = ProcedureForm

    def form_valid(self, form):
        form.save()
        return self.render_to_response({'success': True})

    def get_procedure(self):
        procedure_id = self.kwargs['procedure_id']
        return get_object_or_404(Procedure, pk=procedure_id)

    def get_note(self):
        procedure = self.get_procedure()
        return procedure.note

    def get_form_kwargs(self):
        kwargs = super(ProcedureNoteView, self).get_form_kwargs()
        kwargs['procedure_id'] = self.kwargs['procedure_id']
        return kwargs

    def get_context_data(self, **kwargs):
        context = {}
        context['note'] = self.get_note()
        return context


class CreateRecipeView(LoginRequiredMixin, FormView):
    template_name = 'brewer/create_recipe.html'
    form_class = CreateRecipeForm

    def get_form_kwargs(self):
        kwargs = super(CreateRecipeView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        kwargs['recipe_id'] = 0
        return kwargs

    def form_valid(self, form):
        recipe_id = form.save()
        json_data = json.dumps({
            'success': True,
            'redirect': '/recipe/' + str(recipe_id)
        })
        return HttpResponse(
            json_data,
            content_type='application/json',
        )

    def get_success_url(self):
        return '/recipe/' + str(self.recipe_id)


class EditRecipeView(LoginRequiredMixin, FormView):
    template_name = 'brewer/edit_recipe.html'
    form_class = CreateRecipeForm

    def get_recipe(self):
        recipe_id = self.kwargs['recipe_id']
        return get_object_or_404(Recipe, brewer=self.request.user, pk=recipe_id)

    def get_ingredient(self):
        recipe_id = self.kwargs['recipe_id']
        ingredients = Ingredient.objects.filter(recipe_id=recipe_id).order_by('id')
        return (ingredients, ingredients[len(ingredients) - 1].id + 1)

    def get_procedure(self):
        recipe_id = self.kwargs['recipe_id']
        procedures = Procedure.objects.filter(recipe_id=recipe_id).order_by('id')
        return (procedures, procedures[len(procedures) - 1].id + 1)

    def get_form_kwargs(self):
        kwargs = super(EditRecipeView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        kwargs['recipe_id'] = self.kwargs['recipe_id']
        return kwargs

    def form_valid(self, form):
        recipe_id = form.save()
        json_data = json.dumps({
            'success': True,
            'redirect': '/recipe/' + str(recipe_id),
            'Del_redirect': '/'            
        })
        return HttpResponse(
            json_data,
            content_type='application/json',
        )

    def get_success_url(self):
        return '/recipe/' + str(self.recipe_id)

    def get_context_data(self, **kwargs):
        context = super(EditRecipeView, self).get_context_data(**kwargs)
        context['recipe'] = self.get_recipe()
        context['ingredients'], context['ingredient_index'] = self.get_ingredient()
        context['procedures'], context['procedure_index'] = self.get_procedure()
        return context
