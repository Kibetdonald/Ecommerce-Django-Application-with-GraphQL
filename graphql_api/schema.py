import graphene
from graphene_django import DjangoObjectType
from .models import Product

class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = '__all__'

class Query(graphene.ObjectType):
    products = graphene.List(ProductType)

    def resolve_products(self, info):
        return Product.objects.all()
 
class CreateProductMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String(required=True)
        category = graphene.String(required=True)
        price = graphene.Float(required=True)
        image = graphene.String(required=True)
        stock =  graphene.Int(required=True)
        available = graphene.Boolean(required=True)

    product = graphene.Field(ProductType)

    def mutate(self, info, name, description, price, category, image, stock, available):
        product = Product(name=name, description=description, category=category, price=price, image=image, stock=stock, available=available)
        product.save()
        return CreateProductMutation(product=product)

class Mutation(graphene.ObjectType):
    create_product = CreateProductMutation.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
