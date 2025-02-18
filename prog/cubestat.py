from itertools import product,permutations

def horiz_list(lst, width=2):
    print('\n'.join([''.join([(str(u[-i]) if len(u) >= i else '').rjust(2).rjust(len(str(u[-1]))+1) for u in lst]) for i in range(max(len(u) for u in lst), 0, -1)]))
    #print('\n'.join([''.join([(str(u[-i]) if len(u) >= i else '').rjust(width) for u in lst])]))


def sumgraph(cubes,sides):
    if cubes < 2:raise Exception("Less than 2 cubes isnt allowed")
    if sides < 2:raise Exception("Less than 2 sides isnt allowed")
    cubeslst = [[i+1 for i in range(sides)] for i in range(cubes)]

    all_combs = list(product(*cubeslst))
    sumcubelst = [sum(each) for each in all_combs]
    unique = set(sumcubelst)
    maxvalue = max([sumcubelst.count(each) for each in unique])

    toprint = [list(range(1,maxvalue+1)[::-1])]
    toprint[0].append("")

    for each in unique:
        tmplist = []
        tmplist.append([item*len(str(each)) for item in '█'*sumcubelst.count(each)])
        tmplist[0].append(each)
        toprint.extend(tmplist)

    horiz_list(toprint)

#sumgraph(int(input("\nAký máš počet kociek ? (Aspon 2)\nPočet Kociek: ")),int(input("\nKolko stranovú kocku máš ? (Vetšinou to je 6)\nStrany Kocky: ")))
sumgraph(3,6)
