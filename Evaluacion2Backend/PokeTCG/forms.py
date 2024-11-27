from django import forms 
from .models import Card, Pokemon, Expansion, Element
from datetime import date


#CARTAS#
class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ('pokemon','element','HP','expansion')
    #VALIDACIONES#
    def clean_pokemon(self):
        pokemon = self.cleaned_data.get('pokemon')
        if not pokemon:
            raise forms.ValidationError("El campo Pokemon está vacío")
        if len(pokemon) <3:
            raise forms.ValidationError("El nombre del pokemon debe tener al menos 3 caracteres")
        return pokemon
    def clean_element(self):
        element = self.cleaned_data.get('element')
        if not element:
            raise forms.ValidationError("El campo Elemento está vacío")
        if len(element) <4:
            raise forms.ValidationError("El elemento debe tener al menos 4 caracteres")
        return element
    def clean_expansion(self):
        expansion = self.cleaned_data.get('expansion')
        if not expansion:
            raise forms.ValidationError("El campo Expansión está vacio")
        if len(expansion) < 2:
            raise forms.ValidationError("La expansión debe tener al menos 2 caracteres")
        return expansion
    def clean_HP(self):
        HP = self.cleaned_data.get('HP')
        if HP is not None: 
            if HP < 10:
                raise forms.ValidationError("El HP debe ser al menos 10")
            if HP > 340:
                raise forms.ValidationError("El HP no puede ser mayor de 340")
            if HP % 10 != 0:
                raise forms.ValidationError("El HP debe ser un múltiplo de 10")
        return HP

#POKEMON#
class PokeForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = ('name','element','skill')
    #VALIDACIONES#
    def clean_element(self):
        element = self.cleaned_data.get('element')
        if not element:
            raise forms.ValidationError("El campo Elemento está vacío")
        if len(element) <4:
            raise forms.ValidationError("El elemento debe tener al menos 4 caracteres")
        return element
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError("El nombre es obligatorio")
        if len(name) <3:
            raise forms.ValidationError("El nombre debe tener al menos 3 caracteres")
        return name
    def clean_skill(self):
        skill = self.cleaned_data.get('skill')
        if not skill:
            raise forms.ValidationError("El campo Habilidad es Obligatorio")
        if len(skill) > 50:
            raise forms.ValidationError("La habilidad no puede tener mas de 50 caracteres")
        return skill


#EXPANSIONES#
class ExpanForm(forms.ModelForm):
    class Meta:
        model = Expansion
        fields = ('name','release_date')
        widgets = {
            'release_date':forms.DateInput(attrs={'type':'date'})
        }
    #VALIDACIONES#
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError("El nombre es obligatorio")
        if len(name) <2:
            raise forms.ValidationError("El nombre debe tener al menos 2 caracteres")
        return name
    def clean_release_date(self):
        release_date = self.cleaned_data.get('release_date')
        if not release_date:
            raise forms.ValidationError("La fecha de lanzamiento es obligatoria.")
        if release_date > date.today():
            raise forms.ValidationError("La fecha de lanzamiento no puede ser una fecha futura -_-")
        return release_date



#ELEMENTOS#
class ElementForm(forms.ModelForm):
    class Meta:
        model = Element
        fields = ('name','effectiveness','weakness')
    #VALIDACIONES#
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError("El nombre es obligatorio.")
        if len(name) < 4:
            raise forms.ValidationError("El nombre debe tener al menos 4 caracteres")
        return name
    def clean_effectiveness(self):
        effectiveness = self.cleaned_data.get('effectiveness')
        if not effectiveness:
            raise forms.ValidationError("El campo Efectividad es obligatorio")
        if len(effectiveness) < 4:
            raise forms.ValidationError("El campo debe tener al menos 4 caracteres")
        return effectiveness
    def clean_weakness(self):
        weakness = self.cleaned_data.get('weakness')
        if not weakness:
            raise forms.ValidationError("El campo Debilidad es obligatorio")
        if len(weakness) < 4:
            raise forms.ValidationError("El campo debe tener al menos 4 caracteres")
        return weakness