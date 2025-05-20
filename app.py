import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
df=pd.read_csv('/workspaces/SigmaLabs/RAW_DATA_ALL (3).csv')
x=df.Rating
y=df.ratings
plt.figure(figsize=(10,10))
fig,ax=plt.subplots()
ax.plot(x,y)
st.pyplot(fig)

