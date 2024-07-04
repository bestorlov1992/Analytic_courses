import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('vgsales.csv')
print(df.head())

# Задание № 1
"""data = df[df['Genre'].isin(['Sports'])]
fig, ax = plt.subplots(figsize=(12,6))

sns.lineplot(data=data, x = 'Year', y = 'JP_Sales', hue = 'Genre', ax=ax)

ax.set_title('Объем продаж всех игр жанра \"Sports\" в Японии')
ax.set_xlabel('Год')
ax.set_ylabel('млн. копий')

print(plt.show())


# Задание № 2
data_1 = df[df["Publisher"].isin(['Activision'])][['Year','NA_Sales','EU_Sales','JP_Sales', 'Global_Sales'
                                                   ]].sort_values('Year')
print(data_1.head())
fig, ax = plt.subplots(figsize=(12,6))
for i in range(1, 5):
    sns.lineplot(data=data_1, x = 'Year', y = data_1.columns[i], ax=ax, label = data_1.columns[i], alpha = 0.8)

ax.set_title('Динамика продаж студии \"Activision\" в Северной Америке, Европе, \n Японии, и во всем мире')
ax.set_xlabel('Год')
ax.set_ylabel('Млн. копий')
ax.set_xticks(list(range(int(data_1['Year'].min()), int(data_1['Year'].max()), 2)) + [data_1['Year'].max()])
print(plt.show())"""

# Задание № 3
'''data_1 = df[df["Publisher"].isin(['Activision'])][['Year','NA_Sales','EU_Sales','JP_Sales', 'Global_Sales'
                                                   ]].sort_values('Year')
fig, axs = plt.subplots(nrows = 4, sharex = True, figsize = (14,14))
for i in list(range(1, 5)):
    ax = axs[i-1]
    sns.lineplot(data=data_1, y=data_1.columns[i], x='Year', ax=ax)
    ax.set_ylabel('млн. копий')

    if i == 4:
        ax.set_xlabel('Год')
        ax.set_xticks(list(range(int(data_1['Year'].min()), int(data_1['Year'].max()), 2)) + [data_1['Year'].max()])
fig.suptitle('Продажи студии \"Activision\" в Северной Америке, Европе, \n Японии, и во всем мире.', y =0.95)
print(plt.show())'''


# Задание № 4
"""sns.pairplot(df, hue = 'Platform')
print(plt.show())"""

# Задание № 5
'''data_2 = df[(df['Publisher'] == 'Microsoft Game Studios') | (df['Publisher'] == 'Take-Two Interactive') & (
    df["Year"] >= 2010)][['Year', 'Publisher', 'Global_Sales']]

fig, ax = plt.subplots(figsize=(12,6), sharex = True)

sns.histplot(data_2, x='Global_Sales', hue = 'Publisher', ax=ax, bins = 22, alpha = 0.5)

ax.set_xticks(list(range(0,23)))
print(data_2['Global_Sales'].max())
print(plt.show())'''

# Задание № 6
'''data_3 = df[df['Publisher'] == 'Nintendo'].groupby('Year')['Name'].count().reset_index()
fig, ax = plt.subplots(figsize=(12,6))
sns.lineplot(data=data_3, x='Year', y='Name', ax=ax)

ax.set_title('Количество игр выпускаемых \"Nine\", по годам', y = 1.05)
ax.set_xlabel('Год')
ax.set_label('Штук')
ax.set_xticks(list(range(int(data_3['Year'].min()), int(data_3['Year'].max()), 2)) + [data_3['Year'].max()])

# Прямогольный фон. В этот диапозон входят значения, где выпускали больше 35 игр.
list_id = []
for id, number in enumerate(data_3['Name']):
    if number >= 35:
        list_id.append(id)
ax.axvspan(xmin=data_3['Year'][list_id[0]], xmax=data_3['Year'][list_id[-1]], color = 'green', alpha = 0.5)

print(plt.show())'''


# Задание № 7

data_1 = df.groupby('Genre')['Global_Sales'].sum().reset_index().sort_values(['Global_Sales'], ascending=False)
print(data_1.head(20))
data_2 = df.groupby('Platform')['Global_Sales'].sum().reset_index().sort_values(['Global_Sales'], ascending=False)
print(data_2.head(20))

data_4_df = df[df['Platform'].isin(['PS2', 'X360', 'PS3', 'Wii'])][[
    'Year','Platform','Genre', 'NA_Sales', 'Global_Sales']]
data_4_df = data_4_df[data_4_df['Genre'].isin(['Action', 'Sports', 'Shooter'])]
print(data_4_df.head(500))
g = sns.FacetGrid(data_4_df, row='Platform', col='Genre')
g.map(sns.scatterplot, 'Year', 'Global_Sales')
print(plt.show())


