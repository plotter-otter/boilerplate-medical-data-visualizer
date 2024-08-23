import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv', delimiter = ',')

# 2
df['overweight'] = df['weight']/((df['height']/100)**2)
df['overweight'] = (df['overweight'] > 25).astype(int)

# 3
#simpler
df['cholesterol'] = df['cholesterol'].replace({1: 0, 2: 1, 3: 1})
df['gluc'] = df['gluc'].replace({1: 0, 2: 1, 3: 1})

#more generalised method, focus on the > 1 condition, doesn't require us to know all possible values
#df[['cholesterol','gluc']]=df[['cholesterol','gluc']].apply(lambda col: np.where(col > 1, 1 ,0))

# 4
def draw_cat_plot():
    # 5
    df_cat = df.melt(id_vars = 'cardio', value_vars = ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])


    # 6
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    

    # 7
    catplot = sns.catplot(x = "variable", y = "total", data = df_cat, kind = "bar", hue='value', col = "cardio")

    # 8
    fig = catplot.fig

    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[
    (df['ap_lo'] <= df['ap_hi']) &
    (df['height'] >= df['height'].quantile(0.025)) &
    (df['height'] <= df['height'].quantile(0.975)) &
    (df['weight'] >= df['weight'].quantile(0.025)) &
    (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))



    # 14
    fig, ax = plt.subplots(figsize=(15, 10))

    # 15
    sns.heatmap(corr, mask=mask, annot=True, fmt=".1f", ax = ax)

    # 16
    fig.savefig('heatmap.png')
    return fig
