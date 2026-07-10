import pandas as pd 

students = {
    "StudentID": [1,2,3],
    "Name": ["Santo","Robi","Darmin"],
    
}
scores = {
    "StudentID": [1,2,3],
    "Scores": [78,89,97]
}

df_student = pd.DataFrame(students)
df_score = pd.DataFrame(scores)

merged = pd.merge(df_student,df_score,on="StudentID")
print(merged)