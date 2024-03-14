from django.forms import ModelForm
from cats.models import Cat

class CatForm(ModelForm):
    class Meta:
        model = Cat
        fields = ["name", "age", "legs"]
        