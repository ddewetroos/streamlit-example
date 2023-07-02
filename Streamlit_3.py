import pandas as pd
import streamlit as st
#students names
students = ["Amelia Kami", "Antoinne Mark", "Peter Zen", "North Kim"]
#marks
marks = [82, 76, 96, 68]

df = pd.DataFrame()

df["Student Name"] = students

df["Marks"] = marks
#Save to dataframe
df.to_csv("students.csv", index = False)

#display dataframe
st.dataframe(df)

#Static table
st.table(df)

#Metrics
st.metric("KPI", 56, 3)

#Json
st.json(df.to_dict())

#Displaying an image using Streamlit
#from PIL import Image
#image = Image.open('ann-unsplash.jpg')

#st.image(image, caption = 'Sunset: Photo by Ann Savchenko on Unsplash')

#Code
#average of a list
code = '''def cal_average(numbers):
    sum_number = 0
    for t in numbers:
        sum_number = sum_number + t           

    average = sum_number / len(numbers)
    return average'''
st.code(code, language='python')



