print("@ test_init.__init__")

from . import mod1
# 只有这么import了才能像下面这么使用。
# >>> import test_init
# >>> test_init.mod1.func1()
# 否则单纯`import test_init`什么都干不了
# 而且这么做了甚至连mod2都一起import了因为mod1.py里头有这么一句
# `from .mod2 import mod2_1`


# 方针：
# 1 对于Constants这样的定义变量的configuration文件，我们import到文件名
# 2 对于只定义了函数的package（文件），我们import到函数名
#   2.1 如果要使用文件里的多个函数，import到文件名也行
#   2.2 如果会出现重复的函数名，那么必须使用文件名区分
# 3 为了让在import了module（文件夹）的时候可以使用module.package.function()
#   在文件夹的__init__.py文件里头要import文件夹里的各个package（和module）
# 4 文件夹的__init__.py文件里可以定义当前文件夹相关的一些信息类的变量，如__version__
