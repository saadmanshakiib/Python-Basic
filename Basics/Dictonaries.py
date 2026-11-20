product = {
    "id" : 1,
    "name" : "iphone15",
    "price" : 71000
}

print(product)
print(product["name"])
print(product.get("price"))

product["category"] = "Mobile"
product["stock"] = "Available"

print(product)

product["stock"] = "Not Available"
print(product)

product.pop("stock")
print(product)

for key in product:
    print(key)

print("\n")

for values in product.items():
    print(values)

for key,values in product.items():
    print(key , " : ", values)

if "name"  in product:
    print("Name is found")
else:
    print("Not Found")
