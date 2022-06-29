from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional



#uvicorn main:app --reload  // cmd to get values from api. in order to make this work you have to run from the source folder
#to stop to run ctrl+c
app=FastAPI()


class Item(BaseModel):
    id:int
    name:str
    description:str
    price:float
    on_offer:bool

#Basicamnete uvicorn está a correr an port 8000,  mas pode existir diferentes port e de forma prevenir isso temos de criar um middleware,  e temos de colocar as port permitidas.

@app.get('/')
def index():
    return {"message":"hello wworld"}

@app.get('/greet/{name}')
def greet_name(name:str):
    return {"greeting":f"hello {name}"}

@app.get('/greet')
def greet_optional_name(name:Optional[str]="user"):
    return {"message":f"hello {name}"}
    
@app.put('/item/{item_id}')
def update_item(item_id:int, item:Item):
    return {'namee':item.name,
            'description':item.description,
            'price':item.price,
            'on_offer':item.on_offer}
    