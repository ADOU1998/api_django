from dataclasses import field
from pyexpat import model
from rest_framework.serializers import ModelSerializer

from shop.models import Article, Category, Product

# Afficher les objets category en json 
class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'date_created', 'date_updated', 'name']

# Afficher les objets produits en json 
class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'date_created', 'date_updated', 'name', 'category']

# Afficher les objets articles en json 
class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'date_created', 'date_updated', 'name', 'price', 'product']
