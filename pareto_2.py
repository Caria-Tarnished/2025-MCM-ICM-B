#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.optimize import minimize
from pymoo.core.problem import Problem


class TourismProblem(Problem):
    def __init__(self):
        super().__init__(n_var=3, n_obj=4, n_constr=6, xl=[0, 0, 0], xu=[16000, 5, 1])

    def _evaluate(self, X, out, *args, **kwargs):
        V, N, P = X[:, 0], X[:, 1], X[:, 2]
        
        # 向量化计算
        tourism_expense = 320000000  # 游客在朱诺的消费
        cruise_company_expense = 39000000  # 游轮公司在朱诺的花费
        crew_expense = 16000000  # 游轮公司船员在朱诺的支出

        economic_revenue = (tourism_expense * V / 16000 + cruise_company_expense * N + crew_expense * N) / 100000000
        satisfaction = 100 - 20 * (1 - P)
        carbon_emission = 0.1 * V + 0.5 * N

        ecological_restoration_cost = 5000000  # 假设的生态修复费用
        community_support_cost = 3000000      # 假设的社区支持费用
        cultural_protection_cost = 2000000    # 假设的文化保护费用
        industry_diversification_cost = 1000000  # 假设的产业多元化费用
        direct_income = 100000000 
        indirect_income = 50000000 

        hidden_cost_value = 0.3 * (152000000 + 144000000 + 31000000 + 22000000 + 14000000 + 12000000) + \
                            0.25 * ecological_restoration_cost + \
                            0.2 * community_support_cost + \
                            0.15 * cultural_protection_cost + \
                            0.1 * industry_diversification_cost
        hidden_cost = np.full(V.shape, hidden_cost_value)


        # 约束条件
        g1 = V - 16000
        g2 = V - 12000
        g3 = N - 5
        g4 = 60 - satisfaction
        g5 = carbon_emission - 50
        g6 = hidden_cost - (direct_income + indirect_income)

        out["F"] = np.column_stack([-economic_revenue, -satisfaction, carbon_emission, hidden_cost])
        out["G"] = np.column_stack([g1, g2, g3, g4, g5, g6])


def test_problem():
    problem = TourismProblem()
    # 创建一些测试数据
    X_test = np.array([[8000, 3, 0.5], [16000, 5, 1.0]])
    out = {"F": None, "G": None}
    problem._evaluate(X_test, out)

    # 打印调试信息以确保形状正确
    print("X_test shape:", X_test.shape)
    print("economic_revenue shape:", out["F"][:, 0].shape)
    print("satisfaction shape:", out["F"][:, 1].shape)
    print("carbon_emission shape:", out["F"][:, 2].shape)
    print("hidden_cost shape:", out["F"][:, 3].shape)

    print("g1 to g6 shapes:", [g.shape for g in out["G"].T])


# 运行测试函数以检查问题定义
test_problem()

# 如果测试通过，则进行优化
algorithm = NSGA2(pop_size=100)
res = minimize(TourismProblem(), algorithm, ('n_gen', 200), verbose=False)

# 绘制帕累托前沿图像
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(res.F[:, 0], res.F[:, 1], res.F[:, 2])
ax.set_xlabel('Economic Revenue (negative for maximization)')
ax.set_ylabel('Social Satisfaction (negative for maximization)')
ax.set_zlabel('Carbon Emission')
plt.title('Pareto Front for Tourism Optimization')
plt.show()

pareto_front = res.F
print("帕累托前沿解：")
for i, solution in enumerate(pareto_front):
    print(f"解{i + 1}: 经济收益: {-solution[0]}, 居民满意度: {-solution[1]}, 碳排放: {solution[2]}, 隐藏成本: {solution[3]}")


# In[ ]:




