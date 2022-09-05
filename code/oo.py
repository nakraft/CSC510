import typing

class o:
    def __new__(self, obj) -> str:
        if obj is None:
            return ""
        if not isinstance(obj, dict):
            return str(obj)

        def show(k, v) -> str:
            if "^_" not in str(k):
                v = o(v)
                return f":{k} {v}"
    
        u = []
        for k,v in obj.items():
            u.append(show(k, v))
        u.sort()
        return  "{" + " ".join(u) + "}"        
    

def oo(t):
    print(o(t))
    return t
