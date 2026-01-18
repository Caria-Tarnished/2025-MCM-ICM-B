#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np

# 定义变量名称
variables = ["游客量±10%", "邮轮数±1艘"]

# 定义经济收益、居民满意度、碳排放的变化数据
economic_impact = [0.3, 0.15]
satisfaction_impact = [3, 0]
carbon_impact = [0.8, 1]

# 设置柱状图宽度
bar_width = 0.25

# 设置x轴位置
r1 = np.arange(len(variables))
r2 = [x + bar_width for x in r1]
r3 = [x + bar_width for x in r2]

# 绘制柱状图
plt.bar(r1, economic_impact, width=bar_width, label='经济收益波动（亿）')
plt.bar(r2, satisfaction_impact, width=bar_width, label='居民满意度变化（分）')
plt.bar(r3, carbon_impact, width=bar_width, label='碳排放变化（千吨）')

# 添加x轴标签
plt.xticks([r + bar_width for r in range(len(variables))], variables)

# 添加图例
plt.legend()

# 添加标题
plt.title('旅游相关因素变化影响分析')

# 显示图形
plt.show()


# In[ ]:




