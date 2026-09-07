#without slicing
s = input('enter string:')
rev = ""
for ch in s:
    rev = ch + rev
print("reversed string:",rev)

'''enter string:python
reversed string: nohtyp'''


#with slicing
s = input('enter string:')
print("reversed string:",s[::-1])


'''enter string:python
reversed string: nohtyp'''
