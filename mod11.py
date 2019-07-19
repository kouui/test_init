
from . import Constants as Cst
# 如果在这里不 from . import Constants as Cst
# 无论如何编写 test_init.__init__.py
# 都无法在 func11() 里使用 Cst
def func11():
    print(Cst.m_, ", inside mod11.func11()")
