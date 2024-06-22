import os
import sys
import traceback
from core.Modify.Mod import Mod
from core.utils import log_to_load_log


def load_mod(path: str, manager, index) -> Mod | None:
    script = os.path.join(path, f"mod.py")
    if not os.path.exists(script):
        return None
    # compiling
    with open(script) as f:
        text = f.read().replace("from atom import manager\n", "")
        try:
            code = compile(text, script, "exec")
            p, name = os.path.split(path)
            sys.path.insert(0, path)
            import mod
            a = mod.mod
            del sys.modules["mod"]
            sys.path.remove(path)
            if "mod" not in code.co_names:
                return None
            return a(manager)  # NOQA
        except Exception as e:
            log_to_load_log(f"Mod Loading failed!!! path: {path}", True)
            traceback.print_exc()
            return None
