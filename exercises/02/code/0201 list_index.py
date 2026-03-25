import timeit

# 在固定list大小为1000下不同点取索引
print("验证1：固定list大小 = 1000，在不同点取索引")
for i in [0, 499, 999]:
    setup = "lst = list(range(1000))"
    run = f"x = lst[{i}]"
    t = timeit.Timer(run, setup)
    total = t.timeit(number = 1000000)
    print(f"在 index = {i} 取值1000000次所用时间：{total:.5f}秒")

print("---")

# 改变list大小，在相同点取索引
print("验证2：改变list大小，在相同点取索引")
list_sizes = [1000, 10000, 100000]
for i in list_sizes:
    setup = f"lst = list(range({i}))"
    run = "x = lst[0]"
    t = timeit.Timer(run, setup)
    total = t.timeit(number = 1000000)
    print(f"list大小为{i}下：在 index = 0 处取值1000000次所用时间：{total:.5f}秒")

