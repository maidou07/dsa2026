import timeit
import statistics, math

# 枚举数据大小
sizes = [10000, 20000, 40000, 80000, 160000]

def test():
    # 循环计算sort时间
    for i in sizes:
        setup = f"import random; lst = [random.randrange(10*6) for _ in range({i})]"
        run = "lst.sort()"
        t = timeit.Timer(run, setup)
        sort_time = statistics.mean(t.repeat(repeat = 1000, number = 1))   #取1000次平均 减小涨落影响
        ratio = sort_time / (i * math.log(i))   # 计算time/nlogn 证明O(nlogn)
        
        print(f"{i} : {10**3*sort_time:.3f}ms {10**9*ratio:.3f}*10^(-9)")

test()

