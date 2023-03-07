# Ecommerce-Django-Application-with-GraphQL
This is an ecommerce application built with Django and GraphQL. The application allows users to create accounts, browse products, add products to their cart, and complete orders. The application also includes a GraphQL API that allows developers to query and mutate data.

## Features
- User authentication and authorization
- Product browsing and search
- Shopping cart functionality
- Order management
- GraphQL API for querying and mutating data
## Technologies Used
- Django
- Django REST framework
- GraphQL
- PostgreSQL

## Setup
### Clone the repository:

```
git clone https://github.com/example/ecommerce-django-graphql.git
```

### Create a virtual environment and activate it:

```
python -m venv venv
source venv/bin/activate
```

### Install the dependencies:

```
pip install -r requirements.txt
```

### Set up the database:

```
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata fixtures/*.json
```

### Start the development server:

```
python manage.py runserver
```

### Open the application in your web browser at http://localhost:8000.

## Screenshots
#### Example Mutations
Create Product
![mutation](https://user-images.githubusercontent.com/50916200/223346288-ae1ac952-d66f-4884-953f-40103651b127.JPG)

#### Example Queries
Get All Products
![Query](https://user-images.githubusercontent.com/50916200/223346459-13de1680-4804-4546-b4ab-c6745c85f76e.JPG)

### GraphQL API
The application includes a GraphQL API that allows developers to query and mutate data. The endpoints include:

Products

 - http://127.0.0.1:8000/api/products
 
 Categories
 
 - http://127.0.0.1:8000/api/category
 
 Orders
 
  - http://127.0.0.1:8000/api/order

Here are some example queries and mutations that you can use with the API:

### Queries
Get All Products
```
{
  products {
    name: name
    description: description
    price: price
    slug: slug
    image:image
    stock: stock
    available: available
  }
}
```



### Mutations
Create Product
```
mutation {
  createProduct(
    name: "Apple iPhone 13 Mini", 
    description: "Display: 5.4 inch, Processor: Apple A15 Bionic, Connectivity: 5G, Nano-SIM, eSIM, Wi-Fi 6, Colors: Starlight, Midnight, Blue, Pink, Red", 
    category: "Electronics", 
    price: 90000, 
    image: "https://www.phoneplacekenya.com/wp-content/uploads/2021/07/iPhone-13-mini-c.jpg", 
    stock: 21,
    available: true
  ) 
  {
    product {
      id
      name
      description
      price
      image
      stock
      available
    }
  }
}
```

P.S: Still a work in progress
