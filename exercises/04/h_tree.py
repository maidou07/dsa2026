import turtle
import random

def tree(branchLen, t):

    if branchLen > 5:
        # 1. 树枝的粗细变化：随着树枝变短，相应变细
        t.pensize(max(1, branchLen // 10)) 
    
        # 2. 树枝的颜色变化；树干为棕色，树叶为绿色（用branchLen < 30 判定）
        if branchLen < 30:
            t.pencolor("forest green")
        else:
            t.pencolor("saddle brown")

        t.forward(branchLen)
        
        # 3. 随机倾斜角度
        right_angle = random.randint(10, 20)
        left_angle = random.randint(10, 20)
        
        # 4. 随机长短变化：每次缩短的长度在 12~20 之间随机
        deltaLen_r = random.randint(12, 20)
        deltaLen_l = random.randint(12, 20)
        
        # 绘制右侧树枝
        t.right(right_angle)
        tree(branchLen - deltaLen_r, t)
        
        # 绘制左侧树枝
        t.left(right_angle + left_angle)
        tree(branchLen - deltaLen_l, t)
        
        # 角度回正并返回原位
        t.right(left_angle)
        t.penup()
        t.backward(branchLen)
        t.pendown()

t = turtle.Turtle()
Win = turtle.Screen()

# 初始化海龟的位置、方向和速度
t.speed(0)
t.left(90)
t.penup()
t.backward(200)
t.pendown()
# 初始树干长度设为 120， 开始绘制
tree(120, t)

Win.exitonclick()