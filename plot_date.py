import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
import seaborn as sns
from sklearn.cluster import KMeans

df = pd.read_csv('group_3.csv', sep=";", engine="c")
df = df.drop_duplicates(keep='first')

def plot_age(df):
    df = df[df['Год Рождения'].notna()]
    df = df[df['Год Рождения'] > 1970]
    df['Год Рождения'] = 2022 - df['Год Рождения']
    mean_df = df['Год Рождения'].mean()
    print(mean_df)
    plt.suptitle('Год Рождения')
    plt.hist(df["Год Рождения"], bins=50)
    plt.xticks(np.arange(min(df["Год Рождения"]), max(
        df["Год Рождения"]+1), step=1), rotation=45)
    plt.grid()
    plt.savefig('график_Год_Рождения.pdf')
    plt.show()

def plot_hist_city(stolb):
    letter_counts = Counter(stolb)
    s = stolb.name
    dff = pd.DataFrame.from_dict(letter_counts, orient='index')
    dff = dff[dff > 5000]
    dff = dff.dropna()
    dff = dff.drop(np.NaN, axis=0)
    dff.plot(kind='bar', stacked=True)
    plt.suptitle(str(s))
    print(dff)
    plt.show()
    plt.savefig('график_' + s + '.pdf')

def plot_hist_sex(stolb):
    letter_counts = Counter(stolb)
    s = stolb.name
    dff = pd.DataFrame.from_dict(letter_counts, orient='index')
    dff = dff.dropna()
    dff.plot(kind='bar', stacked=True)
    plt.suptitle(str(s))
    plt.legend(["2 - Мужчины \n 1 - Женщины"])
    plt.show()
    plt.savefig('график_' + s + '.pdf')

def wm_pie_proc(df):
    Womens = len(df[df["Пол"].to_numpy() == 1])
    Mens = len(df[df["Пол"].to_numpy() == 2])
    Mens_Womens = [Womens/len(df["Пол"].to_numpy()),
                   Mens/len(df["Пол"].to_numpy())]
    colors = ("red", "green")
    explode = (0, 0.1)
    plt.pie(Mens_Womens, labels=('Women', 'Men'), colors=colors,
            explode=explode, shadow=True, autopct='%1.1f%%')
    plt.show()

def kdensity_date(df):
    df = df[df['Год Рождения'].notna()]
    df = df[df['Год Рождения'] > 1970]
    df = df[df['Год Рождения'] < 2014]
    df["Год Рождения"].plot.kde()
    plt.show()

def Raspredelenie_po_city(stolb, top):
    letter_counts = Counter(stolb)
    s = stolb.name
    dff = pd.DataFrame.from_dict(letter_counts, orient='index')
    dff = dff.dropna()
    dff = dff.drop(np.NaN, axis=0)

    dff = dff.sort_values(by=0, ascending=False)
    dff = dff[0:top+1]
    dff.plot(kind='bar', stacked=True)
    plt.suptitle(str(s))
    print(dff)
    plt.show()
    plt.savefig('график_' + s + '.pdf')


def klaster(df):
    df = df.dropna()
    x = df.iloc[:, [2, 4]]
    kmeans = KMeans(1)
    kmeans.fit(x)
    identified_clusters = kmeans.fit_predict(x)
    df['cluster'] = identified_clusters
    f = df['Город'].value_counts()[df['Город'].value_counts() > 10000]
    plt.scatter(df['Год Рождения'], df['Город'].value_counts,
                c=df["cluster"], cmap="rainbow")

def city_to_age(df):
    pot = (df['Город'].dropna().map(str) + '-' + (2022 -
           df['Год Рождения'].dropna()).map(str)).value_counts()[:10]
    pot.plot.barh()
    plt.show()