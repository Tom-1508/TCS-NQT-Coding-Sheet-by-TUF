def octal_to_binary(octal_str):
    mapping = {
        '0' : "000",
        '1' : "001",
        '2' : "010",
        '3' : "011",
        '4' : "100",
        '5' : "101",
        '6' : "110",
        '7' : "111"
    }
    
    bin = ""
    for ch in octal_str:
        bin = bin + mapping[ch]
    
    return bin.lstrip("0") or "0"

print(octal_to_binary("65"))   # 110101
print(octal_to_binary("10"))   # 1000