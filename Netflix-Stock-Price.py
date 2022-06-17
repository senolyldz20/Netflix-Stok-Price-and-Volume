#1-İmport İşlemleri
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mpl_dates

#2-Verilerin okunması ve gözlenmesi
netflix_df = pd.read_csv(r"C:\Users\senol\PycharmProjects\DataCamp Project\Mine\Netflix-02\data\Netflix.csv")
print(netflix_df.head())                # verilerin ilk 5 satırlarını çağırmış olduk.


#3-Verilerin Filtrelenemesi
netflix_new_df = netflix_df.drop(columns =["Adj Close"]) #Adj Close sütunu kaldırmış olduk.
print(netflix_new_df)


#4-Verilerin Görseleştirilmesi (Data ve Volume)
fig, ax = plt.subplots(figsize=(20,8))
ax.bar(netflix_new_df["Date"], netflix_new_df["Volume"], color = "red")
ax.xaxis.set_major_locator(plt.MaxNLocator(15))
ax.set_xlabel("Date", fontsize = "12")
ax.set_ylabel("Volume", fontsize = "12")
plt.title("Netflix Date Volume")
plt.grid()
print(plt.show())


#5-Verilerin Görseleştirilmesi (Data ve Close)
fig, ax = plt.subplots(figsize=(20,8))
ax.plot(netflix_new_df["Date"], netflix_new_df["Close"], color = "Blue")
ax.xaxis.set_major_locator(plt.MaxNLocator(15))
ax.set_xlabel("Date", fontsize = "12")
ax.set_ylabel("Price in USD", fontsize = "12")
plt.title("Netflix Stock Prices")
plt.grid()
print(plt.show())
