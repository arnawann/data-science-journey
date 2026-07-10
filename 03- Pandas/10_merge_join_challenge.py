import pandas as pd

print("=== Challenge 1 ===")
products = {
    "ProductID": [101,102,103,104],
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor"]
}


prices = {
    "ProductID": [101,102,103,104],
    "Price": [1000, 20, 50, 200]    
}

product = pd.DataFrame(products)
price = pd.DataFrame(prices)

print(pd.merge(product, price, on="ProductID"))

print("=== Challenge 2 ===")

mahasiswas = {
    "StudentID": [10,20,30,40],
    "Name": ["Jalal","Bangkong","Juminem","Ratno"]
}

nilais = {
    "StudentID": [10,20,30,40],
    "Score": [80,50,70,90]
}

mahasiswa = pd.DataFrame(mahasiswas)
nilai = pd.DataFrame(nilais)
print(pd.merge(mahasiswa, nilai, on="StudentID"))

print("=== Challenge 3 ===")

employees = {
    "ID": [101,102,103],
    "Name": ["Pangat","Susi","Juminten"]
}

departments = {
    "ID": [101,102,103],
    "Department": ["Finance", "HR", "IT"]
}

employee = pd.DataFrame(employees)
department = pd.DataFrame(departments)
print(pd.merge(employee, department, on="ID"))