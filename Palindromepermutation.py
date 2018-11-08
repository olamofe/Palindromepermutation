def Palindromepermutation(name):
    from collections import Counter
    count = Counter()
    name = str(name)
    check = str(name.isalnum())
    if(check == "False"):
        chrname = ""
        for char in name:
            if char.isalnum():
                chrname += char
        name = chrname.lower()
        print(name)
    
    for words in name:
        count[words] += 1
## printing dictionary
    print(dict(count))
    count = dict(count)
    valcount = 0
    for keys in count:
        if int(count[keys])%2 != 0:
            valcount += 1
            if valcount > 1:
                return False
        else:
            pass
    return True
        

check = Palindromepermutation("Tact cOA")
print(check)