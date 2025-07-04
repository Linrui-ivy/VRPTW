# tests/debug_cg.py

import functools
import vrpy.vrp as vrp_module

called = False

_original_find_columns = vrp_module.VehicleRoutingProblem._find_columns

def _trace_find_columns(self, *args, **kwargs):
    global called
    called = True
    print(">>> [DEBUG] _find_columns was called！")
    return _original_find_columns(self, *args, **kwargs)

vrp_module.VehicleRoutingProblem._find_columns = _trace_find_columns
