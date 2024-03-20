import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import openpyxl


df = pd.DataFrame({
    'Название': ['куртка', 'плащ', 'шапка', 'рукав', 'штаны', 'кросовки', 'футболка', 'носки'],
    'Цена': [2567, 1565, 15213, 14567, 2009, 20065, 256754, 293],

})

df_sorted = df.sort_values(by='Цена', ascending=False)

print(df_sorted)

df_sorted.to_excel('df_sorted.xlsx')

df_read = pd.read_excel('df_sorted.xlsx')

plt.plot(df_read["Название"], df_read["Цена"])
plt.show()






# # arr = np.empty((3,3))

# def generate(x,y):
#     return x**y
# arr = np.fromfunction(generate,(2,2))
# print(arr)



# x = pd.Series ([1500,3000,8000,500,200,5000] , index= ['футболка','джинсы','куртка','шапка', 'ботинки', 'носки'])
# print(x)

# x = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]])
# print(x)




# q = np.arange(0,12,2)
# print(q)
# years= [2000,2010,2010,2030]
# population = [117000,18000,19000,230000]


# plt.plot(years,population)
# plt.title("WORLD POPULATION")
# plt.xlabel("Years")
# plt.ylabel("populatoin")
# plt.show()


# print(sorted(clothes_prices))



# data = pd.read_excel("bitcoin.xlsx")

# print(data.head())

# plt.plot(data["Дата"], data["Значение"])
# plt.show()