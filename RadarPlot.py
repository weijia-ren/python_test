#%% [markdown]
# # Draw the radar plot
# ## Import Libraries
# 

#%% 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#%% [markdown]
# ## Load and review data

#%%
data = pd.read_csv('cities_ranking.csv')
data.head(5)
data
#%%
#!/usr/bin/env python
# -*- coding: utf-8 -*-


#%%
#!/usr/bin/env python
# -*- coding: utf-8 -*-
def plot_radar(data, city):
    '''
    data是上面读入的原始数据
    city是要显示的城市，可以是一个城市，比如city="上海"
    也可以是一组城市，比如city=["杭州", "南京"]
    为了视觉效果，最多同时展示5个城市。
    '''
    if type(city) != list: city = [city]

    # 从下面六项指标，体现城市发展水平
    cols = ['文化', '科教', '经济产值', '财富储蓄', '环境', '卫生']

    # 每个城市的配色
    colors = ['green', 'blue', 'red', 'yellow', 'black']

    # 把圆形进行六等分
    angles = np.linspace(0.1 * np.pi, 2.1 * np.pi, len(cols), endpoint=False)
    angles = np.concatenate((angles, [angles[0]]))

    # 初始化一个极坐标图像
    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, polar=True)

    # 逐一添加每个城市图像以及排名信息
    for i, c in enumerate(city):
        rank = data.loc[data['城市'] == c, '排名'].values[0]
        stats = data.loc[data['城市'] == c, cols].values[0].tolist()
        stats = np.concatenate((stats, [stats[0]]))
        ax.plot(angles, stats, '-', linewidth=6, c=colors[i], label='%s 排名第%s'%(c, rank))
        ax.fill(angles, stats, c=colors[i], alpha=0.25)

    # 添加图例
    ax.legend(loc=[0.25, 1.15], fontsize=18)
    ax.set_yticklabels([])
    ax.set_thetagrids(angles * 180/np.pi, cols, fontsize=16)
    ax.grid(True)

    # 完成
    plt.show()
    return fig

plot_radar(data, "上海");
plot_radar(data, ['成都', '重庆']);
