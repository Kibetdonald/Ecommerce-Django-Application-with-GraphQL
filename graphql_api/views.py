from django.http import JsonResponse
from graphene_django.views import GraphQLView
from .schema import schema

class ProductView(GraphQLView):
    def get(self, request):
        query = '''
            query {
                allProducts {
                    id
                    name
                    description
                    price
                    image
                    stock
                    available
                }
            }
        '''
        result = schema.execute(query)
        return JsonResponse(result.data, safe=False)


class CategoryView(GraphQLView):
    def post(self, request):
        mutation = '''
            mutation {
                createCategory(name: $name, description: $description) {
                    order {
                        id
                        name
                        description
                    }
                }
            }
        '''

        result = schema.execute(mutation, variable_values=variables)
        return JsonResponse(result.data, safe=False)


class OrderView(GraphQLView):
    def post(self, request):
        mutation = '''
            mutation {
                createOrder(user: $user, paid: $paid) {
                    order {
                        id
                        user
                        paid
                    }
                }
            }
        '''

        result = schema.execute(mutation, variable_values=variables)
        return JsonResponse(result.data, safe=False)
