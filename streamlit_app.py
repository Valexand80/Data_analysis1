import streamlit as st
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title('Data analysis and aggregation')

st.info('In this app, we will be performing data analysis, data summary and aggregation using the Palmer Penguins dataset')

penguins = sns.load_dataset('penguins')
with st.expander('Data'):
  st.write('**Raw data**')
  penguins

with st.expander("Visualizations"):
  st.write('**Scatter Plot of relationship between bill length and body mass**')
  st.scatter_chart(data = penguins, x='bill_length_mm', y='body_mass_g', color='species')
  
    
