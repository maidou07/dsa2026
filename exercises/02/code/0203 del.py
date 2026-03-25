import timeit
import matplotlib.pyplot as plt
import statistics
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
fig_path = os.path.join(current_dir, '..', 'img')
lst_times = []
dct_times = []

def test(N = 50000):
    global lst_times
    global dct_times

    for i in range(0, N, 1000):  # 枚举del操作的位置索引(list:index, dict:key)，间距为100

        # list 计时部分
        setup1 = f"lst = list(range({N}))"
        run1 = f"del(lst[{i}])"
        lst_time = timeit.Timer(run1, setup1).repeat(repeat = 100, number = 1)
        lst_times.append(statistics.mean(lst_time))

        # dict 计时部分
        setup2 = f"dct = {{k:k for k in range({N})}}"
        run2 = f"del dct[{i}]"
        dct_time = timeit.Timer(run2, setup2).repeat(repeat = 100, number = 1)
        dct_times.append(statistics.mean(dct_time))
test()
# plt绘图
plt.figure(figsize=(10, 6))
plt.plot(range(0, 50000, 1000), lst_times, label='List del x[i]', color='blue', marker='o', markersize=2)
plt.plot(range(0, 50000, 1000), dct_times, label='Dict del d[i]', color='red', linestyle='--')

plt.title('Comparison of del Operation: List vs Dictionary')
plt.xlabel('Index/Key to Delete (i)')
plt.ylabel('Avg Time for 100 Repetitions (seconds)')
plt.legend()
plt.grid(True)
plt.savefig(os.path.join(fig_path, 'del_comparison.png'))
plt.show()



