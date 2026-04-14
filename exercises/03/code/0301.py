pri = {"+":1, "-":1, "*":2, "/":2}
ops = []    # 直接用list实现栈
nums = []
# 封装计算函数，提升代码整洁度
def cal(op):
    global nums
    a, b = nums.pop(), nums.pop()
    if op == '+': nums.append(b + a)
    elif op == '-': nums.append(b - a)
    elif op == '*': nums.append(b * a)
    elif op == '/': nums.append(b // a)
# 格式化表达式
def tokenize(s):
    cache = []  # 数位 缓存
    tokens = []
    for char in s:
        if char.isspace():
            continue
        if char in ['(',')','+','-','*','/']:
            if cache:
                tokens.append(''.join(cache))
                cache.clear()
            tokens.append(char)
        else:
            cache.append(char)
    if cache:
        tokens.append(''.join(cache))
        cache.clear
    return tokens
# 中缀表达式直接计算
def infix_to_value(tokens):
    global nums, ops
    for token in tokens:    # 迭代处理中缀
        if token == '(':
            ops.append(token)
        elif token == ')':
            while ops[-1] != '(':   # 清算括号内表达式
                op = ops.pop()
                cal(op)
            ops.pop()
        elif token in pri:
            while ops and ops[-1] in pri and pri[ops[-1]] >= pri[token]:    # 优先级高和平级先到的全部出栈
                op = ops.pop()
                cal(op)
            ops.append(token)   # 新op入栈
        else:   # 数字直接入栈
            nums.append(int(token))
    while ops:
        op = ops.pop()
        cal(op)
    return nums[-1]
print(infix_to_value(tokenize(input())))


