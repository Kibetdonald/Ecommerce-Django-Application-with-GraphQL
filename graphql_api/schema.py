import graphene
from graphene_django import DjangoObjectType
from .models import Product, Category, Order

class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = '__all__'
class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = '__all__'

class OrderType(DjangoObjectType):
    class Meta:
        model = Order
        fields = '__all__'
class Query(graphene.ObjectType):
    all_products = graphene.List(ProductType)
    all_categories = graphene.List(CategoryType)
    all_orders = graphene.List(OrderType)

    def resolve_all_products(self, info):
        return Product.objects.all()

    def resolve_all_categories(self, info):
        return Category.objects.all()
    
    def resolve_all_orders(self, info):
        return Order.objects.all()

#  Products Mutation
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

# Category Mutation
class CreateCategoryMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String(required=True)
    
    category = graphene.Field(CategoryType)

    def mutate(self, info, name, description):
        category = Category(name=name, description=description)
        category.save()
        return CreateCategoryMutation(category=category)

# Order Mutation
class CreateOrderMutation(graphene.Mutation):
    class Arguments:
        user = graphene.String(required=True)
        paid = graphene.Boolean(required=True)
    
    order = graphene.Field(OrderType)

    def mutate(self, info, user, paid):
        order = Order(user=user, paid=paid)
        order.save()
        return CreateOrderMutation(order=order)

class Mutation(graphene.ObjectType):
    create_product = CreateProductMutation.Field()
    create_category = CreateCategoryMutation.Field()
    create_order = CreateOrderMutation.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
