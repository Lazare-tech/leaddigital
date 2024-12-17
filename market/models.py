from django.conf import settings
from django.db import models
import secrets
import string

# Create your models here.
from django.db import models
from django.utils.text import slugify
from phonenumber_field.modelfields import PhoneNumberField
# Modèle pour les catégories d'articles
class Servicecategorie(models.Model):
    nom_service = models.CharField(max_length=255, verbose_name="Nom du service")
    slug = models.SlugField(unique=True, max_length=255, blank=True)
    
    class Meta:
        verbose_name= "Categorie du service"
        verbose_name_plural= "Categories du service"
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.generate_unique_slug()
        super().save(*args, **kwargs)

    def generate_unique_slug(self):
        slug = slugify(self.nom_service)
        unique_slug = slug
        num = 1
        while Servicecategorie.objects.filter(slug=unique_slug).exists():
            unique_slug = f'{slug}-{num}'
            num += 1
        return unique_slug
    
    def __str__(self):
        return self.nom_service
# Modèle pour les articles individuels
class Service(models.Model):
    service = models.ForeignKey(Servicecategorie, related_name='services', verbose_name="Service", on_delete=models.CASCADE)
    titre = models.CharField(max_length=255, verbose_name="Titre du service", null=True)
    contenu=models.TextField(verbose_name='contenu')
    photo = models.ImageField(upload_to='service_image', verbose_name="Image du service", null=True, blank=True)
    date_ajout = models.DateTimeField(verbose_name="Date ajout du service", auto_now=True)

    slug = models.SlugField(unique=True, max_length=255, blank=True)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.generate_unique_slug()
        super().save(*args, **kwargs)

    def generate_unique_slug(self):
        slug = slugify(self.titre)
        unique_slug = slug
        num = 1
        while Service.objects.filter(slug=unique_slug).exists():
            unique_slug = f'{slug}-{num}'
            num += 1
        return unique_slug
    
    def __str__(self):
        return self.titre
#

class Adresse(models.Model):
    ville = models.CharField(max_length=40, verbose_name='ville', null=True, blank=True)
    # slug = models.SlugField(unique=True, max_length=255, blank=True)
    pays = models.CharField(max_length=40, verbose_name='Pays', null=True, blank=True)
    quartier = models.CharField(max_length=40, verbose_name='Quartier ou secteur du vendeur', null=True, blank=True)
    repere = models.CharField(max_length=40, verbose_name='Point de référence du vendeur', null=True, blank=True)
    contact = PhoneNumberField(verbose_name='Numéro de téléphone')
    utilisateur = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Utilisateur',
        related_name='adresses'
    )

    def __str__(self):
        return f"{self.ville}, {self.quartier}, {self.repere} - {self.utilisateur.username}"

    # def generate_unique_slug(self):
    #     characters = string.ascii_letters + string.digits
    #     unique_slug = ''.join(secrets.choice(characters) for _ in range(8))  # Exemple : 'aB3dE9Fg'
    #     while Adresse.objects.filter(slug=unique_slug).exists():
    #         unique_slug = ''.join(secrets.choice(characters) for _ in range(8))
    #     return unique_slug

    # def save(self, *args, **kwargs):
    #     if not self.slug:  # Génère un slug uniquement si le champ est vide
    #         self.slug = self.generate_unique_slug()
    #     super().save(*args, **kwargs)
