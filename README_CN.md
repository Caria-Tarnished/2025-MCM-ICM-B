# 2025 MCM/ICM 问题B - 朱诺旅游可持续性分析

[![Competition](https://img.shields.io/badge/Competition-MCM%2FICM%202025-blue)](https://www.comap.com/contests/mcm-icm)
[![Award](https://img.shields.io/badge/Award-Honorable%20Mention-green)](https://www.comap.com/contests/mcm-icm)
[![Problem](https://img.shields.io/badge/Problem-B-orange)](https://www.comap.com/contests/mcm-icm)

> **中文** | [English](README.md)

## 项目概述

本仓库包含我们团队参加 **2025年数学建模竞赛（MCM/ICM）问题B** 的完整代码和材料。我们的团队获得了 **Honorable Mention（荣誉奖）** 。

### 问题描述

问题B聚焦于 **阿拉斯加朱诺市的旅游可持续性**，特别是分析邮轮旅游对当地经济、环境和社会的影响。挑战在于平衡经济效益与环境保护和社区福祉。

## 项目结构

```
。
├── 2025_MCM-ICM_Problems/          # 竞赛题目文件
│   ├── 2025_MCM_Problem_B.pdf      # 英文原题
│   └── Contest_AI_Policy.pdf       # AI使用政策
├── 2025赛题翻译/                    # 题目中文翻译
│   └── 2025_MCM_Problem_B_翻译.pdf
├── Data/                            # 数据文件
│   ├── glacier_data.xlsx           # 冰川数据
│   ├── tourism_data.xlsx           # 旅游数据
│   ├── Juneau_field_data.xlsx      # 朱诺实地数据
│   └── Juneau_city_tourism_data/   # 朱诺城市旅游详细数据
├── Analysis.py                      # 敏感性分析代码
├── pareto_2.py                      # 帕累托前沿优化
├── moudle.ipynb                     # 主要建模代码
├── Time_forecast.ipynb              # 时间序列预测
├── 参考论文/                        # 参考文献
└── 论文/                            # 论文相关材料
```

## 主要模型与方法

### 1. 多目标优化模型
- **算法**: NSGA-II (非支配排序遗传算法 II)
- **目标函数**:
  - 经济收益最大化
  - 居民满意度最大化
  - 碳排放最小化
  - 隐藏成本最小化
- **文件**: `pareto_2.py`

### 2. 时间序列预测
- **方法**: 
  - Prophet 模型
  - LSTM 神经网络
- **预测变量**:
  - 空气质量指数
  - 温室气体排放
  - 冰川面积
  - 碳排放量
- **文件**: `Time_forecast.ipynb`

### 3. 决策优化
- **方法**:
  - 遗传算法 (Genetic Algorithm)
  - 直接搜索法 (Direct Search)
  - 线性回归建模
- **文件**: `moudle.ipynb`

### 4. 敏感性分析
- 分析游客量和邮轮数量变化对经济、社会和环境的影响
- **文件**: `Analysis.py`

## 技术栈

- **Python 3.9+**
- **主要库**:
  - `numpy` - 数值计算
  - `pandas` - 数据处理
  - `matplotlib` - 数据可视化
  - `scikit-learn` - 机器学习
  - `tensorflow/keras` - 深度学习
  - `prophet` - 时间序列预测
  - `pymoo` - 多目标优化
  - `deap` - 遗传算法

## 安装与运行

### 环境配置

```bash
# 克隆仓库
git clone https://github.com/Caria-Tarnished/2025-MCM-ICM-B.git
cd 2025-MCM-ICM-B

# 创建虚拟环境（推荐）
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 安装依赖
pip install numpy pandas matplotlib scikit-learn
pip install tensorflow prophet pymoo deap
```

### 运行代码

```bash
# 运行帕累托优化
python pareto_2.py

# 运行敏感性分析
python Analysis.py

# 运行 Jupyter Notebook
jupyter notebook moudle.ipynb
jupyter notebook Time_forecast.ipynb
```

## 主要结果

1. **帕累托前沿解**: 找到了经济、社会和环境目标之间的最优平衡点
2. **时间序列预测**: 预测了未来5年的环境指标变化趋势
3. **决策变量优化**: 确定了最优的游客量和邮轮数量配置
4. **敏感性分析**: 量化了不同因素变化对系统的影响程度

## 数据说明

### 主要数据集

- **glacier_data.xlsx**: 冰川面积历史数据
- **tourism_data.xlsx**: 旅游业相关数据（游客量、邮轮数量等）
- **Juneau_field_data.xlsx**: 朱诺地区综合数据
- **Juneau_city_tourism_data/**: 详细的城市旅游统计数据
  - 人口数据
  - 收入数据
  - 环境质量数据
  - 排放数据

## 团队成员

- 队员1: **[@KuTo-lgq](https://github.com/KuTo-lgq)**
- 队员2: **[@Caria-Tarnished](https://github.com/Caria-Tarnished)**
- 队员3: 一位数院同学

## 致谢

感谢所有为本项目提供数据和参考资料的机构和个人。

## 许可证

本项目仅用于学术交流和学习目的。

## 联系方式

如有任何问题或建议，欢迎通过以下方式联系：

- Email: [2571610260@qq.com]
- GitHub Issues: [项目Issues页面]

---

**注意**: 本仓库中的代码和数据仅供参考学习，请勿直接用于其他竞赛。
