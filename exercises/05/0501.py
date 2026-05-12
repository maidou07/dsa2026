class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size
        self.count = 0 # 新增：元素计数器

    def hashfunction(self, key):
        return key% self.size

    def rehash(self,oldhash):
        return (oldhash+ 1)% self.size

    # 新增：_resize 实现扩容操作
    def _resize(self):
        temp_slots = self.slots
        temp_data = self.data

        # 翻倍
        self.size = self.size * 2
        self.slots = [None] * self.size
        self.data = [None] * self.size
        self.count = 0 # 重新计数

        # 遍历旧数组，rehash
        for i in range(len(temp_slots)):
            if temp_slots[i] != None:
                self.put(temp_slots[i], temp_data[i])

    def put(self,key,data):
        hashvalue = self.hashfunction(key)
        
        # 新增：扩容判断：储存超过一半
        if self.count > self.size // 2:
            self._resize()

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
            self.count += 1 # 计数
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data  #replace
            else:
                nextslot = self.rehash(hashvalue)
                while self.slots[nextslot] != None and \
                      self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot)

                if self.slots[nextslot] == None:
                    self.slots[nextslot]=key
                    self.data[nextslot]=data
                    self.count += 1 #计数
                else:
                    self.data[nextslot] = data #replace

    def get(self,key):
        startslot = self.hashfunction(key)

        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and \
                          not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position=self.rehash(position)
                if position == startslot:
                    stop = True
        return data

# 测试用例
print("0501")
print("- Hash自动扩容测试")
H = HashTable()
print(f"初始大小: {H.size}")
# 连续插入15个数据。
keys_to_insert = [54, 26, 93, 17, 77, 31, 12, 55, 20, 35, 45, 55, 65, 75, 85, 95]
for k in keys_to_insert:
    H.put(k, f"value_{k}")
    print(f"插入 {k} 完毕，当前元素个数: {H.count}，散列容量: {H.size}")
# 测试读取
print("- 扩容后读取测试：")
print(H.get(54))