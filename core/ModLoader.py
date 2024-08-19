import os
import sys
import traceback
from core.Modify.Mod import Mod
from core.utils import log


def load_mod(path: str, manager, index) -> type | None:
    script = os.path.join(path, f"mod.py")
    if not os.path.exists(script):
        return None
    relative = os.path.exists(os.path.join(path, f"rel.txt"))
    # compiling
    with open(script) as f:
        text = f.read()
        try:
            code = compile(text, script, "exec")
            p, name = os.path.split(path)
            if "mod" not in code.co_names:
                return None
            if relative:
                sys.path.insert(0, p)
                exec(f"import {name}.mod")
                a = eval(f"{name}.mod.mod")
                del sys.modules[f"{name}.mod"]
                sys.path.remove(p)
                return [a, path] # NOQA
            else:
                sys.path.insert(0, path)
                import mod
                a = mod.mod
                del sys.modules["mod"]
                sys.path.remove(path)
                return [a, path]  # NOQA
        except Exception as e:
            log(f"Mod Loading failed!!! path: {path}", True)
            traceback.print_exc()
            return None
