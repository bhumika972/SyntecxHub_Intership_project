import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np
data=pd.read_csv(r"C:\Users\S.A COMPUTER\PycharmProjects\SyntecxHub_Intership_project\DataScience_Intenship\Data\Housing_Dataset.csv")
print(data.head(5))
print(data.tail(5))
print(data.dtypes)
print(data.describe())
print(data.columns)
print(data.shape)
print(data.isnull().sum())

usefull=['Suburb', 'Rooms', 'Type', 'Price',
         'Method', 'SellerG','Car','Bedroom2','Bathroom',
       'Landsize','Distance',
         'BuildingArea','CouncilArea',
         'Regionname', 'Propertycount']
newData=data[usefull]
print(newData.shape)
print(newData.isnull().sum())

cols=['Car','Bathroom','Bedroom2','Propertycount','Distance']
newData[cols]=newData[cols].fillna(0)


sns.displot(newData.BuildingArea)
plt.show()
newData['BuildingArea']=newData['BuildingArea'].replace(np.nan,newData['BuildingArea'].median())
newData['Landsize']=newData['Landsize'].replace(np.nan,newData['Landsize'].median())
print(newData.isnull().sum())
newData.dropna(inplace=True)
print(newData.isna().sum())

newData=pd.get_dummies(newData,drop_first=True)
print(newData.shape)

