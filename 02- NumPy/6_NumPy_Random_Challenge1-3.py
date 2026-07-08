import numpy as np

print("====CH 1====")
numbers = np.random.randint(1,100,size=10)
print(numbers)

print("====CH 2====")
numbers = np.random.randint(10,50,size=(2,5))
print(numbers)

print("====CH 3====")

print("====Probable to Repetition====")
fruits = ["Apple","Orange","Banana","Mango"]
print(np.random.choice(fruits,size=3))

print("====Avoiding Repetition====")
fruits = ["Apple","Orange","Banana","Mango"]
print(np.random.choice(fruits,size=3, replace=False))
