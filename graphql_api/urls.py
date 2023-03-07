from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from .views import ProductView, CategoryView

urlpatterns = [
    path('products/', csrf_exempt(ProductView.as_view(graphiql=True)), name='products'),
    path('category/', csrf_exempt(CategoryView.as_view(graphiql=True)), name='category')
]
