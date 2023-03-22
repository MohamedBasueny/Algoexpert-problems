def caesarCipherEncryptor(string, key):
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    print(len(letters))
    newStirng=[]
    for l in string : #  O(N)T  ,   O(N)S
        newletter = letters[letters.index(l)+ key] if (letters.index(l)+key) <= 25 else letters[(letters.index(l)+ key)%26]
        newStirng.append(newletter)
    return "".join(newStirng)
string = "xyz"
key = 54
print(caesarCipherEncryptor(string, key))