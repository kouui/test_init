print("@ test_init.__init__")

#-----------------------------------------------------------------------------

##from .import Constants as Cst

# 方针：
# 1 对于Constants这样的定义变量的configuration文件，我们import到文件名
#
# 2 对于只定义了函数的package（文件），我们import到文件名
#
# 3 为了让在import了module（文件夹）的时候可以使用module.package.function()
#   在文件夹的__init__.py文件里头要import文件夹里的各个package（和module），也就是说
#   1. 如果文件夹 A 里头有 xxxx.py 文件，则在 A 里的 __init__.py必须要有一句 from . import xxxx
#   2. 如果文件夹 A 里头有文件夹 AA,AA里头有 xxxx.py 文件,那么问了可以使用
#      from A.AA import xxxx 必须在 A 里的 __init__.py必须要有一句 from . import AA
#
#
# 4 文件夹的__init__.py文件里可以定义当前文件夹相关的一些信息类的变量，如__version__
#
# 5 不在 __init__.py 文件里 import Constants.py 之类的文件

#-----------------------------------------------------------------------------

##from . import mod1
##from . import mod11
# 只有这么import了才能像下面这么使用。
# >>> import test_init
# >>> test_init.mod1.func1()
# 否则单纯`import test_init`什么都干不了

# 不能使用 test_init.xxxx
# test_init.xxxx 的使用必须在 test_init.__init__.py 中
# from . import xxxx

# from test_init import mod2 与 import test_init 没关系
# 只要文件夹结构在就行

# >>> from test_init import mod1
# 的时候 test_init.__init__.py 也会被执行

# 但因为这是最高层的文件夹，所以不这么做，因为使用的时候一般不会 import test_init
# 而是 from test_init import mod1


#-----------------------------------------------------------------------------

from . import mod2
# 要能使用 from test_init.mod2 import mod2_1, 必须要有上面这一句

#-----------------------------------------------------------------------------
