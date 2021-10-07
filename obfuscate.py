import sys, random

def randomString(strSize, allowedChars):
    return ''.join(random.choice(allowedChars) for x in range(strSize))

def obfuscateStr(str, variables):
    if str[:1] == ":":
        return str
    obfuscated = ""
    for char in str:
        if char == "%":
            if obfuscated[-1:] == "!":
                obfuscated = obfuscated[:-1] + "%"
                print(obfuscated)
            else:
                char = "!"
        if char in variables.keys():
            char = "%" + variables[char] + "%"
        obfuscated = obfuscated + char
    return obfuscated


# Initialize variables
obfuscated = "@echo off\nsetlocal enableDelayedExpansion\n"
variables = {}
for char in "ets abcdfghijklmnopqruvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    while True:
        name = randomString(int(sys.argv[2]), "abcdefghijklmnopqrstuvwxyz")
        if name in variables.values():
            continue
        break
    obfuscated = obfuscated + obfuscateStr("set " + name + "=" + char, variables) + "\n"
    variables[char] = name
    
print(variables)

with open(sys.argv[1]) as f:
    batch = f.readlines()
    
for line in batch:
    obfuscated = obfuscated + obfuscateStr(line, variables)
        
with open('obfuscated.bat', 'w') as f:
    f.write(obfuscated)