from django.shortcuts import render
from django.contrib.auth import login, authenticate,logout
from . import forms
from market.models import Service, Servicecategorie
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect, render
from pyexpat.errors import messages
from django.contrib import messages
from .forms import AdresseForm, ServiceCategorieForm, ServiceForm
from .models import Adresse, Service,Servicecategorie
# Create your views here.
def home(request):
    return render(request,'market/home.html')
#
def services(request):
    services_marketing=Service.objects.filter(service__nom_service='Marketing digital')
    services_web=Service.objects.filter(service__nom_service='Developpement web & mobile')
    context={
        'services_marketing':services_marketing,
        'services_web':services_web,
    }
    return render(request,'market/services.html',context)
#
def contact(request):
    return render(request,'market/contact.html')

########
@login_required
def service_delete(request, slug=None):
    service = get_object_or_404(Service, slug=slug)
    
    if request.method == 'POST':
        service.delete()
        messages.success(request, " L\'service a été supprimé avec succès.")

        return redirect('market:dashboard')
        
    # Optionally, you can render a confirmation page here if not using a modal
        # return render(request,'market/admin/admin.html')

    return redirect('market:dashboard')
#
def add_service(request):
    if request.method == 'POST':
        # Initialize the form with POST data and files
        form = forms.ServiceForm(request.POST, request.FILES)
        
        if form.is_valid():
            # Save the main product instance without committing yet
            service = form.save(commit=False)
            service.user = request.user  # Assign the current user
            
            # Save the product instance to the database
            service.save()  # Save product first

          
            
            messages.success(request, " L\'service a été enregistré avec succès.")
            return redirect('market:dashboard')
        else:
            messages.error(request, "Erreur lors de l\'enregistrement de l\'service Veuillez vérifier les informations.")
    else:
        form = ServiceForm()

    return render(request, 'market/admin/service/add_service.html', {'form': form})
##


@login_required
def service_update(request, slug=None):
    service = get_object_or_404(Service, slug=slug)
    
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES, instance=service)
        if form.is_valid():
            # Sauvegarde du produit, y compris la photo si un nouveau fichier est téléchargé
            service = form.save(commit=False)
            service.user = request.user  # Assign the current user
            
            # Save the product instance to the database
            service.save()  # Save product first

            messages.success(request, " L\'service a été mis à jour avec succès.")
            return redirect('market:dashboard')
        else:
            # Ajout de messages d'erreur spécifiques pour le formulaire
            messages.error(request, 'Une erreur s\'est produite. Veuillez vérifier les informations saisies.')
    else:
        form = ServiceForm(instance=service)

    return render(request, 'market/admin/service/service_update.html', {'form': form})
######################ARTICLE CATEGORIE

def service_categorie(request):
    categorie_service=Servicecategorie.objects.all()
    nombre_categorie_service=categorie_service.count()
    #
    service=Service.objects.all()
    nombre_service=service.count()

    context={
        'service':service,
        'categorie_service':categorie_service,
        'nombre_service':nombre_service,
        'nombre_categorie_service':nombre_categorie_service
    }
    return render(request,'market/admin/service/service_categorie.html',context)
#


    return context
@login_required
def add_categorie_service(request):
    if request.method == 'POST':
        # Initialize the form with POST data and files
        form = ServiceCategorieForm(request.POST)
        
        if form.is_valid():
            # Save the main product instance without committing yet
            categorie_service = form.save(commit=False)
            categorie_service.user = request.user  # Assign the current user
            
            # Save the product instance to the database
            categorie_service.save()  # Save product first

          
            
            messages.success(request, " Le service a été enregistré avec succès.")
            return redirect('market:service')
        else:
            messages.error(request, "Erreur lors de l\'enregistrement du service Veuillez vérifier les informations.")
    else:
        form = ServiceCategorieForm()

    return render(request, 'market/admin/service/add_categorie.html', {'form': form})    
##

@login_required
def categorie_service_delete(request, slug=None):
    service = get_object_or_404(Servicecategorie, slug=slug)
    
    if request.method == 'POST':
        service.delete()
        messages.success(request, " La categorie a été supprimé avec succès.")

        return redirect('market:service')
        
    # Optionally, you can render a confirmation page here if not using a modal
        # return render(request,'market/admin/admin.html')

    return redirect('market:service')
#

@login_required
def categorie_service_update(request, slug=None):
    categorie_service = get_object_or_404(Servicecategorie, slug=slug)
    print("okk")
    if request.method == 'POST':
        form = ServiceCategorieForm(request.POST, request.FILES, instance=categorie_service)
        if form.is_valid():
            # Sauvegarde du produit, y compris la photo si un nouveau fichier est téléchargé
            categorie_service = form.save(commit=False)
            categorie_service.user = request.user  # Assign the current user
            
            # Save the product instance to the database
            categorie_service.save()  # Save product first

            messages.success(request, " L\'service a été mis à jour avec succès.")
            return redirect('market:service')
        else:
            # Ajout de messages d'erreur spécifiques pour le formulaire
            messages.error(request, 'Une erreur s\'est produite. Veuillez vérifier les informations saisies.')
    else:
        form = ServiceCategorieForm(instance=categorie_service)

    return render(request, 'market/admin/service/update_categorie_service.html', {'form': form})
#
def dashboard_admin(request):
    services=Service.objects.all().order_by('-date_ajout')
    address=Adresse.objects.all()
    context={
        'service':services,
        'addresses':address
    }
    return render(request,'market/admin/admin.html',context)
####
def detail(request, service_slug):
    # Récupérer le produit spécifique par son ID
    service = get_object_or_404(Service, slug=service_slug)
    service_categorie=service.service
    print("ssss",service_categorie)
    # Récupérer les produits similaires de la même catégorie, en excluant le produit actuel
    similar_services = Service.objects.filter(service=service_categorie).exclude(slug=service_slug)
    print("cccc",similar_services)
    # Récupérer les avis associés au produit
    # reviews = comments.reviews.all()  # Utilise related_name dans Review model
    
    # Récupérer les catégories pour la navigation
    # categories = Category.objects.all().prefetch_related('souscategories')
    # #produit variant associes a ce produit
    # produit_variant=ProductVariant.objects.filter(product=product_id)
    context = {
        'service': service,               # Passer le produit au contexte du template
        'similar_services': similar_services,
        # 'categories': categories,
        # 'reviews': reviews,      
        # 'produit_variant':produit_variant,
            
    }
    return render(request, 'market/detail.html', context)
###################################
def user_addresses(request):
    # Fetch the addresses for the logged-in user
    addresses = Adresse.objects.filter(utilisateur=request.user)
    return render(request, 'user_addresses.html', {'addresses': addresses})

@login_required
def update_address(request,pk):
    address = get_object_or_404(Adresse, pk=pk, utilisateur=request.user)
    if request.method == 'POST':
        form = AdresseForm(request.POST, instance=address)
        if form.is_valid():
            form.save()
            messages.success(request, 'L\'adresse a été mis à jour avec succès.')

            return redirect('market:dashboard')
    else:
        form = AdresseForm(instance=address)
    return render(request, 'market/admin/service/adresse_update.html', {'form': form})

####################
@login_required
def delete_address(request, pk):
    address = get_object_or_404(Adresse, pk=pk, utilisateur=request.user)
    if request.method == 'POST':
        address.delete()
        messages.success(request, 'L\adresse a été supprime avec succès.')

        return redirect('market:dashboard')
    return render(request, 'confirm_delete.html', {'address': address})

def adresse_create(request):
    print("adresse_create appelée")  # Vérifiez dans la console

    if request.method == 'POST':
        form = AdresseForm(request.POST)
        if form.is_valid():
            adresse = form.save(commit=False)
            adresse.utilisateur = request.user
            adresse.save()
            messages.success(request, 'L\'adresse a été mis à jour avec succès.')

            return redirect('market:dashboard')  # Redirect to a success page or list of addresses
    else:
        form = AdresseForm()
    
    context = {
        'form': form,
    }
    return render(request, 'market/admin/service/adresse_form.html', context)