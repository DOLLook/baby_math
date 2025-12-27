import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'SimSun']
plt.rcParams['axes.unicode_minus'] = False

def solve_consecutive_numbers():
    """使用木桩法解决连续数字求和问题"""
    print("🎯 挑战题：连续数字求和")
    print("=" * 50)
    print("题目：有6个连续的数字加起来等于33，找出这6个连续的数字是多少？")
    print()
    
    # 解题思路
    print("📝 解题思路（木桩法）：")
    print("-" * 50)
    print("1. 木桩法：每一根木桩比前一根高1")
    print("2. 每一根再砍去第一根那么高的一截")
    print("3. 剩下的高度就是：0, 1, 2, 3, 4, 5")
    print("4. 剩下的高度加起来：0 + 1 + 2 + 3 + 4 + 5 = 15")
    print("5. 总和是33，砍掉的总和是：33 - 15 = 18")
    print("6. 每根砍掉的是：18 ÷ 6 = 3")
    print("7. 所以第一根木桩的高度是3")
    print("8. 这6个连续的数字是：3, 4, 5, 6, 7, 8")
    print()
    
    # 验证答案
    numbers = [3, 4, 5, 6, 7, 8]
    total = sum(numbers)
    print(f"验证：{numbers[0]} + {numbers[1]} + {numbers[2]} + {numbers[3]} + {numbers[4]} + {numbers[5]} = {total}")
    print()
    
    # 绘制木桩法示意图
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    # 图1：原始木桩（6个连续数字）
    ax = axes[0, 0]
    for i, num in enumerate(numbers):
        # 绘制木桩
        rect = patches.Rectangle((i, 0), 0.6, num, 
                                   facecolor='lightblue', edgecolor='blue', linewidth=2)
        ax.add_patch(rect)
        # 标注位置
        ax.text(i + 0.3, -0.3, f'第{i+1}根', fontsize=10, ha='center')
    ax.set_xlim(-0.5, 6)
    ax.set_ylim(-0.5, 9)
    ax.set_title('原始木桩（6个连续数字）', fontsize=14, fontweight='bold')
    ax.set_ylabel('高度', fontsize=12)
    ax.grid(True, alpha=0.3)
    
    # 图2：砍去第一根的高度（每根砍掉第一根的高度）- 从底部砍去
    ax = axes[0, 1]
    for i, num in enumerate(numbers):
        # 绘制砍掉的部分（从底部砍去，用红色表示）
        rect_cut = patches.Rectangle((i, 0), 0.6, 3, 
                                        facecolor='lightcoral', edgecolor='red', linewidth=2,
                                        alpha=0.7, hatch='//')
        ax.add_patch(rect_cut)
        # 绘制剩下的部分（顶部）
        rect_remain = patches.Rectangle((i, 3), 0.6, num - 3, 
                                          facecolor='lightgreen', edgecolor='green', linewidth=2)
        ax.add_patch(rect_remain)
    # 绘制砍切线
    ax.axhline(y=3, color='red', linestyle='--', linewidth=2, label='砍切线')
    ax.set_xlim(-0.5, 6)
    ax.set_ylim(-0.5, 9)
    ax.set_title('从底部砍去第一根的高度（砍掉3）', fontsize=14, fontweight='bold')
    ax.set_ylabel('高度', fontsize=12)
    ax.grid(True, alpha=0.3)
    ax.legend(loc='upper right')
    
    # 图3：剩下的高度（0, 1, 2, 3, 4, 5）
    ax = axes[1, 0]
    remain_heights = [0, 1, 2, 3, 4, 5]
    for i, height in enumerate(remain_heights):
        if height > 0:
            rect = patches.Rectangle((i, 0), 0.6, height, 
                                       facecolor='lightgreen', edgecolor='green', linewidth=2)
            ax.add_patch(rect)
            ax.text(i + 0.3, height / 2, str(height), fontsize=14, ha='center', va='center', 
                    fontweight='bold', color='darkgreen')
        else:
            ax.text(i + 0.3, 0.3, '0', fontsize=14, ha='center', va='center', 
                    fontweight='bold', color='darkgreen')
        ax.text(i + 0.3, -0.3, f'第{i+1}根', fontsize=10, ha='center')
    ax.set_xlim(-0.5, 6)
    ax.set_ylim(-0.5, 6)
    ax.set_title('剩下的高度：0, 1, 2, 3, 4, 5', fontsize=14, fontweight='bold')
    ax.set_ylabel('高度', fontsize=12)
    ax.grid(True, alpha=0.3)
    
    # 图4：计算过程总结
    ax = axes[1, 1]
    ax.axis('off')
    
    # 显示计算过程
    calculation_text = """计算过程：

1. 剩下的高度：0 + 1 + 2 + 3 + 4 + 5 = 15

2. 总和是33，砍掉的总和：33 - 15 = 18

3. 每根砍掉：18 ÷ 6 = 3

4. 第一根木桩高度：3

5. 这6个连续数字：3, 4, 5, 6, 7, 8

验证：
3 + 4 + 5 + 6 + 7 + 8 = 33 √"""
    
    ax.text(0.5, 0.5, calculation_text, fontsize=12, ha='center', va='center',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    plt.suptitle('木桩法解决连续数字求和问题', fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.show()
    
    print("🎉 答案是：3, 4, 5, 6, 7, 8")
    print("=" * 50)

# 运行解题程序
solve_consecutive_numbers()
