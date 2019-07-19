# 这里的Cst.m_与
# import test_init 后的 test_init.Cst.m_ 有相同的id()
# 也就是说内存地址相同

# In [1]: import test_init
# @ test_init.__init__
#
# In [2]: from test_init import mod1
# @ test_init.mod2.__init__
#
# In [3]: mod1.func1()
# 1.23 , inside mod2.mod2_1.func2_1()
# 1.23 , inside mod1.func1()
#
# In [4]: mod1.Cst.a_
# Out[4]: array([1], dtype=uint8)
#
# In [5]: mod1.Cst.a_[0] = 2
#
# In [6]: test_init.Cst.a_
# Out[6]: array([2], dtype=uint8)
from . import Constants as Cst
# 如果在这里不 from . import Constants as Cst
# 无论如何编写 test_init.__init__.py
# 都无法在 func1() 里使用 Cst

from .mod2 import mod2_1

def func1():
    mod2_1.func2_1()
    print(Cst.m_, ", inside mod1.func1()")
