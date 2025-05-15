import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
# 读取数据并查看
df = pd.read_csv('medical_examination.csv')
print(df.head())

#计算BMI和overweight并添加新列
df['BMI']=df['weight'] / ((df['height'] / 100) ** 2)

df['overweight'] = (df['BMI'] > 25).astype(int)


# 标准化 cholesterol 和 gluc，1 为正常，2或3 为高
df['cholesterol']=(df['cholesterol']>1).astype(int)
df['gluc']=(df['gluc']>1).astype(int)

print(df[['cholesterol','gluc']].head())
# 创建绘图函数（后面填充具体画图逻辑）
def draw_cat_plot():
    # 你可以在这写分类图逻辑
    df_cat = pd.melt(df, 
                     id_vars=['cardio'], 
                     value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active','overweight'])

    # 画分类计数图
    fig = sns.catplot(x='variable', hue='value', col='cardio', data=df_cat,
                      kind='count', height=5, aspect=1)

    fig.set_axis_labels("variable", "total")
    fig = fig.fig  # 提取出 matplotlib 的 figure 对象
    fig.savefig('catplot.png')
    plt.show()
    return fig

def draw_heat_map():
    # 你可以在这写热力图逻辑
    df_heat =df[(df['ap_lo'] <= df['ap_hi'])&(df['height'] >= df['height'].quantile(0.025))&(df['height'] <= df['height'].quantile(0.975))&(df['weight'] >= df['weight'].quantile(0.025))&(df['weight'] <= df['weight'].quantile(0.975))]

    corr = df_heat.corr()
    mask = np.triu(np.ones_like(corr, dtype=bool))
    fig, ax = plt.subplots(figsize=(12, 10))
    sns.heatmap(corr, mask=mask, annot=True, fmt=".1f", linewidths=0.5, center=0.00, square=True, cbar_kws={"shrink": 0.5})
    fig.savefig('heatmap.png')
    plt.show()    
    return fig  



draw_heat_map()