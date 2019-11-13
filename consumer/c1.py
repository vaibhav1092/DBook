import requests

value = 'token 6e4220227b2e1c23cbbc36fa6ef11615a2095249'
body_val = {
    "name": "Java",
    "author": "XXX33",
    "price": 22934.3,
    "qty": 203,
    "publication": "TTTT",
    "reviews": "stars"
}
response = requests.get('http://localhost:8000/v1/book/',
                         headers={'Authorization':value})
print(response.status_code)
print(response.json())
