from TM1py import TM1Service

tm1_params = {
    "address": '',
    "port": 30033,
    "ssl": False,
    "user": "admin",
    "password": ""
}

with TM1Service(**tm1_params) as tm1:
    print(tm1.server.get_product_version())
