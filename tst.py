
x = {'a':9,'b':2,'c':3}

sorted_x = sorted(x.items(), key=lambda kv: kv[1])
print(sorted_x)
