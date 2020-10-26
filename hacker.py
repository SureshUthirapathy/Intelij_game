#
# import math
# print(math.floor(5.1))
#
# def sim_int(p=None,n=None,r=None):
#     p= int(input("enter p: "))
#     n= int(input("enter n: "))
#     r= int(input("enter r: "))
#
#     si = ( p * n * r)/100
#     return si
# #v = sim_int()
# #print(v)
#
#
# def ceil_floor(a=None,b=None):
#     a= eval(input("enter a: "))
#     b= eval(input("enter b: "))
#     print(a,b)
#     a = math.ceil(a)
#     b = math.floor(b)
#     return a,b
#
# # v1,v2 = ceil_floor()
# # print(v1,v2)
#
# from math import sqrt
# def lists():
#     lst = []
#     for i in range(1,6):
#         ele = float(input ("enter value {0}".format(i)))
#         ele = sqrt(ele)
#         lst.append(ele)
#     return lst , type(ele) ,dir()
#
#
# print(lists())
#
# import sys
#
# data = sys.stdin.readline()
# print(data.rstrip())
#
# data = sys.stdin.readline()
# print(data.rstrip())
#
# print("***********")
# for i in range(4):
#     data = sys.stdin.readline()
#     print(data.rstrip(),i)

a= " Hello World"
#" Hello World"
#"109876543210"
#"012345678901"
#"123456789012"
# #"210987654321"
# print(a[6:len(a)-3:1])  #" Wo"
# print(len(a))
# print(a.lower())
# print(a[:4] + 'p' + a[5:])
# print(a[5])

x = [1,2,4]
print(x)
it = iter(x)
print(it.__next__())
print(next(it))
print(next(it))
print(next(it))


