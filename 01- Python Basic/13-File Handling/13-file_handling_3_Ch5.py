total = 0
count = 1

with open("salary.txt", "r") as file:
    for line in file:

        total += int(line.strip())
        print("Salary", count, ":", line.strip())
        count += 1
        
print("Total Salary:", total)

jumlah_data = count - 1
average = total / jumlah_data
print("Average Salary:",(average))
        
