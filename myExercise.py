import sys

f = open(sys.argv[1])
list_argv = list(sys.argv[2].split(","))
dic = {}
for i in f:
    x = i.split(":")
    dic.update({x[0]: x[1].rstrip("\n")})
for i in list_argv:
    try:
        print("Name: {}, University: {},{}".format(i,str(dic[i].split(",")[0]),str(dic[i].split(",")[1])))
        assert i in dic.keys()
    except:
        print("No record of ‘{}’ was found!".format(i))
