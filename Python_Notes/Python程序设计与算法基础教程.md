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
Python 程序由**模块**（.py源文件）组成。

模块包含语句，**语句**是 Python 程序的**基本构成元素**。




