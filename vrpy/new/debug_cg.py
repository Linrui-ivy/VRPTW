# tests/debug_cg.py

import functools
import vrpy.vrp as vrp_module

# 用一个全局变量记录 _find_columns 有没有被调用
called = False

# 先把原来的方法存下来
_original_find_columns = vrp_module.VehicleRoutingProblem._find_columns

# 然后包装它
def _trace_find_columns(self, *args, **kwargs):
    global called
    called = True
    print(">>> [DEBUG] _find_columns 被调用了！")
    return _original_find_columns(self, *args, **kwargs)

# 最后替换类的方法
vrp_module.VehicleRoutingProblem._find_columns = _trace_find_columns
