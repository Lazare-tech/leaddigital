from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from phonenumber_field.formfields import PhoneNumberField
from market.models import Adresse, Service, Servicecategorie  # Pour utiliser le modèle d'utilisateur personnalisé
#####
class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['photo', 'titre', 'service', 'contenu']
        widgets = {
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'titre': forms.TextInput(attrs={'class': 'form-control'}),
            'contenu': forms.Textarea(attrs={'class': 'form-control'}),
                        

            'service': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_nom(self):
        titre = self.cleaned_data.get('titre')
        if len(titre) > 40:
            raise forms.ValidationError("Le titre du service ne peut pas dépasser 40 caractères.")
        return titre
    
#####
       
class ServiceCategorieForm(forms.ModelForm):
    # Define the field for secondary images correctly

    class Meta:
        model = Servicecategorie
        fields = ['nom_service']
        widgets = {
            'nom_service': forms.TextInput(attrs={'class': 'form-control'}),
           

          
        }
    def clean_nom(self):
        nom_service = self.cleaned_data.get('nom_service')
        if len(nom_service) > 40:
            raise forms.ValidationError("Le nom ne peut pas dépasser 40 caractères.")
        return nom_service
    #############
    
class AdresseForm(forms.ModelForm):
    contact = PhoneNumberField()

    class Meta:
        model = Adresse
        fields = ['pays','ville', 'quartier', 'repere', 'contact']
        
        widgets = {
                        'pays': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez le pays'}),

            'ville': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez la ville'}),
            'quartier': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez le quartier'}),
            'repere': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez le point de référence'}),
            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez le numéro de téléphone'}),
        }
    
    def clean_contact(self):
        contact = self.cleaned_data.get('contact')
        # Ensure contact is valid
        if not contact:
            raise forms.ValidationError("Le numéro de téléphone est requis.")
        return contact
    
    def clean_ville(self):
        ville = self.cleaned_data.get('ville')
        # Ensure ville is not empty
        if not ville:
            raise forms.ValidationError("La ville est requise.")
        return ville
    
    def clean_quartier(self):
        quartier = self.cleaned_data.get('quartier')
        # Ensure quartier is not empty
        if not quartier:
            raise forms.ValidationError("Le quartier est requis.")
        return quartier
    
    def clean_repere(self):
        repere = self.cleaned_data.get('repere')
        # Ensure repere is not empty
        if not repere:
            raise forms.ValidationError("Le point de référence est requis.")
        return repere
    
   