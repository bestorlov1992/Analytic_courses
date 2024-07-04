import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# plt.style.use('seaborn')


# Так строим графики через matplotlib
'''df = pd.read_csv('wage-data-coast.csv')
print(df)

data = df[df['Year'] == 2000]['Salary']
data_1 =df[df['Year'] == 2010]['Salary']

fig, ax = plt.subplots(figsize = (12,6))
_, bins,_ = ax.hist(data_1, label = '2010', alpha = 0.5, bins = 20)
ax.hist(data, label = '2000', alpha = 0.5, bins = bins)

ax.set_title('Распределение минимальных зарплат в 2000 и 2010 годах')
ax.set_xlabel('Минимальная зарплата, $/час')
ax.set_ylabel('# записей')
ax.set_xticks(list(bins))
ax.legend()

print(plt.show())'''


# Так строим графики через seaborn
"""df = pd.read_csv('wage-data-coast.csv')
data = df[df['Year'].isin([2000, 2010])]
ax = sns.histplot(data=data, x='Salary', hue='Year')

ax.set_title('Распределение минимальных зарплат в 2000 и 2010 годах')
ax.set_xlabel('Минимальная зарплата, $/час')
ax.set_ylabel('# записей')
print(plt.show())

# График № 1
data_1 = df[df['State'].isin(['Alaska', 'California', 'Washington', 'Arizona', 'Florida'])]
fig, ax = plt.subplots(figsize = (12, 6))
sns.lineplot(data = data_1, x='Year', y='Salary', hue='State', ax = ax)

ax.set_title('Динамика минимальной зарплаты в пяти штатах')
ax.set_xlabel('Год')
ax.set_ylabel('Минимальная зарплата, $/час')

print(plt.show())"""

# График № 2
"""df = pd.read_csv('wage-data-coast.csv')
data_2 = df[df['Year'].isin([2000])]
fig, ax = plt.subplots(figsize=(12, 6))
sns.histplot(data_2, x = 'Salary', hue = 'IsCoastal', ax = ax)

ax.set_title('Минимальная зарплата по прибрежным и неприбрежным штатам в 2000 году')
ax.set_xlabel('Минимальная зарплата, $/час')
ax.set_ylabel('# записей')
print(plt.show())"""

# ОСНОВНЫЕ ВИДЫ ГРАФИКОВ
"""df = pd.read_csv('wage-data-coast.csv')
data_2 = df[df['Year'].isin([2000])]
fig, ax = plt.subplots(figsize=(12, 6))
sns.histplot(data_2, x = 'Salary', hue = 'IsCoastal', ax = ax,  alpha = 0.25, bins =25, multiple = 'dodge')

ax.set_title('Минимальная зарплата по прибрежным и неприбрежным штатам в 2000 году')
ax.set_xlabel('Минимальная зарплата, $/час')
ax.set_ylabel('# записей')
print(plt.show())"""

# Линейный график минимальной зарплаты по пяти штатам
"""df = pd.read_csv('wage-data-coast-with-population.csv')
data =df[df['State'].isin(['Alaska', 'California', 'Washington', 'Arizona', 'Florida'])]
df_t = data[data['Year'] == 2017][['State', 'Population']].sort_values('Population')
df_t.loc[:, 'Size'] = list(range(1, df_t.shape[0] + 1))
data1 = data.merge(df_t[['State', 'Size']], how ='left', on='State')

fig, ax = plt.subplots(figsize = (12, 6))
sns.lineplot(data=data1, x = 'Year', y = 'Salary', hue = 'State', ax=ax, style='IsCoastal', size='Size')
ax.set_title('Динамика минимальной зарплаты в пяти штатах')
ax.set_xlabel('Год')
ax.set_ylabel('Минимальная зарплата, $/час')

print(data1.head(10))
print(df_t.shape)
print(plt.show())"""

# Точечный график
"""fig, ax_1 = plt.subplots(figsize = (12, 6))
sns.scatterplot(data=df, x='Year', y='Salary', ax = ax_1, hue="Population", alpha = 0.5,
                size='Population')

ax.set_title('Динамика минимальной зарплаты в США')
ax.set_xlabel('Год')
ax.set_ylabel('Минимальная зарплата, $/час')

print(plt.show())"""

# Несколько графиков на одном полотне

df = sns.load_dataset('diamonds')
print(df)
# fig, ax = plt.subplots(figsize=(15, 15))
sns.pairplot(df, hue = 'cut')
print(plt.show())
