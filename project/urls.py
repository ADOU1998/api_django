from django.contrib import admin
from django.urls import path, include
from rest_framework import routers # Importation du router
# from shop.models import Product

from shop.views import CategoryViewset, ProductViewset, ArticleViewset

# Ici nous créons notre retour
router = routers.SimpleRouter()
# Puis lui déclarons une url basée sur le mot clé ‘category’ et notre view
# afin que l’url générée soit celle que nous souhaitons ‘/api/category/’
router.register('category', CategoryViewset, basename='category')
router.register('product', ProductViewset, basename='product')
router.register('article', ArticleViewset, basename='article')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')), # Framework Rest-django
    # path('api/category/', CategoryAPIView.as_view()), pour afficher la liste des categorie
    # path('api/product/', ProductAPIView.as_view()), #pour afficher la liste des produits
    path('api/', include(router.urls)), # Url route principale
]
