print("===== STRING METHOD CHALLENGE 1 =====")
name = " arnawan dwi nugraha "
print(name.strip().title())

print("===== STRING METHOD CHALLENGE 2 =====")
career = "DATA SCIENTIST"
print(name.lower())

print("===== STRING METHOD CHALLENGE 3 =====")
sentence = "I love Excel"
print(sentence.replace("Excel", "Python"))

print("===== STRING METHOD CHALLENGE 4 =====")

skills = "Python,SQL,Machine Learning"
skills_list = skills.split(",")

print(skills_list)

for skill in skills_list:
    print(skill)


print("===== STRING METHOD CHALLENGE 5 =====")

raw_name = " ARNAWAN DWI NUGRAHA "

clean_name = raw_name.strip().title()

print(clean_name)

print("Jumlah karakter:", len(clean_name))

    
