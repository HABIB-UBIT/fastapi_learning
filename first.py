from fastapi import FastAPI, Request
from typing import Optional
from mock_Data import products
from dtos import productDTO

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
# @app.get("/products/search")
# def search_products(id: int, query: str):
#     for product in products:
#         if product["id"] == id and query.lower() in product["title"].lower():
#             return product

#     return {"message": "Product not found"}


## query parameter when one param can be optional
@app.get("/products/search")
def search_products(id: int, query: Optional[str] = None):
    for product in products:
        # Check if ID matches
        if product["id"] == id:
            # If a query is provided, check if it's in the title
            if query:
                if query.lower() in product["title"].lower():
                    return product
            else:
                # If no query provided, just return the product by ID
                return product
                
    return {"message": "Product not found"}


##http://127.0.0.1:8000/greet?name=ali
@app.get("/greet")
def greet_user(request: Request):
    print(request.query_params)  # This will print the query parameters to the console
    name = request.query_params.get("name", "Guest")
    age= request.query_params.get("age", "unknown")
    return {"message": f"Hello, {name}! You are {age} years old."}


## different types of http methods

@app.post("/create_product")
def create_product(data: productDTO):  ## data is the instance of productDTO class. the bosy we are passing in the postman is being validated and transformed into the productDTO object. if the data is not valid according to the productDTO model, FastAPI will automatically return a 422 Unprocessable Entity response with details about the validation errors.
    product_data= data.model_dump()  ## model_dump() is a method provided by Pydantic's BaseModel that converts the model instance into a dictionary. This allows us to easily access the data in a format that can be used for further processing, such as storing it in a database or returning it in an API response.
    print(product_data)  ## this will print the validated and transformed data to the console. you can replace this with your logic to save the product data to a database or perform other operations as needed. 
    products.append(product_data)  ## this will add the new product to the existing list of products. in a real application, you would typically save this data to a database instead of just appending it to a list. 
    return {"status": "Product created successfully....", "product": products}  ## this will return a response indicating that the product was created successfully, along with the details of the created product. you can customize this response as needed for your application.

@app.put("/update_product/{product_id}")
def update_product(product_id: int, data: productDTO):
    for product in products:
        if product["id"] == product_id:
            product.update(data.model_dump())  
            return {"status": "Product updated successfully", "product": products} 
    return {"status": "Product not found"}


@app.delete("/delete_product/{product_id}")
def delete_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            products.remove(product)
            return {"status": "Product deleted successfully", "products": products}
    return {"status": "Product not found"}
    
    
## how to call different http methods (post, put, delete) -- Any tool?

## how to validate data - dtos data transform validation objects -- pydantic models


