from fastapi import FastAPI
#from fastapi.middleware.cors import CORSMiddleware
from redis_om import get_redis_connection,  HashModel


#uvicorn main:app --reload  // cmd to get values from api. in order to make this work you have to run from the source folder
#to stop to run ctrl+c
app=FastAPI()


'''
Basicamnete uvicorn está a correr an port 8000,  mas pode existir diferentes port e de forma prevenir isso temos de criar um middleware,  e temos de colocar as port permitidas.

app.add_middleware(
    CORSMiddleware,
    #this port are our frontend so we need to allow frontend to call apis
    allow_origins=['http://localhost:3000'],
    allow_methods=['*'],
    allow_headers=['*']
    
)'''

redis = get_redis_connection(
    host="redis-10771.c293.eu-central-1-1.ec2.cloud.redislabs.com",
    port="10771",
    password="Ekh7F2c8vmHUbTi6q5cOJdoFFBuxGMgd",
    decode_responses=True
)


'''
agora tem de ser convertido um modulo para uma tabela no redis

'''


class Product(HashModel):
    name: str
    price: float
    quantity: int

    class Meta:
        database = redis


@app.get('/products')
def all():
    return [format(pk) for pk in Product.all_pks()]


def format(pk: str):
    product = Product.get(pk)

    return {
        'id': product.pk,
        'name': product.name,
        'price': product.price,
        'quantity': product.quantity
    }


@app.post('/products')
def create(product: Product):
    return product.save()


@app.get('/products/{pk}')
def get(pk: str):
    return Product.get(pk)


@app.delete('/products/{pk}')
def delete(pk: str):
    return Product.delete(pk)