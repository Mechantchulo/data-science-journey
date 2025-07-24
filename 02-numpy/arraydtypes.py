import numpy as np
#checking datatypes using dtype

arr = np.array([1,2,3,4])
print(arr.dtype)#output -> int64 -> 64 reps 64bit system

arrs = np.array(['apple', 'mango', 'orange'])
print(arrs.dtype)#output <U6 -> unicode string type with length 6

#creating arrays with a defined datatype
arrd = np.array([1,2,3,4], dtype='S')
print(arrd.dtype) # |S1 means:
                   # S → Byte string (not Unicode)
                   # 1 → Each element is stored using 1 byte
                   # | → Byte order (irrelevant for byte strings, but used in numeric types)
                   
#an array with data type 4 bytes integer
arr4 = np.array([1,2,3,4], dtype='i4')
print(arr4.dtype) # i4 → 4-byte (32-bit) signed integer

#converting datatypes on existing arrays
#The best way to change the data type of an existing array, is to make a copy of the array with the astype() method.

arrc = np.array([1.1, 2.1, 3.1])

newarr = arrc.astype('i')

print(newarr)
print(newarr.dtype)

#Change data type from integer to boolean
arrb = np.array([1,0,3])
newarrb = arrb.astype(bool)
print(newarrb)#any non-zero = True
print(newarrb.dtype)