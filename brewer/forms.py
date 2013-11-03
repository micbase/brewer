from django import forms
from brewer.models import Topic


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
                }
