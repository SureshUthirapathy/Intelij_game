def deleteProducts(ids, m):
    dict={}
    del_dict ={}
    for i in ids:
        if not (i in dict.keys()):
            dict[i] = 1
        else:
            dict[i] = dict[i] + 1
    sorted_dict = sorted(dict.items(), key=lambda kv: kv[1])
    for i in sorted_dict:
        if i[1] < m:
            del_dict[i[0]] = i[1]
    sorted_del_lst = sorted(del_dict.items(), key=lambda kv: kv[1])
    cnt = 0
    for i in sorted_del_lst:
        if ((i[1] - m ) <= 0):
            m = m - i[1]
            cnt = cnt + 1
    if cnt == 0 and m in dict.values():
        cnt = 1

    return(len(dict.keys()) - cnt )


ids = [1,1,1,2,2,3,3,4,4,5,2,3,4,5,6]
ids = [3,4,4,5,6]
m = 0

v1 = deleteProducts(ids,m)

print(v1)
