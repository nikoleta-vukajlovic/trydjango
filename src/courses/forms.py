from .models import Course
from django import forms


class CourseModelForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title']

    # samo na nivou forme, nema veze sa bazom
    def clean_title(self):
        title = self.cleaned_data.get("title")
        if title.lower() == "abc":
            raise forms.ValidationError("Not valid title")
        return title
