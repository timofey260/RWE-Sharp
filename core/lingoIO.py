import json.decoder
import re
import json as jsonenc


def tojson(string: str, replacement: str = None, log=False):
    try:
        closebracketscount = string.count("]")
        openbracketscount = string.count("[")
        t = string
        if closebracketscount > openbracketscount:
            t = t[:-1]
        t = t.replace("#Data:", "#data:") \
            .replace("#Options:", "#options:") \
            .replace("[#", "{#") \
            .replace("point(", "\"point(") \
            .replace("rect(", "\"rect(") \
            .replace("color(", "\"color(") \
            .replace("color (", "\"color(") \
            .replace(")\"", ")") \
            .replace(")", ")\"") \
            .replace("void", "0")
        count = 0
        m = list(t)
        brcount = 0
        for i in m:
            if i == "{":
                localcount = 0
                v = count
                while v < len(m):
                    if m[v] == "[" or m[v] == "{":
                        localcount += 1
                    elif m[v] == "]" or m[v] == "}":
                        localcount -= 1
                        if localcount == 0:
                            m[v] = "}"
                            break
                    v += 1
            count += 1
            if i in ["{", "["]:
                brcount += 1
            elif i in ["}", "]"]:
                brcount -= 1
                if brcount == 0:
                    m = m[:count+1]
                    break
        t = "".join(m)
        t = t.replace("#", "\"").replace(":", "\":").replace("1\":st", "1':st").replace("2\":nd", "2':nd").replace("3\":rd", "3':rd")
        # print(t)
        if t.replace(" ", "") != "":
            if replacement is not None:
                return {**tojson(replacement), **json.loads(t)}
            return json.loads(t)
        else:
            if replacement is not None:
                return tojson(replacement)
            return {}
    except:
        print("fixing, just wait bro we got it bro")
        if replacement is None:
            raise
        return tojson(replacement)


def tolingo(string: dict):
    s = jsonenc.dumps(string)
    # print(s)
    t = s.replace("\"point(", "point(").replace("\"rect(", "rect(").replace("\"color(", "color(") \
        .replace(")\"", ")").replace("{", "[").replace("}", "]").replace("'", "")
    t = re.sub(r"\"([a-zA-Z]+[0-9]*)\":", r"#\1:", t)
    # print(t)
    return t


def fromarr(col: str, mark: str):
    s = col.replace(mark + "(", "")
    s = s.replace(",", " ")
    s = s.replace(")", "")
    a = []
    for i in s.split():
        n = float(i)
        if float(i) == int(float(i)):
            n = int(float(i))
        a.append(n)
    return a


def point(col: list | tuple):
    return f"point({col[0]}, {col[1]})"


def frompoint(col: str):
    return fromarr(col, "point")


def makearr(col: list | tuple, mark: str):
    return f"{mark}({col[0]}, {col[1]})"
