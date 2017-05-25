import itertools

table = {
    ("1", "1", "1"): "31",
    ("1", "1"): "21",
    ("1", ): "11",
    ("2", "2", "2"): "32",
    ("2", "2"): "22",
    ("2",): "12",
    ("3", "3", "3"): "33",
    ("3", "3"): "23",
    ("3",): "13",
}
prec = "1"
result =[1]
for i in range(30):
    prec = "".join(table[tuple(l)] for e, l in itertools.groupby(prec))
    result.append(int(prec))
    print (result)
print (len(str(result[30])))