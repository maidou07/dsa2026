import timeit
# 1. 在固定dict大小 = 1000下在不同key取item
print("验证1：固定dict大小 = 1000，在不同key执行get item")
for key in [0, 499, 999]:
    setup = "dic = {k:k for k in range(1000)}"
    run = f"x = dic[{key}]"
    t = timeit.Timer(run, setup)
    total = t.timeit(number=1000000)
    print(f"在 key = {key} 取数1000000次所用时间：{total:.5f}秒")
print("---")
# 2. 改变dict大小，在相同key取item
print("验证2：改变dict大小，在相同key执行get item")
dict_sizes = [1000, 10000, 100000]
for i in dict_sizes:
    setup = f"dic = {{k:k for k in range({i})}}"
    run = "x = dic[0]"
    t = timeit.Timer(run, setup)
    total = t.timeit(number=1000000)
    print(f"dict大小为{i}下：在 key = 0 处取数1000000次所用时间：{total:.5f}秒")
print("---")
# 3. 在固定 dict大小 = 1000 下在不同key执行set item
print("验证3：固定dict大小 = 1000，在不同key执行set item")
for key in [0, 499, 999]:
    setup = "dic = {k:k for k in range(1000)}"
    run = f"dic[{key}] = 0"
    t = timeit.Timer(run, setup)
    total = t.timeit(number=1000000)
    print(f"在 key = {key} 修改1000000次所用时间：{total:.5f}秒")
print("---")
# 4. 改变dict大小，在相同key 执行 set item
print("验证4：改变dict大小，在相同key执行set item")
dict_sizes = [1000, 10000, 100000]
for i in dict_sizes:
    setup = f"dic = {{k:k for k in range({i})}}"
    run = "dic[0] = 0"
    t = timeit.Timer(run, setup)
    total = t.timeit(number=1000000)
    print(f"dict大小为{i}下：在 key = 0 处修改1000000次所用时间：{total:.5f}秒")
