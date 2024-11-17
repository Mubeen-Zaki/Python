string = "amazing"

dict_ds = dict()
for i in string:
    if i in dict_ds.keys():
        dict_ds[i] += 1
    else:
        dict_ds[i] = 1

for i in dict_ds.items():
    if i[1] == 1:
        print(i[0])
        break