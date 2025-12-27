"""
可视化工具函数
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns

# 设置中文字体支持
plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

def plot_function(func, x_range, title="函数图像", xlabel="x", ylabel="y"):
    """
    绘制一元函数图像
    
    参数:
        func: 函数对象
        x_range: x轴范围，格式为 (start, end, num_points)
        title: 图像标题
        xlabel: x轴标签
        ylabel: y轴标签
    """
    x = np.linspace(x_range[0], x_range[1], x_range[2])
    y = func(x)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, linewidth=2, color='blue')
    plt.title(title, fontsize=14)
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
    plt.axvline(x=0, color='k', linestyle='-', linewidth=0.5)
    plt.show()

def plot_3d_surface(func, x_range, y_range, title="三维曲面"):
    """
    绘制二元函数的三维曲面
    
    参数:
        func: 二元函数对象
        x_range: x轴范围，格式为 (start, end, num_points)
        y_range: y轴范围，格式为 (start, end, num_points)
        title: 图像标题
    """
    x = np.linspace(x_range[0], x_range[1], x_range[2])
    y = np.linspace(y_range[0], y_range[1], y_range[2])
    X, Y = np.meshgrid(x, y)
    Z = func(X, Y)
    
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    surf = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
    ax.set_xlabel('X', fontsize=12)
    ax.set_ylabel('Y', fontsize=12)
    ax.set_zlabel('Z', fontsize=12)
    ax.set_title(title, fontsize=14)
    
    fig.colorbar(surf, shrink=0.5, aspect=5)
    plt.show()

def plot_multiple_functions(functions, x_range, labels=None, title="函数对比"):
    """
    绘制多个函数的对比图像
    
    参数:
        functions: 函数列表
        x_range: x轴范围
        labels: 函数标签列表
        title: 图像标题
    """
    x = np.linspace(x_range[0], x_range[1], x_range[2])
    
    plt.figure(figsize=(12, 6))
    colors = ['blue', 'red', 'green', 'orange', 'purple', 'brown']
    
    for i, func in enumerate(functions):
        y = func(x)
        label = labels[i] if labels and i < len(labels) else f'函数 {i+1}'
        plt.plot(x, y, linewidth=2, color=colors[i % len(colors)], label=label)
    
    plt.title(title, fontsize=14)
    plt.xlabel('x', fontsize=12)
    plt.ylabel('y', fontsize=12)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
    plt.axvline(x=0, color='k', linestyle='-', linewidth=0.5)
    plt.show()
