# a = 97
# z = 122
def solution(s, skip, index):
    new = ''
    for S in s:
        count = change = 0
        while count != index:
            change += 1
            if chr((((ord(S)+change)-97) % 26) + 97) not in skip:count += 1             
        new += chr((((ord(S)+change)-97) % 26) + 97)
    print(ord('a'))
    print(ord('z'))
    print(ord('A'))
    print(ord('Z'))
    print(chr(97))
    
    return new