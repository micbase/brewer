
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.views.generic import (
    CreateView,
    ListView,
    TemplateView,
    FormView,
)

from auth.views import LoginRequiredMixin
import brewer as brewer_constants
from brewer.forms import (
       # CreateTopicForm,
        RecipeForm,
        IngredientForm,
        ProcedureForm,
)

from brewer.models import (
   # Course,
    #CourseSchedule,
   # Membership,
   # Post,
   # Topic,

    Recipe,
    Ingredient,
    Procedure,
    Source,
)
"""
class CourseView(ListView):
    template_name = 'brewer/courses.html'
    paginate_by = 20

    def get_queryset(self):
        course_name = self.request.GET.get("course_name", "")
        return Course.objects.filter(
            name__icontains=course_name,
        )

    def get_context_data(self, **kwargs):
        context = super(CourseView, self).get_context_data(**kwargs)
        context['course_name'] = self.request.GET.get("course_name", "")
        return context


class UserProfileView(LoginRequiredMixin, ListView):
    template_name = 'brewer/user_profile.html'
    paginate_by = 20

    def get_queryset(self):
        users = self.request.user
        return Course.objects.filter(
            students=users
        )

    def get_membership(self):
        users = self.request.user
        return Membership.objects.filter(
            member=users
        )

class CreateTopicView(LoginRequiredMixin, CreateView):
    template_name = 'brewer/create_topic.html'
    model = Topic
    form_class = CreateTopicForm

    def get_success_url(self):
        return '/topics/' + self.kwargs['course_id']

    def get_form_kwargs(self):
        kwargs = super(CreateTopicView, self).get_form_kwargs()
        course_id = self.kwargs['course_id']
        kwargs['course'] = get_object_or_404(Course, pk=course_id)
        kwargs['author'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(CreateTopicView, self).get_context_data(**kwargs)
        context['course_id'] = self.kwargs['course_id']
        return context"""

class RepcipeView(TemplateView):
    template_name = 'brewer/recipe.html'

    def get_context_data(self, **kwargs):
        context = super(RecipeView, self).get_context_data(**kwargs)
        context['recipe_id'] = self.kwargs['recipe_id']
        return context

class RecipeNoteView(FormView):
    template_name = 'brewer/recipe.html'
    form_class = RecipeForm
    ##ingredient_form_class = IngredientForm
    ##procedure_form_class = ProcedureForm

    def get_recipe(self):
        recipe_id = self.kwargs['recipe_id']
        return get_object_or_404(Recipe, pk=recipe_id)

    def get_note(self):
        recipe = self.get_recipe()
        return recipe.note

    def get_success_url(self):
        return '/recipe/' + self.kwargs['recipe_id']

    def get_form_kwargs(self):
        kwargs = super(RecipeView, self).get_form_kwargs()
        kwargs['recipe_id'] = self.kwargs['recipe_id']
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(RecipeView, self).get_context_data(**kwargs)
        #context['course'] = self.get_course()
        #context['course_joined'] = self.is_course_joined()
        context['recipe'] = Recipe.objects.get(pk=self.kwargs['recipe_id'])
        context['note'] = self.get_note()
       # context['ingredient'] = Ingredient.objects.get(pk=self.kwargs['recipe_id'])
       # context['procedure'] = Procedure.objects.get(pk=self.kwargs['recipe_id'])
        return context

class IngredientNoteView(FormView):
    template_name = 'brewer/recipe.html'
    form_class = IngredientForm

    def get_ingredient(self):
        ingredient_id = self.kwargs['ingredient_id']
        return get_object_or_404(Ingredient, pk=ingredient_id)

    def get_note(self):
        ingredient = self.get_ingredient()
        return ingredient.note

    def get_success_url(self):
        return '/recipe/' + self.kwargs['recipe_id']

    def get_form_kwargs(self):
        kwargs = super(IngredientView, self).get_form_kwargs()
        kwargs['ingredient_id'] = self.kwargs['ingredient_id']
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(IngredientView, self).get_context_data(**kwargs)
        context['ingredient'] = Ingredient.objects.get(pk=self.kwargs['ingredient_id'])
        context['note'] = self.get_note()
        return context

class ProcedureNoteView(FormView):
    template_name = 'brewer/recipe.html'
    form_class = ProcedureForm

    def get_procedure(self):
        procedure_id = self.kwargs['procedure_id']
        return get_object_or_404(Procedure, pk=procedure_id)

    def get_note(self):
        procedure = self.get_procedure()
        return procedure.note

    def get_success_url(self):
        return '/recipe/' + self.kwargs['recipe_id']

    def get_form_kwargs(self):
        kwargs = super(IngredientView, self).get_form_kwargs()
        kwargs['procedure_id'] = self.kwargs['procedure_id']
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(ProcedureView, self).get_context_data(**kwargs)
        context['procedure'] = Procedure.objects.get(pk=self.kwargs['procedure_id'])
        context['note'] = self.get_note()
        return context
