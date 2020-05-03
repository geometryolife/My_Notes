## <center>第一章 Python 概述</center>
**解释型、面向对象** *脚本语言*

**特点：** 简单、高级、面向对象、可扩展性、免费和开源、可移植性、丰富的库、可嵌入性

**pip:** 安装和管理 Python 扩展包

**setuptools:** 发布 Python 包

```
# 安装最新版
python -m pip install SomeProject
# 安装某个版本
python -m pip install SomeProject==1.4
# 安装某个范围版本
python -m pip install SomeProject>=1,<2
# 安装某个兼容版本
python -m pip install SomeProject~=1.4.2
# 更新安装包
python -m pip install -U SomeProject

# Python\Scripts中pip.exe、pip3.exe、pip3.7.exe与pip等价
pip install numpy

# "[WinError 5]拒绝访问"，使用管理员或 -user 安装到个人目录
```

```
# 更新 pip 和 setuptools
python -m pip install -U pip setuptools
# NumPy提供数组和矩阵处理，以及傅里叶变换等高效数值处理功能。
python -m pip install NumPy
# Matplotlib 是 Python 最著名的绘图库之一
python -m install Matplotlib
```

**解释器：** REPL(Read-Eval-Print-Loop)——在控制台上交互式地执行 Python 代码的过程。
- 解释器环境中的特殊变量“\_”

	```
	>>> 11 + 22
	33
	>>> _
	33
	>>> _ + 33
	66
	```

**命令行参数：** 在 Python 程序中导入 sys 模块，可以通过 sys.argv 访问命令行参数。argv[0] 为 Python 脚本名，argv[1]、argv[2] 分别为第一、第二个参数。

**Python 交互式帮助系统>>>** help()
```Python
# 列出安装的所有模块
help> modules
# 显示与 random 相关的模块
help> modules random
# 显示 random 模块的帮助信息
help> random
# 显示 random 模块的 random 函数的帮助信息
help> random.random

# 查看 Python 内置对象列表
>>> dir(__builtins__)
```

## <center>第二章 Python 语言基础</center>
#### 概述
Python 程序由**模块**（.py源文件）组成。

模块包含语句，**语句**是 Python 程序的**基本构成元素**。语句通常包含**表达式**，而表达式由操作符和运算符构成，用于创建和处理**对象**。

计算机->数据（对象）->运算操作

Python -> 一切皆对象 -> 内存块（特定值、特定类型的运算操作）

*对象* -> **标识、类型、值**

标识：唯一、内存&位置、**id(obj1)**

类型：所属类型、取值范围、处理操作、**type(obj1)**

值：**print(obj1)**

#### 对象和引用
- **使用字面量创建实例对象**
	+ 字面量在Python语句中解释为表达式
	+ Python 基于字面量创建相应的的数据类型的对象
```Python
123  # 输出123
"abc"  # 输出‘abc’
```

- **使用类对象创建实例对象**
	+ **类对象(参数)**
	+ `def` 创建函数对象
	+ `class` 创建类对象
```Python
int(12)
complex(1, 2)  # 输出：(1+2j)
```

- **数据类型**
- **变量和对象的引用**
	+ Python 对象是位于计算机内存中的一个内存数据块
	+ 引用对象必须赋值给变量
	+ 指向对象的引用即**变量**
	+ 变量名必须为有效的标识符


