from fastapi import FastAPI, Request
from typing import Optional
from mock_Data import products

app = FastAPI()

# @app.get("/")   copilot suggestion
# async def root():
#     return {"message": "Hello World"}

@app.get("/")
def home():
    return "Welcome to FastAPI!"

@app.get("/products")
def get_products():
    return products

## path parameter
# @app.get("/products/{product_id}")
# def get_one_product(product_id: int):
#     for product in products:
#         if product["id"] == product_id:
#             return product
#     return {"message": "Product not found"}

## query parameter when both params are must to pass
@app.get("/products/search")
def search_products(id: int, query: str):
    for product in products:
        if product["id"] == id and query.lower() in product["title"].lower():
            return product

    return {"message": "Product not found"}


## query parameter when one param can be optional
# @app.get("/products/search")
# def search_products(id: int, query: Optional[str] = None):
#     for product in products:
#         # Check if ID matches
#         if product["id"] == id:
#             # If a query is provided, check if it's in the title
#             if query:
#                 if query.lower() in product["title"].lower():
#                     return product
#             else:
#                 # If no query provided, just return the product by ID
#                 return product
                
#     return {"message": "Product not found"}


##http://127.0.0.1:8000/greet?name=ali
@app.get("/greet")
def greet_user(request: Request):
    print(request.query_params)  # This will print the query parameters to the console
    name = request.query_params.get("name", "Guest")
    age= request.query_params.get("age", "unknown")
    return {"message": f"Hello, {name}! You are {age} years old."}