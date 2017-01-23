from django import forms
from .models import Post

class Exit_Survey_Form(forms.ModelForm):

    class Meta:
        model = users
        fields = (*)

        if request.method == "POST":
            form = Exit_Survey_Form(request.POST, instance=post)
            if form.is_valid():
