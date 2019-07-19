to use this package, namely `test_init`

```

~/kouui $ ipython
Python 3.6.7 | packaged by conda-forge | (default, Feb 28 2019, 02:16:08)
Type 'copyright', 'credits' or 'license' for more information
IPython 7.5.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import sys; sys.path.append("./python/")                                

In [2]: from test_init import mod1                                              
@ test_init.__init__
@ test_init.mod2.__init__

In [3]:
```

that is, `import` starts from the package name and end with the name of module xxxx.py.
