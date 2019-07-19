print("@ test_init.mod2.__init__")

c_ = 3
# 这个c_无法被mod2内的任何package里的函数看见。
# 当有人以某种形式`import mod2`，便可以有
# mod2.c_
from .. import Constants as Cst
# 同理也无法被mod2内的任何package里的函数看见
# 只有当有人以某种形式`import mod2`，才可以有
# mod2.Cst

# 因此，__init__不适合用来定义module或者package范畴的公有变量。
