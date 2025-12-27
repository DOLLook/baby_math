"""
数学计算工具函数
"""

import numpy as np
from scipy import integrate, optimize
import sympy as sp

def derivative(func, x0, h=1e-5):
    """
    计算函数在某点的数值导数
    
    参数:
        func: 函数对象
        x0: 求导点
        h: 步长
    
    返回:
        导数值
    """
    return (func(x0 + h) - func(x0 - h)) / (2 * h)

def integral(func, a, b, method='quad'):
    """
    计算函数的定积分
    
    参数:
        func: 函数对象
        a: 积分下限
        b: 积分上限
        method: 积分方法 ('quad' 或 'simpson')
    
    返回:
        积分值
    """
    if method == 'quad':
        result, error = integrate.quad(func, a, b)
        return result
    elif method == 'simpson':
        x = np.linspace(a, b, 1000)
        y = func(x)
        return integrate.simps(y, x)
    else:
        raise ValueError("不支持的积分方法")

def solve_equation(func, x0=0):
    """
    求解方程 func(x) = 0
    
    参数:
        func: 函数对象
        x0: 初始猜测值
    
    返回:
        方程的根
    """
    result = optimize.root_scalar(func, x0=x0)
    if result.converged:
        return result.root
    else:
        raise ValueError("方程求解未收敛")

def find_extremum(func, x0, method='max'):
    """
    寻找函数的极值点
    
    参数:
        func: 函数对象
        x0: 初始猜测值
        method: 'max' 或 'min'
    
    返回:
        极值点x坐标和极值
    """
    if method == 'max':
        result = optimize.minimize(lambda x: -func(x), x0)
        return result.x[0], -result.fun
    else:
        result = optimize.minimize(func, x0)
        return result.x[0], result.fun

def taylor_series(func, x0, n=5):
    """
    计算函数的泰勒级数展开（符号计算）
    
    参数:
        func: SymPy表达式
        x0: 展开点
        n: 展开阶数
    
    返回:
        泰勒级数表达式
    """
    x = sp.symbols('x')
    series = sp.series(func, x, x0, n+1)
    return series.removeO()

def limit(func, x0, direction='both'):
    """
    计算函数的极限
    
    参数:
        func: SymPy表达式
        x0: 趋近点
        direction: 趋近方向 ('+', '-', 'both')
    
    返回:
        极限值
    """
    x = sp.symbols('x')
    if direction == '+':
        return sp.limit(func, x, x0, dir='+')
    elif direction == '-':
        return sp.limit(func, x, x0, dir='-')
    else:
        return sp.limit(func, x, x0)
