import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv', delimiter = ',').set_index('id')

# 2
df['overweight'] = df['weight']/((df['height']/100)**2)
df['overweight'] = (df['overweight'] > 25).astype(int)

# 3
#simpler
df['cholesterol'] = df['cholesterol'].replace({1: 0, 2: 1, 3: 1})
df['gluc'] = df['gluc'].replace({1: 0, 2: 1, 3: 1})

#more generalised method, focus on the > 1 condition, doesn't require us to know all possible values
#df[['cholesterol','gluc']]=df[['cholesterol','gluc']].apply(lambda col: np.where(col > 1, 1 ,0))

#data cleaning
df = df[
    (df['ap_lo'] <= df['ap_hi']) &
    (df['height'] >= df['height'].quantile(0.025)) &
    (df['height'] <= df['height'].quantile(0.975)) &
    (df['weight'] >= df['weight'].quantile(0.025)) &
    (df['weight'] <= df['weight'].quantile(0.975))
]

# 4
def draw_cat_plot():
    # 5
    df_cat = None


    # 6
    df_cat = None
    

    # 7



    # 8
    fig = sns.catplot(
    data=df, x="class", y="survived", col="cardio",
    kind="bar")


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = None

    # 12
    corr = None

    # 13
    mask = None



    # 14
    fig, ax = None

    # 15



    # 16
    fig.savefig('heatmap.png')
    return fig
