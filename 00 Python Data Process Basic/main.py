"""
基础知识
"""
import numpy as np
import pandas as pd

# numpy：python数值计算扩展，用于矩阵计算
# 1.普通list
data1 = [1, 2, 3, 5, 6, 7, 8, 9]
# 使用numpy的数组
array1 = np.array(data1)
print(array1)
# 2.多维数组
data2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
array2 = np.array(data2)
print(array2)
print(array2.dtype)
# 3.类型转换
array2_str = array2.astype("str")
print(array2)
print(array2_str.dtype)
# 4.数值计算
# 直接向量化计算（矩阵计算）
print(array1 + 1)
print(array1 * array1)
print(array1 * array1)
print(array1[2])
# 范围访问（切片访问）
print(array1[-2:])
array1[1] = 0
print(array1)
print(array2[0])
# 平均值
print(array2.mean())
# 求和
print(array2.sum())
# 遍历
for a in array2:
    print(a)
# 条件赋值
array2[np.where(array2 > 0)] = 111
print(array2)

print(np.ones((2, 3)))
m = np.matrix("1 2;3 4")
print(m.T)
print(m.H)

# pandas：基于numpy的数据分析工具，能方便操作大型数据集
# 和numpy主要区别是加入了索引，即map中的key，list和map的区别
# 1.Series
s = pd.Series([1, 2, 3, 4, 5])
print(s)
s = pd.Series([1, 2, 3, 4, 5], index=["a", "b", "c", "d", "e"])
print(s)
print(s.index)
print(s["a"])
print(s[["a", "b"]])
# 直接从字典中创建
d = {"what": "什么东西", "when": "什么时候"}
print(pd.Series(d))
print(pd.Series(d, index=["what", "when", "how"]))

# 2.DataFrame
# 强一些的Series
d = {"name": ["张三", "李四", "王五"],
     "sex": ["🚹", "♂", "🚺"],
     "age": [1, 2, 3],
     }
df = pd.DataFrame(d)
print(df)
df.info()
#  类型转换类似numpy，不过可以直接用点表示访问下标
print(df.age.astype("str"))
print(df["age"].astype("str"))
# 下标访问行
print(df.ix[0])
# 切片访问行
print(df[0:2])
# 赋值
df.age = 22
print(df)
df.age = [3, 4, 5]
print(df)
# 注意不能用点号形式新建
df["country"] = ["China", "America", "India"]
print(df)
print(df.index)
# 数据选取
print(df[["age", "sex"]])
print(df[df.age > 4])
print(df[df.sex == "🚹"])
print(df.sex == "🚹")
print((df.sex == "🚹") & (df.age < 4))
print(df[(df.sex == "🚹") & (df.age < 4)])
print(df.query('(age==3 and sex=="🚺") or (age <8 and sex=="♂")'))

# 计算
print(df.age * 10)

df1 = pd.DataFrame(np.arange(4).reshape(2, 2), columns=["a", "b"])
df2 = pd.DataFrame(np.arange(6).reshape(2, 3), columns=["a", "b", "d"])
print(df1 + df2)
print(df1.add(df2, fill_value=0))

# scipy：基于numpy的科学计算包，包括统计，线性代数等工具
"""
其在以下方面有着优秀的函数库：
1.线性代数
2.数值积分
3.插值
4.优化
5.随机数生成
6.信号处理
7.图像处理
8.其他

模块名 应用领域
scipy.cluster 向量计算/Kmeans
scipy.constants 物理和数学常量
scipy.fftpack 傅立叶变换
scipy.integrate 积分程序
scipy.interpolate 插值
scipy.io 数据输入输出
scipy.linalg 线性代数程序
scipy.ndimage n维图像包
scipy.odr 正交距离回归
scipy.optimize 优化
scipy.signal 信号处理
scipy.sparse 稀疏矩阵
scipy.spatial 空间数据结构和算法
scipy.special 一些特殊的数学函数
scipy.stats 统计
"""
