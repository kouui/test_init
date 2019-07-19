# 虽然这么import了
# 但是这里的Cst.m_
# import test_init
# 的 test_init.Cst.m_ 有相同的id()
# 也就是说内存地址相同

# In [1]: import test_init
# @ test_init.__init__
#
# @ test_init.mod3.__init__
# @ test_init.mod2.__init__
# In [2]: from test_init.mod3.mod31 import mod31_1
# @ test_init.mod3.mod31.__init__
#
# In [3]: mod31_1.func31_1()
# 1.23 , inside mod3.mod31_1.func31_1()
#
# In [4]: mod31_1.Cst.a_
# Out[4]: array([1], dtype=uint8)
#
# In [5]: mod31_1.Cst.a_[0] = 2
#
# In [6]: test_init.Cst.a_
# Out[6]: array([2], dtype=uint8)

from ... import Constants as Cst

def func31_1():
    print(Cst.m_, ", inside mod3.mod31_1.func31_1()")
