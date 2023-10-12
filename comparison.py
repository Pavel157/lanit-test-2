def compare (raw):
    raw1 = list(raw)
    for elem in raw1:
        if elem == "<":
             raw2 = raw.partition("<")
             a = int(raw2[0])
             b = int(raw2[2])
             c = a<b
        elif elem == ">":
            raw2 = raw.partition(">")
            a = int(raw2[0])
            b = int(raw2[2])
            c = a > b
    return c