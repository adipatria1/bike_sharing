import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st 

st.title('DASHBOARD SEWA SEPEDA TAHUN 2011 - 2012')
def plot_trend(chart_type):
    # Load data
    bike_df = pd.read_csv(r'C:\Users\Work\Documents\bike_sharing\bike_sharing_all.csv')

    if chart_type == 'Bar':

        bike_2011_2012 = bike_df.copy()
        bike_2011_2012['yr'] = bike_2011_2012['yr'].replace({0: '2011', 1: '2012'})
        bike_2011_2012 = bike_2011_2012[(bike_2011_2012['yr'] == '2011') | (bike_2011_2012['yr'] == '2012')]

        monthly_data = bike_2011_2012.groupby(['yr', 'mnth'])['cnt'].sum().reset_index()

        fig, ax = plt.subplots(figsize=(10,5))
        sns.barplot(data=monthly_data, x="mnth", y="cnt", hue="yr", ax=ax, palette=["#FFC300", "#900C3F"])
        ax.set_title('Pola Permintaan Sewa Sepeda Tahun 2011-2012', fontsize=20, pad=20)
        ax.set_xlabel('Bulan', fontsize=12)
        ax.set_ylabel('Jumlah Permintaan', fontsize=12)
        ax.tick_params(axis='both', which='major', labelsize=12)

    elif chart_type == 'Line':
        
        bike_df_2011_casual = bike_df[(bike_df['yr'] == 0) & (bike_df['casual'])]
        bike_df_2011_registered = bike_df[(bike_df['yr'] == 0) & (bike_df['registered'])]
        bike_df_2012_casual = bike_df[(bike_df['yr'] == 1) & (bike_df['casual'])]
        bike_df_2012_registered = bike_df[(bike_df['yr'] == 1) & (bike_df['registered'])]

        fig, ax = plt.subplots(figsize=(10,5))
        ax.plot(bike_df_2011_casual.groupby('mnth')['cnt'].sum(), color='orange', label='Casual 2011')
        ax.plot(bike_df_2011_registered.groupby('mnth')['cnt'].sum(), color='red', label='Registered 2011')
        ax.plot(bike_df_2012_casual.groupby('mnth')['cnt'].sum(), color='black', label='Casual 2012')
        ax.plot(bike_df_2012_registered.groupby('mnth')['cnt'].sum(), color='blue', label='Registered 2012')
        ax.set_title('Trend Penggunaan Sepeda Tahun 2011 dan 2012', fontsize=20, pad=20)
        ax.set_xlabel('Bulan')
        ax.set_ylabel('Jumlah Pengguna')
        ax.legend()
        plt.show()

    st.pyplot(fig)

menu = ['Bar', 'Line']
choice = st.sidebar.selectbox('Pilih Chart yang ingin ditampilkan', menu)

if choice == 'Bar':
    plot_trend('Bar')
else:
    plot_trend('Line')
