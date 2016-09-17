def myhash(s):
    h=1
    for c in s:
        intC=ord(c)
        h=ord(c)*h
        h=(h>>32)+(h<<32)
        h=h^((intC)or(intC<<16)or(intC<<32)or(intC<<48)or(intC<<8)or(intC<<24)or(intC<<56)or(intC<<40))
        h=h%7205759403792700000
    return h
