import pandas as pd
import streamlit as st
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
le=LabelEncoder()
df= pd.read_csv("fish.csv")
df['Species']=le.fit_transform(df['Species'])

x=df.iloc[:,:-1]
y=df.iloc[:,-1]

x_train,x_test,y_train,y_test=train_test_split(x.values,y.values)
model=LinearRegression()
model.fit(x_train,y_train)

import streamlit as st
st.title("Fish Weight prediction")
ft=st.radio("Fish_type",("Bream","Roach","Whitefish","Parkki","Pike","Smelt"))
length1=st.number_input("Length1")
length2=st.number_input("length2")
length3=st.number_input("length3")
height=st.number_input("height")
width=st.number_input("width")

if ft=="Bream":
	ft=0
elif ft=="Roach":
	ft=1
elif ft=="Whitefish":
	ft=2
elif ft=="Parkki":
	ft=3
elif ft=="Pike":
	ft=4
else:
      ft=5


li=[ft,length1,length2,length3,height,width]

x=model.predict([li])
st.write(x)
st.text(x)