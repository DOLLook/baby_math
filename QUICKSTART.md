# 快速启动指南

## 1. 环境准备

### 1.1 安装Python
确保你的系统已安装Python 3.8或更高版本。

### 1.2 安装依赖包

```bash
# 进入项目目录
cd %PROJECT_ROOT%

# 安装所有依赖包
pip install -r requirements.txt
```

## 2. 启动Jupyter

### 2.1 启动Jupyter Lab（推荐）

```bash
jupyter lab
```

### 2.2 启动Jupyter Notebook

```bash
jupyter notebook
```

启动后，浏览器会自动打开Jupyter界面。

## 3. 学习路径

### 第一阶段：基础数学
1. 打开 `notebooks/01_基础数学/01_Python数学基础.ipynb`
2. 学习NumPy基础、函数可视化、SymPy符号计算
3. 完成笔记本中的练习题

### 第二阶段：线性代数
1. 打开 `notebooks/02_线性代数/01_线性代数基础.ipynb`
2. 学习向量运算、矩阵运算、矩阵分解
3. 完成笔记本中的练习题

### 第三阶段：微积分
1. 打开 `notebooks/03_微积分/01_微积分基础.ipynb`
2. 学习极限、导数、积分、泰勒级数
3. 完成笔记本中的练习题

### 第四阶段：概率统计
1. 打开 `notebooks/04_概率统计/01_概率统计基础.ipynb`
2. 学习统计量、概率分布、假设检验、相关性分析
3. 完成笔记本中的练习题

### 第五阶段：应用案例
1. 打开 `notebooks/05_应用案例/01_数据可视化与EDA.ipynb`
2. 学习数据可视化、探索性数据分析
3. 完成笔记本中的练习题

## 4. 使用自定义工具

项目提供了多个自定义工具函数，可以在笔记本中直接使用：

```python
# 导入工具函数
import sys
sys.path.append('..')
from utils.visualization import plot_function, plot_3d_surface
from utils.math_utils import derivative, integral, solve_equation
from utils.matrix_utils import matrix_multiply, matrix_inverse, eigen_decomposition

# 使用示例
plot_function(lambda x: x**2, (-5, 5, 100), "二次函数")
```

## 5. 常见问题

### Q1: 安装依赖时出错
A: 尝试使用国内镜像源：
```bash
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### Q2: Jupyter无法启动
A: 确保已正确安装jupyter：
```bash
pip install jupyter jupyterlab
```

### Q3: 中文显示乱码
A: 笔记本已配置中文字体支持，如果仍有问题，请安装中文字体。

### Q4: 如何添加新的笔记本
A: 在对应的主题目录下创建新的.ipynb文件即可。

## 6. 进阶学习

### 创建虚拟环境（推荐）
```bash
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境 (Windows)
venv\Scripts\activate

# 激活虚拟环境 (Linux/Mac)
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt
```

### 使用Jupyter扩展
```bash
# 安装Jupyter扩展
pip install jupyter_contrib_nbextensions
jupyter contrib nbextension install --user

# 启用常用扩展
jupyter nbextension enable --py widgetsnbextension
```

## 7. 获取帮助

- 查看每个笔记本中的详细说明和注释
- 参考官方文档：
  - NumPy: https://numpy.org/doc/
  - Matplotlib: https://matplotlib.org/stable/contents.html
  - SciPy: https://docs.scipy.org/doc/scipy/
  - SymPy: https://docs.sympy.org/

祝你学习愉快！
