# import array
#
# a = array.array('i',[5,6,7,8])
# #b = array.array(5,6,7,8)
# c = array.array[1,2,3,4]
#
# #print(b)
# print(type(c))

def deleteProducts(ids, m):
    dict={}
    del_dict ={}
    for i in ids:
        if not (i in dict.keys()):
            dict[i] = 1
        else:
            dict[i] = dict[i] + 1
    print(dict)
    sorted_dict = sorted(dict.items(), key=lambda kv: kv[1])
    print(sorted_dict)
    print("***********")
    for i in sorted_dict:
        print(i)
        if i[1] < m:
            del_dict[i[0]] = i[1]
    print(del_dict)
    sorted_del_lst = sorted(del_dict.items(), key=lambda kv: kv[1])
    print("***********")
    print(sorted_del_lst)
    cnt = 0
    for i in sorted_del_lst:
        if ((i[1] - m ) <= 0):
             m = m - i[1]
             cnt = cnt + 1
    if cnt == 0 and m in dict.values():
        cnt = 1

    print(sorted_del_lst,m,cnt)
    print(len(dict.keys()) - cnt )


ids = [1,1,1,2,2,3,3,4,4,5,2,3,4,5,6]
ids = [3,4,4,5,6]
m = 3

deleteProducts(ids,m)
