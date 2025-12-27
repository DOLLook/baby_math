"""
数学编程教学工具函数模块
"""

from .visualization import plot_function, plot_3d_surface
from .math_utils import derivative, integral, solve_equation
from .matrix_utils import matrix_multiply, matrix_inverse, eigen_decomposition

__all__ = [
    'plot_function',
    'plot_3d_surface',
    'derivative',
    'integral',
    'solve_equation',
    'matrix_multiply',
    'matrix_inverse',
    'eigen_decomposition'
]
