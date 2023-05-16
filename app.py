import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import io
import joblib


def main(): 
    new_model = joblib.load("regression.pkl")
    st.title('Esame')

    #indus	tax	ptratio	lstat	price
    st.subheader('Input_values')
    indus_value = st.slider("indus", min_value=0, max_value=50, value=25) #check valori
    ptratio = st.slider('ptratio', min_value=0, max_value=50, value=25) #check valori
    tax_value = st.slider('tax', min_value=0, max_value=50, value=25) #check valori
    lstat_value = st.slider('lstat', min_value=0, max_value=50, value=25) #check valori

    #nput_df = pd.DataFrame(input_data, index=[0])
    prediction = new_model.predict([[indus_value, ptratio,tax_value, lstat_value]])

    st.subheader('Output')
    st.write(f'Price previsto: {prediction[0]}')
    # if st.button('Scarica Excel'):
    #     output = io.BytesIO()
    #     writer = pd.ExcelWriter(output, engine='xlsxwriter')
    #     input_df.to_excel(writer, index=False, sheet_name='Input')
    #     pd.DataFrame(prediction, columns=['Profitto previsto']).to_excel(writer, index=False, sheet_name='Output')
    #     writer.save()
    #     output.seek(0)
    #     st.download_button(label="Download", data=output, file_name='output.xlsx', mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',)

if __name__ == "__main__":
    main()

# per lanciare streamlit: streamlit run app.py