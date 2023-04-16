def merge(values):
    res = {}
    [res.setdefault(k, set()).add(v) for i in values for k, v in i.items()]
    return res
