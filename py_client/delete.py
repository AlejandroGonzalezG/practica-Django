import requests

product_id = input("Ingrese el id del producto \n")
try:
    product_id = int(product_id)
except:
    product_id = None
    print(f'{product_id} no es un id válido')

endpoint = f"http://localhost:8000/api/products/{product_id}/delete/"

get_response = requests.delete(endpoint)
print(get_response.status_code, get_response.status_code == 204)