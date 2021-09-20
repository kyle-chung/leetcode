给你 二维 平面上两个 由直线构成的 矩形，请你计算并返回两个矩形覆盖的总面积。

每个矩形由其 左下 顶点和 右上 顶点坐标表示：

第一个矩形由其左下顶点 (ax1, ay1) 和右上顶点 (ax2, ay2) 定义。
第二个矩形由其左下顶点 (bx1, by1) 和右上顶点 (bx2, by2) 定义。

示例 1：

输入：ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = 0, by1 = -1, bx2 = 9, by2 = 2
输出：45

def computeArea(self, A, B, C, D, E, F, G, H):
        if D <= F or E >= C or B >= H or G <= A:
            return (D-B) * (C-A) + (H-F) * (G-E)
        
        left = max(E, A)
        right = min(C, G)
        up = min(H, D)
        down = max(F, B)
        return (D-B) * (C-A) + (H-F) * (G-E) - (up-down) * (right-left)
      
# 自创
class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        sum = (ax2-ax1)*(ay2-ay1) + (bx2-bx1)*(by2-by1)
        set1 = set(range(ax1,ax2+1))
        set2 = set(range(ay1,ay2+1))
        set3 = set(range(bx1,bx2+1))
        set4 = set(range(by1,by2+1))

        x = set1.intersection(set3)
        y = set2.intersection(set4)

        if not x or not y: return sum
        return sum - (len(x)-1)*(len(y)-1)
