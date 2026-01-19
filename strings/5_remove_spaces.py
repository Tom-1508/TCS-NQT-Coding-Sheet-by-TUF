def remove_spaces(s):
    res = ""
    for ch in s:
        if ch != " ":
            res += ch
    return res

print(remove_spaces("Hi Tamal Bro"))  # HiTamalBro

