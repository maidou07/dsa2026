def generate_pascal_triangle(n): # n: number_of_row
    if n == 1:
        return [[1]]
    else:
        # 获取递归结果
        tri = generate_pascal_triangle(n-1) 
        last_row = tri[-1]
        # 构建新行
        current_row = [1]
        for i in range(len(last_row)-1):
            current_row.append(last_row[i] + last_row[i+1])
        current_row.append(1)
        # 返回完整三角形
        tri.append(current_row)
        return tri

# 调用递并输出杨辉三角
def pascal_triangle(number_of_row = 10):
    triangle = generate_pascal_triangle(number_of_row)
    width = len(' '.join(map(str, triangle[-1])))
    for row in triangle:
        print(' '.join(map(str, row)).center(width))

pascal_triangle()