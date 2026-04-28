import turtle

def koch(t, length, depth):
    if depth == 0:
        t.forward(length)
    else:
        # 线段分3份，中间凸起为等边三角形的两条边，共绘制4条
        koch(t, length / 3, depth - 1)
        t.left(60)
        koch(t, length / 3, depth - 1)
        t.right(120)
        koch(t, length / 3, depth - 1)
        t.left(60)
        koch(t, length / 3, depth - 1)
    
t = turtle.Turtle()
Win = turtle.Screen()
t.speed(0)
t.penup()
t.backward(300)
t.pendown()
# 绘制5阶的Koch曲线
koch(t, 600, 5)
Win.exitonclick()
