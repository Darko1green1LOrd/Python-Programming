def dfind(source,what,where=1,listmode=False):
    if where != "all":
        if where < 1:raise Exception("Set position must be atleast 1")
    out = []

    if listmode:
        for i,each in enumerate(source):
            if each == what:
                out.append(i)


        if where == "all":output = out
        elif len(out) >= where:output = out[where-1]
        elif len(out) == 0:
            output = None
            print("No Matches Found")
        else:output = out[-1]

    else:
        value = []
        count = 0
        for i,each in enumerate(source):

            if (len(value) == len(what)):
                out.append(value)
                value = []
                count = 0

            if each == what[count]:
                value.append([each,i])
                count += 1

            else:
                value = []
                count = 0

        if (len(value) == len(what)):out.append(value)

        if where == "all":
            if len(what)==1:
                var=([every[0] for every in[[item[1] for item in each] for each in out]])
            else:
                var=([[item[1] for item in each] for each in out])
        elif len(out) >= where:var=([[item[1] for item in out[where-1]]])
        elif len(out) == 0:
            print("No Matches Found")
        else:var=([[item[1] for item in out[-1]]])
        output = (var[0][0] if len(what)==1 and where !="all" else var) if len(out) != 0 else None

    return(output)

def dcount(source,what):
    return(len(dfind(source,what,"all")))

def dreplace(source,old,new,count="all"):
    if count != "all":
        if count < 1:raise Exception("Set position must be atleast 1")
    src = list(source)
    limit = dcount(source,old)
    origlimit = limit
    while True:
        pos = dfind(src,old)
        for each in pos:
            src[each[0]:each[-1]+1] = ["".join(src[each[0]:each[-1]+1])]
        limit -= 1
        if limit <= (origlimit-count if count != "all" else 0):break


    for i in range(len(dfind(src,old,"all",True)) if count == "all" else count):
        src[dfind(src,old,1,True)] = new

    return("".join(src))


def dsplit(char,schar=" ",limit=0):
    count = dcount(char,schar)
    origcount = count
    if limit == 0:limit = origcount
    out = []

    while True:

        loc = dfind(char,schar)
        if loc >= 0:
            thing = char[:loc]
            out.append(thing)
        char=dreplace(char,f"{thing}{schar}","",1)

        count-=1
        if count <= origcount-limit:break

    out.append(char)
    return out

print(dsplit("Thing1 Thing2 Thing3 ju sa"," "))
#print(dsplit("Thing1 Thing2 Thing3 ju sa"," ",2))
#print(dfind("Ahojoj","oj","all"))
#print(dfind("Ahojoj","o"))
#print(dfind("Ahojoj","g"))
#print(dfind("Ahojoj","o","all"))
#print(dfind(['Text', '1', 'D', 'a', 'r', ' ', 'Text', '2', 'Text'],"Text","all"))
#print(dcount("Ahojddd","d"))
#print(dreplace("Text1Dar Text2Text","Text","Ohoooj"))
#print(dreplace("Text1Dar Text2Text","Text","Ohoooj",1))
