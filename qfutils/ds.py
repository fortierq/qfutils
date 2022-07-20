imperative = dict | list


def union_json(d1: imperative, d2: imperative) -> imperative:
    if isinstance(d1, dict):
        for k in d1:
            if k in d2:
                d1[k] = union_json(d1[k], d2[k])
        for k in d2:
            if k not in d1:
                d1[k] = d2[k]
    if isinstance(d1, list):
        if d2:
            d1 = list(set(d1) | set(d2))
    return d1
