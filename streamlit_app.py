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
  st.write('**Scatter Plot of relationship between bill length and the body mass**')
  st.scatter_chart(data = penguins, x='bill_length_mm', y='body_mass_g', color='species')
  st.write('**Scatter Plot of relationship between flipper length and the body mass**')
  st.scatter_chart(data = penguins, x='flipper_length_mm', y='body_mass_g', color='species')
    
with st.expander('Aggregation and Summarization'):
  st.write('simple aggregation by species and displaying mean body mass value')
  penguins_agg_mean = penguins.groupby('species').mean('body_mass_g')
  penguins_agg_mean
