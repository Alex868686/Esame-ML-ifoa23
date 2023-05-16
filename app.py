import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
import streamlit as st

def main():
    st.title('Are you ready?')
    st.markdown('Streamlit is **_really_ cool**.')
    st.header('Are you :blue[really ready] :sunglasses:')

if __name__ == "__main__":
    main()

# per lanciare streamlit: streamlit run app.py