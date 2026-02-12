from django import forms

spisok_film_words = [
    "doolot", "наркотики"
]

class CreateFilmForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField()
    image = forms.ImageField()
    year = forms.IntegerField()


    def clean (self):
        data = self.cleaned_data
        name = data.get('name')
        if name in spisok_film_words:
            raise forms.ValidationError("Это слово запрещено")
        return data
