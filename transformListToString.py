print("this module has a function called transformListToString")

def transformListToString(toBeTransformed):
    m = ""
    for index, item in enumerate(toBeTransformed):
        if index != len(toBeTransformed) - 1:
            m += str(item)
            m += ", "
            print(m) # debug output
        else:
            m += "and "
            m += str(item)
            print(m) # debug output
            break
    return m
