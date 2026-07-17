with open("sales_data_dirty.csv",
        "w"
) as file:
    file.write("""Product,Category,Price,Quantity
Laptop,Electronics,1200,3
Mouse,Electronics,20,15
Chair,Furniture,150,5
Chair,Furniture,150,5
Sofa,Furniture,,2
T-shirt,Clothing,25,
Jeans,Clothng,50,4
Keyboard,Electronics,80,8
Mouse,Electronics,20,15
Table,Furniture,200,3
Phone,electronics,900,5
Laptop,Electronics,1200,3
""")