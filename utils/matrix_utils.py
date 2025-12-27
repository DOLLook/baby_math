"""
矩阵运算工具函数
"""

import numpy as np
from scipy import linalg

def matrix_multiply(A, B):
    """
    矩阵乘法
    
    参数:
        A: 第一个矩阵
        B: 第二个矩阵
    
    返回:
        矩阵乘积
    """
    return np.dot(A, B)

def matrix_inverse(A):
    """
    计算矩阵的逆
    
    参数:
        A: 方阵
    
    返回:
        逆矩阵
    """
    return np.linalg.inv(A)

def eigen_decomposition(A):
    """
    矩阵的特征值分解
    
    参数:
        A: 方阵
    
    返回:
        特征值和特征向量
    """
    eigenvalues, eigenvectors = np.linalg.eig(A)
    return eigenvalues, eigenvectors

def svd_decomposition(A):
    """
    奇异值分解
    
    参数:
        A: 矩阵
    
    返回:
        U, S, V
    """
    return linalg.svd(A)

def qr_decomposition(A):
    """
    QR分解
    
    参数:
        A: 矩阵
    
    返回:
        Q, R
    """
    return linalg.qr(A)

def lu_decomposition(A):
    """
    LU分解
    
    参数:
        A: 矩阵
    
    返回:
        P, L, U
    """
    return linalg.lu(A)

def solve_linear_system(A, b):
    """
    求解线性方程组 Ax = b
    
    参数:
        A: 系数矩阵
        b: 常数向量
    
    返回:
        解向量
    """
    return np.linalg.solve(A, b)

def matrix_norm(A, ord=None):
    """
    计算矩阵的范数
    
    参数:
        A: 矩阵
        ord: 范数类型 (None, 'fro', 1, -1, 2, -2, np.inf, -np.inf)
    
    返回:
        矩阵范数
    """
    return np.linalg.norm(A, ord=ord)

def matrix_rank(A):
    """
    计算矩阵的秩
    
    参数:
        A: 矩阵
    
    返回:
        矩阵的秩
    """
    return np.linalg.matrix_rank(A)

def matrix_determinant(A):
    """
    计算矩阵的行列式
    
    参数:
        A: 方阵
    
    返回:
        行列式值
    """
    return np.linalg.det(A)

def matrix_trace(A):
    """
    计算矩阵的迹
    
    参数:
        A: 方阵
    
    返回:
        矩阵的迹
    """
    return np.trace(A)
