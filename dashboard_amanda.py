import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Membaca dataset
df = pd.read_csv('./day.csv')

st.title('Dashboard Penyewaan Sepeda')

# Menampilkan informasi dataset
st.subheader('Informasi Dataset')
st.write(df.describe())

# Sidebar untuk pengaturan
st.sidebar.header('Pengaturan')
selectedYear = st.sidebar.selectbox('Pilih Tahun', ['Semua', '2011', '2012'])
selectedTempCategory = st.sidebar.selectbox('Pilih Kategori Suhu', ['Semua', 'Very Cold', 'Cold', 'Mild', 'Warm', 'Hot'])

# Filter berdasarkan tahun
if selectedYear != 'Semua':
    yearMap = {'2011': 0, '2012': 1}
    df = df[df['yr'] == yearMap[selectedYear]]

# Konversi suhu ke kategori
temp_bins = [0, 0.2, 0.4, 0.6, 0.8, 1]
temp_labels = ['Very Cold', 'Cold', 'Mild', 'Warm', 'Hot']
df['temp_category'] = pd.cut(df['temp'], bins=temp_bins, labels=temp_labels)

# Filter berdasarkan kategori suhu
if selectedTempCategory != 'Semua':
    df = df[df['temp_category'] == selectedTempCategory]

# Visualisasi Penyewaan Berdasarkan Tahun
st.subheader('Jumlah Penyewa Berdasarkan Tahun')
yearCounts = df.groupby('yr')['cnt'].sum().reset_index()
yearLabels = {0: '2011', 1: '2012'}
yearCounts['yr'] = yearCounts['yr'].map(yearLabels)

plt.figure(figsize=(8, 6))
sns.barplot(data=yearCounts, x='yr', y='cnt', palette='Greens')
plt.title('Jumlah Penyewa Berdasarkan Tahun')
plt.xlabel('Tahun')
plt.ylabel('Jumlah Penyewa')
st.pyplot(plt)

# Visualisasi Penyewaan Berdasarkan Suhu (dengan kategori suhu)
st.subheader('Jumlah Penyewa Berdasarkan Suhu')
tempCounts = df.groupby('temp_category')['cnt'].sum().reset_index()

plt.figure(figsize=(8, 6))
sns.barplot(data=tempCounts, x='temp_category', y='cnt', palette='viridis')
plt.title('Penyewaan Sepeda Berdasarkan Suhu')
plt.xlabel('Kategori Suhu')
plt.ylabel('Jumlah Penyewa')
plt.xticks(rotation=45)
st.pyplot(plt)

# Kesimpulan
st.subheader('Kesimpulan')
st.write('Analisis ini menunjukkan bagaimana tahun dan kategori suhu mempengaruhi jumlah penyewaan sepeda. Kita dapat melihat tren penyewaan sepeda pada tahun tertentu dan kategori suhu yang berbeda, yang dapat membantu dalam merencanakan strategi dan pengelolaan layanan penyewaan sepeda yang lebih efektif.')
