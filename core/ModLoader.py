import os
import sys
import traceback
from core.Modify.Mod import Mod, ModInfo
from core.utils import log
from core.info import PE

# this code is as save as 2 towers at september 11th


def load_mod(path: str, manager, index) -> type | None:
    info = os.path.join(path, f"modinfo.json")
    script = os.path.join(path, f"mod.py")
    if not os.path.exists(info):
        return None
    # compiling
    modinfo = ModInfo.import_from_file(open(info))
    log(f"Loading {modinfo.title} by {modinfo.author}({modinfo.id})")
    if not os.path.exists(script):
        log(f"No script found for {modinfo.id}!", True)
        return None
    with open(script) as f:
        text = f.read()
        try:
            code = compile(text, script, "exec")
            if modinfo.mod_class not in code.co_names:
                return None

            sys.path.insert(0, path)
            # todo requirements
            try:
                exec(f"from mod import {modinfo.mod_class}")
                a = eval(modinfo.mod_class)
            except ImportError:
                pass
            # import mod
            # a = mod.mod
            if a is None:
                return None
            del sys.modules["mod"]
            sys.path.remove(path)
            log(f"{modinfo.id} loaded!")
            return [a, path]  # NOQA
        except Exception as e:
            log(f"Mod Loading failed for {modinfo.id}!!!", True)
            traceback.print_exc()
            return None


def old_load_mod(path: str, manager, index) -> type | None:
    script = os.path.join(path, "mod.py")
    if not os.path.exists(script):
        return None
    relative = os.path.exists(os.path.join(path, "rel.txt"))
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
