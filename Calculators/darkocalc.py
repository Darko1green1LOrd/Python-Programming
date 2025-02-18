import math
from itertools import product,combinations,permutations
from re import findall
from os import path,rmdir,system,name
from rich.console import Console
from rich.table import Table
from string import ascii_uppercase
from traceback import print_exc

def cisla(start,end):return ",".join(str(num) for num in range(start,end+1))
def mult(what,howmuch):return ",".join(str(each) for each in [str(what)]*int(howmuch))
def nun(a,b):return((math.factorial(a))/(math.factorial(a-b)*math.factorial(b)))
def nbn(a,b):return(nun((a+b-1),a))
def to_perc(number):return(f"{number*100}%")
def from_perc(number):return(number if type(number) != str else int(number.split("%")[0].strip())/100)

class ExitException(Exception):pass
filesaving = False

def save(filevar,text):
    counter = 0
    while path.isfile(f"{filevar}{counter}.txt"):
        counter += 1
    filename = f"{filevar}{counter}.txt"

    if path.isdir(filename):rmdir(filename)
    with open(filename, 'w') as f:
        f.writelines(str(text))

def printsv(name,text):
    if filesaving:save(name,text)
    print(text)




def bynomic(inputvar,showprocess=False):
    values,displayvalues,inp=[],"",inputvar.strip()
    a = eval(inp.split(" ")[0])
    b = eval(inp.split(" ")[1])
    n = int(inp.split(" ")[2])

    for i in range(n+1):
        values.append(eval(f"((math.factorial({n}))/(math.factorial({n}-{i})*math.factorial({i})))*({a**(n-i)})*({b**i})"))
        displayvalues+=f"((({n}!):(({n}-{i})!*{i}!))*({a} Na {n-i})*({b} Na {i}))+"

    if showprocess:return f"\n{displayvalues[:-1]}\n=\n{'+'.join(str(each) for each in values)}\n=\n{sum(values)}"
    else:return sum(values)



class ipcalc:
    def __init__(self,inputvar,name="Mainnet"):
        inputip=inputvar.strip()
        adr=inputip.split('/')[0]
        maskn=inputip.split('/')[1]

        if len(adr) == 35:adr=self.todec(inputip.split('/')[0]) #binary
        else:pass #decimal

        if len(maskn) == 35:maskn=(inputip.split('/')[1]).count("1") #binary
        elif 0 < len(maskn) < 3:pass #Shortened Mask/Prefix
        else:maskn=self.tobin((inputip.split('/')[1])).count("1") #decimal

        adrbin=self.tobin(adr)
        mb=("1" * int(maskn) + "0" * (32 - int(maskn)))

        maskbin=self.adddots(mb)
        mask=self.todec(maskbin)

        v1,v2=[*adrbin],[*maskbin]
        try:
            netadrbase = ''.join([str((eval(f"{v1[x]}*{v2[x]}")) if v1[x] and v2[x] != "." else str("")) for x in range(len(v1))])
        except: print(f"{adrbin}\n{adr}\n{len(adr)}")
        netadrbin = self.adddots(netadrbase)
        netadr=self.todec(netadrbin)

        broadrbase=f"{netadrbase[0:(int(maskn))]}{netadrbase[(int(maskn)):len(netadrbase)].replace('0','1')}"
        broadrbin= self.adddots(broadrbase)
        broadr=self.todec(broadrbin)

        minhost=f"{netadr.rsplit('.',1)[0]}.{int(str(netadr.rsplit('.',1)[1]))+1}"
        minhostbin=self.tobin(minhost)

        maxhost=f"{broadr.rsplit('.',1)[0]}.{int(str(broadr.rsplit('.',1)[1]))-1}"
        maxhostbin=self.tobin(maxhost)

        usablehosts=2**(32 - int(maskn))-2

        printsv("Darko_ip-calc",
        f'''



Input:               {inputip}

Meno:                {name}
Adresa:              {adrbin}   {adr}
Maska:               {maskbin}   {mask} = {maskn}

Sieťová Adresa:      {netadrbin}   {netadr}
Prvá Použiteľná:     {minhostbin}   {minhost}
Posledná Použiteľná: {maxhostbin}   {maxhost}
Broadcast Adresa:    {broadrbin}   {broadr}
Počet Použiteľných:  {usablehosts}
        ''')
    def tobin(self,adress):
        adress = '.'.join([bin(int(x)+256)[3:] for x in adress.split('.')])
        return adress
    def todec(self,adress):
        adress = '.'.join([str(int(x, 2)) for x in adress.split('.')])
        return adress
    def adddots(self,adress):
        adress = '.'.join(adress[i:i+8] for i in range(0, len(adress), 8))
        return adress

class subnetcalc:
    def __init__(self,inputvar):
        subnets_print,unused_subnets,values,finaltries,unusedtries,unused_count,subnets="","",[0,1,2,3,4,5,6,7],[],False,1,[]
        inputip=inputvar.strip()
        ipgiven = inputip.split(" ")[0]

        amount = inputip.split(" ")[1]

        adr=ipgiven.split('/')[0]
        maskn=ipgiven.split('/')[1]

        if len(adr) == 35:adr=self.todec(inputip.split('/')[0]) #binary
        else:pass #decimal

        if len(maskn) == 35:maskn=(ipgiven.split('/')[1]).count("1") #binary
        elif 0 < len(maskn) < 3:pass #Shortened Mask/Prefix
        else:maskn=self.tobin((ipgiven.split('/')[1])).count("1") #decimal

        adrbin=self.tobin(adr)
        mb=("1" * int(maskn) + "0" * (32 - int(maskn)))
        maskbin=self.adddots(mb)
        mask=self.todec(maskbin)

        difference=maskbin.count("1")
        firstpart=adrbin.replace(".","")[:difference]
        hostpart=adrbin.replace(".","")[difference:]

        for each in values:
            if 2**each >= int(amount):
                bits_amount=each
                break
        subnetmask=int(maskn)+bits_amount
        if len(hostpart) < bits_amount:raise Exception(f"Host part is not big enough for {amount} Subnets(Mask number is too big)")

        tries = [("".join(str(each)).replace(" ","").replace(",","").replace("(","").replace(")","")) for each in list(product([1,0], repeat=bits_amount))]
        tries.reverse()
        for each in tries[:int(amount)]:finaltries.append(each)
        for each in tries[int(amount):]:
            if not unusedtries:
                unused_subnets+=f"Nepoužité podsiete: {2**bits_amount-int(amount)}\n"
                unusedtries = True

            unused_subnetbin=self.adddots(f"{firstpart}{hostpart.replace(hostpart[0:bits_amount],each,1)}")
            unused_subnetadr=self.todec(unused_subnetbin)
            unused_subnets+=f"Unused Subnet {unused_count}: {unused_subnetbin}  {unused_subnetadr}/{subnetmask}\n"
            unused_count+=1
        for num in range(int(amount)):
            subnetbin=self.adddots(f"{firstpart}{hostpart.replace(hostpart[0:bits_amount],finaltries[num],1)}")
            subnetadr=self.todec(subnetbin)
            subnets_print+=f"Subnet {num+1}: {subnetbin}  {subnetadr}/{subnetmask}\n"
            subnets.append([f"{subnetadr}/{subnetmask}",f"Subnet {num+1}"])

        printsv("Darko_subnet-calc",
        f'''




Input:               {inputip}

Adresa:              {adrbin}   {adr}
Maska:               {maskbin}   {mask} = {maskn}

Počet Podsietí: {amount}
{subnets_print}
{unused_subnets}
        ''')
        ask=input("Do you want to use Mode 1(Ip Calculator) on all the subnets? (Excluding Unused Subnets)\n(Y/N): ").lower()
        if(ask) == "y":
            for each in subnets:
                mode1=ipcalc(each[0],each[1])
        elif(ask) == "n":pass
        else:raise Exception("Please Select Y or N")

    def tobin(self,adress):
        adress = '.'.join([bin(int(x)+256)[3:] for x in adress.split('.')])
        return adress
    def todec(self,adress):
        adress = '.'.join([str(int(x, 2)) for x in adress.split('.')])
        return adress
    def adddots(self,adress):
        adress = '.'.join(adress[i:i+8] for i in range(0, len(adress), 8))
        return adress



class probability:

    def mode1(inputvar):
        inp=inputvar.strip()
        inp1 = eval(inp.split(" ")[0])
        inp2 = eval(inp.split(" ")[1])

        in_favor = inp1/inp2
        against = 1 - in_favor

        printsv("Darko_probability_m1-calc",
        f'''

Počet požadovaných možností: {inp1}
Počet všetkých možností:     {inp2}

Šanca pre:                   {inp1} / {inp2} = {in_favor} ({to_perc(in_favor)})
Šanca proti:                 1 - {in_favor} = {against} ({to_perc(against)})
Celkovo:                     {in_favor} + {against} = {in_favor+against} ({to_perc(in_favor+against)})

        ''')


    def mode2(sides,selectedsides=[]):
        if sides < 2:raise Exception("Less than 2 sides isnt allowed")

        sidesvar = [i+1 for i in range(sides)]

        if len(selectedsides) == 0:
            for each in input(f"\n\nVyber čísla ktoré chceme z {','.join(str(each) for each in sidesvar)} (Rozdeluj čiarkou)\nPoužitie: ak je zadanie večie ako 2 vyber všetky nad 2\n\nNapr: 6 Stranná kocka , všetky párne čísla napíšeme 2,4,6\nNapr2: 6 Stranná kocka , všetky čísla večie ako 2 napíšeme 3,4,5,6\n\nChcené čísla: ").split(","):
                selectedsides.append(eval(each))

        in_favor = len(selectedsides)/len(sidesvar)
        against = 1 - in_favor

        printsv("Darko_probability_m2-calc",
        f'''

Vybrané Strany: {','.join(str(each) for each in selectedsides)} ({len(selectedsides)})
Strany Kocky:   {','.join(str(each) for each in sidesvar)} ({len(sidesvar)})

Šanca pre:      {len(selectedsides)} / {len(sidesvar)} = {in_favor} ({to_perc(in_favor)})
Šanca proti:    1 - {in_favor} = {against} ({to_perc(against)})
Celkovo:        {in_favor} + {against} = {in_favor+against} ({to_perc(in_favor+against)})

        ''')


    def mode3(cubes,sides,value=None):
        if cubes < 2:raise Exception("Less than 2 cubes isnt allowed")
        if sides < 2:raise Exception("Less than 2 sides isnt allowed")


        uniquelst = []
        cubeslst = [[i+1 for i in range(sides)] for i in range(cubes)]

        all_combs = list(product(*cubeslst))
        sumcubelst = [sum(each) for each in all_combs]

        for each in sumcubelst:
            if each not in uniquelst:uniquelst.append(each)

        if value == None:
            value = int(input(f"\n\nVyber akú sčítanú hodnotu z {','.join(str(each) for each in uniquelst)} chceš\n\nHodnota: "))

        indexes = [i for i,each in enumerate(sumcubelst) if each==value]
        finallst = [all_combs[each] for each in indexes]


        in_favor = (len(finallst))/(sides**cubes)
        against = 1 - in_favor

        printsv("Darko_probability_m3-calc",
        f'''

Hodnota:      {finallst} ({len(finallst)})
Počet Kociek: {cubes}

Šanca pre:    {(len(finallst))} / {(sides**cubes)} = {in_favor} ({to_perc(in_favor)})
Šanca proti:  1-{in_favor} = {against} ({to_perc(against)})
Celkovo:      {in_favor}+{against} = {in_favor+against} ({to_perc(in_favor+against)})

        ''')


    def mode4(cubes,sides,value=None,mode=None):
        if cubes < 2:raise Exception("Less than 2 cubes isnt allowed")
        if sides < 2:raise Exception("Less than 2 sides isnt allowed")


        uniquelst = []
        indexes = []
        cubeslst = [[i+1 for i in range(sides)] for i in range(cubes)]

        all_combs = list(product(*cubeslst))

        for each in all_combs:
            for item in each:
                if item not in uniquelst:uniquelst.append(item)

        if mode == None:
            mode = int(input("\n\nSelect Mode\n1: At least/Minimally\n2: Exact Amount\n3: Exact value in selected cubes\n4: Maximally\nMode: "))

        if mode == 1:
            if value == None:
                value = input(f"\n\nVyber akú hodnotu z {','.join(str(each) for each in uniquelst)} chceš A Kolko minimálne max {cubes}\nNapr:Chcem 1 aspon 3 krát = 1,3\nNapr2:Chcem 8 aspon 2 krát a 5 aspon 1 krát = 8-2 5-1\n\nHodnota: ")
            value = value.split(" ")

            for i,each in enumerate(all_combs):
                tmplist = list(each)
                for item in value:
                    if tmplist != None:
                        setind = int(item.split("-")[0])
                        setvar = int(item.split("-")[1])
                        if tmplist.count(setind) < setvar:tmplist = None
                if tmplist != None:
                    indexes.append(i)

        elif mode == 2:
            if value == None:
                value = input(f"\n\nVyber akú hodnotu z {','.join(str(each) for each in uniquelst)} chceš A Kolko presne max {cubes}\nNapr:Chcem 1 presne 3 krát = ab-3\nNapr2:Chcem 8 aspon 2 krát a 5 aspon 1 krát = 8-2 5-1\n\nHodnota: ")
            value = value.split(" ")

            for i,each in enumerate(all_combs):
                tmplist = list(each)
                for item in value:
                    if tmplist != None:
                        setind = int(item.split("-")[0])
                        setvar = int(item.split("-")[1])
                        if tmplist.count(setind) != setvar:tmplist = None
                if tmplist != None:
                    indexes.append(i)

        elif mode == 3:
            if value == None:
                value = input(f"\n\nVyber akú kocku z {','.join(str(each+1) for each in range(cubes))} chceš a hodnotu z {','.join(str(each) for each in uniquelst)} chceš\nNapr: Chcem aby druhá kocka bola 3 = 2-3\nNapr2: Chcem aby prvá kocka bola 2 a tretia 4 = 1-2 3-4\n\nHodnota: ")
            value = value.split(" ")

            for i,each in enumerate(all_combs):
                tmplist = list(each)
                for item in value:
                    setind = int(item.split("-")[0])-1
                    setvar = int(item.split("-")[1])
                    tmplist[setind] = setvar
                if list(each) == tmplist:
                    indexes.append(i)

        elif mode == 4:
            if value == None:
                value = input(f"\n\nVyber akú hodnotu z {','.join(str(each) for each in uniquelst)} chceš A Kolko maximálne max {cubes}\nNapr:Chcem 1 max 3 krát = 1,3\nNapr2:Chcem 8 max 2 krát a 5 max 1 krát = 8-2 5-1\n\nHodnota: ")
            value = value.split(" ")

            for i,each in enumerate(all_combs):
                tmplist = list(each)
                for item in value:
                    if tmplist != None:
                        setind = int(item.split("-")[0])
                        setvar = int(item.split("-")[1])
                        if tmplist.count(setind) > setvar:tmplist = None
                if tmplist != None:
                    indexes.append(i)


        else:raise Exception("You slected invalid mode")

        finallst = [all_combs[each] for each in indexes]

        in_favor = (len(finallst))/(sides**cubes)
        against = 1 - in_favor

        printsv("Darko_probability_m4-calc",
        f'''

Hodnota:      {finallst} ({len(finallst)})
Počet Kociek: {cubes}
Všetky Možn:  {(sides**cubes)}

Šanca pre:    {(len(finallst))} / {(sides**cubes)} = {in_favor} ({to_perc(in_favor)})
Šanca proti:  1-{in_favor} = {against} ({to_perc(against)})
Celkovo:      {in_favor}+{against} = {in_favor+against} ({to_perc(in_favor+against)})

        ''')


    def mode5(items,amount,mode=None,value=None):
        for match in findall(r'(mult\("(.*?)",\d+\))', items):items = items.replace(match[0], str(eval(match[0])), 1)
        for match in findall(r'(cisla\(\d+\,\d+\))', items):items = items.replace(match, str(eval(match)), 1) #https://regex101.com/
        print(f"Predmety: {items}")
        if len(items) < amount:raise Exception("Amount cannot be more than the amount of entered items")

        uniquelst = []
        uniquelst2 = []
        indexes = []
        itemslst = items.split(",")

        if len(itemslst) < 2:raise Exception("Less than 2 items isnt allowed")
        if amount < 2:raise Exception("Less than 2 amount isnt allowed")

        all_combs = [each for each in combinations(itemslst,amount)]

        for each in all_combs:
            for item in each:
                if item not in uniquelst:uniquelst.append(item)

        if mode == None:
            mode = int(input("\n\nSelect Mode\n1: At least/Minimally\n2: Exact Amount\n3: Exact value in selected parts\n4. Value in every part is different\n5: Maximally\nMode: "))

        if mode == 1:
            if value == None:
                value = input(f"\n\nVyber akú hodnotu z {','.join(str(each) for each in uniquelst)} chceš A Kolko minimálne max {amount}\nNapr:Chcem ab aspon 3 krát = ab,3\nNapr2:Chcem oj aspon 2 krát a j aspon 1 krát = oj-2 j-1\n\nHodnota: ")
            value = value.split(" ")

            for i,each in enumerate(all_combs):
                tmplist = list(each)
                for item in value:
                    if tmplist != None:
                        setind = item.split("-")[0]
                        setvar = int(item.split("-")[1])
                        if tmplist.count(setind) < setvar:tmplist = None
                if tmplist != None:
                    indexes.append(i)

        elif mode == 2:
            if value == None:
                value = input(f"\n\nVyber akú hodnotu z {','.join(str(each) for each in uniquelst)} chceš A Kolko presne max {amount}\nNapr:Chcem ab presne 3 krát = ab-3\nNapr2:Chcem oj presne 2 krát a j presne 1 krát = oj-2 j-1\n\nHodnota: ")
            value = value.split(" ")

            for i,each in enumerate(all_combs):
                tmplist = list(each)
                for item in value:
                    if tmplist != None:
                        setind = item.split("-")[0]
                        setvar = int(item.split("-")[1])
                        if tmplist.count(setind) != setvar:tmplist = None
                if tmplist != None:
                    indexes.append(i)

        elif mode == 3:
            if value == None:
                value = input(f"\n\nVyber akú časť {','.join(str(each+1) for each in range(amount))} chceš a hodnotu z {','.join(str(each) for each in uniquelst)} chceš\nNapr: Chcem aby druhá časť bola ahoj = 2,ahoj\nNapr2: Chcem aby prvá časť bola o a tretia gj = 1-o 3-gj\n\nHodnota: ")
            value = value.split(" ")

            for i,each in enumerate(all_combs):
                tmplist = list(each)
                for item in value:
                    setind = int(item.split("-")[0])-1
                    setvar = item.split("-")[1]
                    tmplist[setind] = setvar
                if list(each) == tmplist:
                    indexes.append(i)

        elif mode == 4:
            for i,each in enumerate(all_combs):
                tmplist = list(each)
                [uniquelst2.append(item) for item in [each for each in tmplist] if item not in uniquelst2]
                value = ' '.join(str(each)+"-1" for each in uniquelst2).split(" ")
                for item in value:
                    if tmplist != None:
                        setind = item.split("-")[0]
                        setvar = int(item.split("-")[1])
                        if tmplist.count(setind) != setvar:tmplist = None
                if tmplist != None:
                    indexes.append(i)

        elif mode == 5:
            if value == None:
                value = input(f"\n\nVyber akú hodnotu z {','.join(str(each) for each in uniquelst)} chceš A Kolko Maximálne max {amount}\nNapr:Chcem ab Max 3 krát = ab-3\nNapr2:Chcem oj aspon 2 krát a j aspon 1 krát = oj-2 j-1\n\nHodnota: ")
            value = value.split(" ")

            for i,each in enumerate(all_combs):
                tmplist = list(each)
                for item in value:
                    if tmplist != None:
                        setind = item.split("-")[0]
                        setvar = int(item.split("-")[1])
                        if tmplist.count(setind) > setvar:tmplist = None
                if tmplist != None:
                    indexes.append(i)


        else:raise Exception("You slected invalid mode")

        finallst = [all_combs[each] for each in indexes]


        maxv = nun((len(items.split(","))),amount)
        in_favor = (len(finallst))/maxv
        against = 1 - in_favor

        printsv("Darko_probability_m5-calc",
        f'''

Hodnota:      {finallst} ({len(finallst)})
Počet:        {amount}
Všetky Možn:  {maxv}

Šanca pre:    {(len(finallst))} / {maxv} = {in_favor} ({to_perc(in_favor)})
Šanca proti:  1-{in_favor} = {against} ({to_perc(against)})
Celkovo:      {in_favor}+{against} = {in_favor+against} ({to_perc(in_favor+against)})

        ''')

    def mode6(inputvar):
        inp=inputvar.strip()
        inp1 = eval(inp.split(",")[0])
        inp2 = eval(inp.split(",")[1])

        out = nbn(inp1,inp2)
        nothing = ""

        printsv("Darko_probability_m6-calc",
        f'''
Kolko Vyberame:     {inp1}
Kolko Druhov:       {inp2}

Kolko Spôsobov:     nun(({inp1}+{inp2}-1),{inp1}) = {out}

        ''')

    def mode7(inputvar,mode=None,value=None):
        inp=inputvar.strip()
        inp1 = from_perc(inp.split(",")[0])
        inp2 = eval(inp.split(",")[1])

        def mode1_calculate(value_i):return(nun(inp2,value_i)*(inp1**value_i)*(0.1**(inp2-value_i)))

        if mode == None:
            mode = int(input("\n\nSelect Mode\n1: Exact Amount\n2: At least/Minimally\n3: Maximally\nMode: "))

        if mode == 1:
            if value == None:
                value = int(input(f"\n\nVyber akú hodnotu z {','.join(str(num) for num in range(1,inp2+1))} chceš\nNapr:Chcem šancu na presne 2 neuspešné pokusy = 2\nNapr:Chcem šancu na presne 1 uspešný pokus = 1\n\nHodnota: "))
                finalvar = mode1_calculate(value)
                calculation = f"nun({inp2},{value}*({inp1}**{value})*(0.1**({inp2}-{value})))"

        elif mode == 2:
            if value == None:
                value = int(input(f"\n\nVyber akú hodnotu z {','.join(str(num) for num in range(1,inp2+1))} chceš\nNapr:Chcem šancu na aspon/min 2 neuspešné pokusy = 2\nNapr:Chcem šancu na aspon/min 1 aspon pokus = 1\n\nHodnota: "))
                all_vars = [each for each in [num for num in range(1,inp2+1)] if each >= value]
                calculated_vars = [mode1_calculate(each) for each in all_vars]

                finalvar = sum(calculated_vars)
                calculation = "+".join(str(num) for num in calculated_vars)

        elif mode == 3:
            if value == None:
                value = int(input(f"\n\nVyber akú hodnotu z {','.join(str(num) for num in range(1,inp2+1))} chceš\nNapr:Chcem šancu na max 2 neuspešné pokusy = 2\nNapr:Chcem šancu na max 1 uspešný pokus = 1\n\nHodnota: "))
                all_vars = [each for each in [num for num in range(1,inp2+1)] if each <= value]
                calculated_vars = [mode1_calculate(each) for each in all_vars]

                finalvar = sum(calculated_vars)
                calculation = "+".join(str(num) for num in calculated_vars)

        else:raise Exception("You slected invalid mode")

        in_favor = finalvar
        against = 1 - in_favor

        printsv("Darko_probability_m7-calc",
        f'''

Šanca:         {inp1} ({to_perc(inp1)})
Počet Pokusov: {inp2}

Šanca pre:    {calculation} = {in_favor} ({to_perc(in_favor)})
Šanca proti:  1-{in_favor} = {against} ({to_perc(against)})
Celkovo:      {in_favor}+{against} = {in_favor+against} ({to_perc(in_favor+against)})

        ''')

    def mode8(items,size,mode):
        for match in findall(r'(cisla\(\d+\,\d+\))', items):items = items.replace(match, str(eval(match)), 1) #https://regex101.com/
        print(f"Predmety: {items}")

        discarded = []
        itemslst = items.split(",")
        if len(itemslst) < size:raise Exception("Amount of given items cannot be less than the given size")

        if mode == 1:combs = ["".join(each).lstrip("0") for each in permutations(itemslst,size) if len("".join(each).lstrip("0")) == size]
        elif mode == 2:combs = ["".join(each).lstrip("0") for each in combinations(itemslst,size) if len("".join(each).lstrip("0")) == size]
        else:raise Exception("You have to select either mode 1 or mode 2")

        printsv("Darko_probability_m8-calc",
        f'''

Predmety:            {items}
Kolko ciferné čísla: {size}
Režim:               {mode} ({"Permutácie" if mode == 1 else "Kombinácie"}) ({"Z Opakovaním" if mode == 1 else "Bez Opakovania"})

Výsledok:            {",".join([each for each in combs])} ({len(combs)})

Odstranene:          {",".join([each for each in discarded])} ({len(discarded)})

        ''')

    def mode9(topvar,bottomvar):
        out = nun(topvar,bottomvar)
        printsv("Darko_probability_m9-calc",
        f'''

Horné Číslo:  {topvar}
Spodné Číslo: {bottomvar}

Výsledok:     ({topvar}!)/(({topvar}-{bottomvar})!*{bottomvar}!) = {out}

        ''')

    def mode10(leftvar,rightvar):
        out = nbn(leftvar,rightvar)
        printsv("Darko_probability_m10-calc",
        f'''

Horné Číslo:  {leftvar}
Spodné Číslo: {rightvar}

Výsledok:     (({leftvar}+{rightvar}-1)!)/((({leftvar}+{rightvar}-1)-{leftvar})!*{leftvar}!) = {out}

        ''')



class statistics:

    def mode1(items,inptype=1):
        if inptype == 1:
            for match in findall(r'(mult\("(.*?)",\d+\))', items):items = items.replace(match[0], str(eval(match[0])), 1)
            for match in findall(r'(cisla\(\d+\,\d+\))', items):items = items.replace(match, str(eval(match)), 1) #https://regex101.com/

            try:itemslst = [int(num) for num in items.split(",")]
            except ValueError: itemslst = [float(num) for num in items.split(",")]

        elif inptype == 2:
            try:itemslst = [each for item in [[int(each.split(",")[0])]*int(each.split(",")[1]) for each in items.split(" ")] for each in item]
            except ValueError: itemslst = [each for item in [[float(each.split(",")[0])]*int(each.split(",")[1]) for each in items.split(" ")] for each in item]


        itemslst.sort()
        uniquelst = [[each,itemslst.count(each)] for each in set(itemslst)]

        print(f"Predmety: {itemslst}")

        sum_uniq = [each[0]*each[1] for each in uniquelst]
        sum_amount = [each[1] for each in uniquelst]
        aritmet_priem = sum(sum_uniq)/sum(sum_amount)
        lstype = "Parny" if (len(itemslst) % 2) == 0 else "Neparny"

        mod_var = [each for each in uniquelst if each[1] == max([item[1] for item in uniquelst])]
        mod = "None" if len(mod_var) == len(uniquelst) else mod_var if len(mod_var) > 1 else f"{mod_var[0][0]} ({mod_var[0][1]})"

        med = [itemslst[(len(itemslst)//2)-1],itemslst[len(itemslst)//2]] if lstype == 'Parny' else [itemslst[len(itemslst)//2]]

        spread = "+".join(each for each in ["".join(str(item) for item in ["1/",sum(sum_amount),"*","(",each[1],"*","(",each[0],"-",aritmet_priem,")","**2",")"]) for each in uniquelst])
        spread_var = eval(spread)
        odchyl = math.sqrt(spread_var)
        coef = to_perc(odchyl/aritmet_priem)

        printsv("Darko_statistics-calc",
        f'''

Daný Input:             {itemslst} ({len(itemslst)}) {lstype}
Hodnoty(Hodnota,Kolko): {uniquelst}

Sum Hodnoty:            {'+'.join([str(each) for each in sum_uniq])} = {sum(sum_uniq)}
Sum Počet:              {'+'.join([str(each) for each in sum_amount])} = {sum(sum_amount)}

Modus(Max vyskyt):      {mod}
Median(Stred v sorted): {f'({med[0]}+{med[1]})/2 = {(med[0]+med[1])/2}' if lstype == "Parny" else f'{med[0]}'}
Aritmetický Priemer:    {sum(sum_uniq)}/{sum(sum_amount)} = {aritmet_priem}

Rozptyl:                {spread} = {spread_var}

Smerodajná Odchylka:    Odmocnina({spread_var})= {odchyl}
Variačný Koeficient     {odchyl}/{aritmet_priem}*100% = {coef}

        ''')



class priemer:

    def mode1(items,inptype=1):
        itemslst,uniquelst = [],[]
        if inptype == 1:
            for each in items.split(" "):
                value,things = [],[]
                for item in each.split(","):
                    it = type(eval(item))
                    value.append(int(item) if it == int else float(item))
                if len(value) == 2:value.append(1)

                things = [value[0]]*value[1]

                [itemslst.append(each) for each in [[num,value[2]] for num in things]]

        else:
            for match in findall(r'(mult\("(.*?)",\d+\))', items):items = items.replace(match[0], str(eval(match[0])), 1)
            for each in items.split(","):
                value,things = [],[]

                if each.find("-") != 1:each+="-1"

                for item in each.split("-"):
                    it = type(eval(item))
                    value.append(int(item) if it == int else float(item))

                itemslst.append(value)
                
        print(items)
        [uniquelst.append([each[0],itemslst.count(each),each[1]]) for each in itemslst if [each[0],itemslst.count(each),each[1]] not in uniquelst]


        arit_calc = ["+".join(str(each[0]) for each in itemslst),len(itemslst)]
        arit_out = eval(arit_calc[0])/arit_calc[1]

        vaz_calc = ["+".join(f"({each[0]}*{each[1]})" for each in itemslst),"+".join(str(each[1]) for each in itemslst)]
        vaz_out = eval(vaz_calc[0])/eval(vaz_calc[1])

        alt_vaz_calc = ["+".join(f"({each[0]}*{each[1]}*{each[2]})" for each in uniquelst),"+".join(f"({each[1]}*{each[2]})" for each in uniquelst)]
        alt_vaz_out = eval(vaz_calc[0])/eval(vaz_calc[1])

        har_calc = ["+".join(str(each[1]) for each in uniquelst),"+".join(f"({each[1]}/{each[0]})" for each in uniquelst)]
        try:
            har_out = eval(har_calc[0])/eval(har_calc[1])
            har_text = f"{har_calc[0]}/{har_calc[1]} = {eval(har_calc[0])}/{eval(har_calc[1])} = {har_out} = {round(har_out,2)} = {round(har_out)}"
        except ZeroDivisionError:har_text = "Nemožné lebo jedna z hodnôt je 0"

        geo_calc = ["+".join(f"{each[1]}" for each in uniquelst),"*".join(str(each[0]) for each in itemslst)]
        geo_out = eval(geo_calc[1])**(1/eval(geo_calc[0]))

        printsv("Darko_priemer-calc",
        f'''

Daný Input(Hodnota,Váha):    {itemslst} ({len(itemslst)} Hodnôt)
Hodnoty(Hodnota,Kolko,Váha): {uniquelst}

Aritmetický Priemer:         {arit_calc[0]}/{arit_calc[1]} = {eval(arit_calc[0])}/{arit_calc[1]} = {arit_out} = {round(arit_out,2)} = {round(arit_out)}

Važený Priemer:              {vaz_calc[0]}/{vaz_calc[1]} = {eval(vaz_calc[0])}/{eval(vaz_calc[1])} = {vaz_out} = {round(vaz_out,2)} = {round(vaz_out)}

Važený Priemer(Iný vypočet): {alt_vaz_calc[0]}/{alt_vaz_calc[1]} = {eval(alt_vaz_calc[0])}/{eval(alt_vaz_calc[1])} = {alt_vaz_out} = {round(alt_vaz_out,2)} = {round(alt_vaz_out)}

Harmonicky Priemer:          {har_text}

Geometrický Priemer:         {geo_calc[0]} Odmocnina({geo_calc[1]}) = {eval(geo_calc[0])} Odmocnina({eval(geo_calc[1])}) = {geo_out} = {round(geo_out,2)} = {round(geo_out)}

        ''')



class mat_logic:
    def __init__(self,amount):
        if amount < 2:raise ValueError("Ammount is minimally 2")
        Letters = list(ascii_uppercase)
        Variables,Usable_Variables = [],[]
        Current_check = 1

        combinations = [each for each in product([0,1], repeat=amount)]
        combinations.reverse()

        for i in range(amount):
            letter = Letters.pop(0)
            value = []
            value.append(letter)
            Usable_Variables.append(letter)
            value.append([each[i] for each in combinations])

            Variables.append(value)

        while True:
            system('cls||clear')
            table = Table()
            Rows = []
            for each in Variables:
                table.add_column(each[0])
                Rows.append(each[1])

            for i in range(len(Rows[0])):
                current = []
                for each in Rows:current.append(str(each[i]))
                table.add_row(*current, style='bright_green')
        
            console = Console()
            console.print(table)

            newvar = input(f"\nDostupné hodnoty: {' '.join([str(each) for each in Usable_Variables])}\n\nNegation = k\nUparrow/And : a\nDownarrow/Or : d\nRightArrow/If value to left <= value to right : ra\nArrowToBothSides/If leftvalue == rightvalue : ba\n\nNapr: A a (kB)\nZadajte porovnanie: ")

            value,tmplist = [],[]
            newvar = newvar.replace("d","or").replace("ra","<=").replace("ba","==").replace("a","and").replace("k","not ")
            value.append(newvar)
            Usable_Variables.append(f"c{Current_check}")
            for n in range(len(Variables[0][1])):
                tmpvar = newvar
                current_one = []
                for i,each in enumerate(Usable_Variables):
                    if tmpvar.count(each) > 0:
                        tmpvar = tmpvar.replace(each,str(Variables[i][1][n]))
                        current_one.append(tmpvar)
                tmplist.append(eval(current_one[-1])*1)
            value.append(tmplist)
            Variables.append(value)

            Current_check += 1
            if (Current_check == 100) or (input("Ak chcete pridať dalšie porovnanie napíšte c: ").lower() != "c"):break

        system('cls||clear')
        table = Table()
        Rows = []
        for each in Variables:
            table.add_column(each[0])
            Rows.append(each[1])

        for i in range(len(Rows[0])):
            current = []
            for each in Rows:current.append(str(each[i]))
            table.add_row(*current, style='bright_green')
        
        console = Console()
        console.print(table)




class activate:
    def __init__(self):
        global filesaving
        mode = int(input(f"\nSelect Mode\n0: Exit the program\n1: Toggle Saving to file (Currently {'On' if filesaving else 'Off'})\n\n2: Bynomic\n3: Ip\n4: Probability\n5: Statistics\n6: Priemer\n7: Mat Logic\n\nMode: "))
        run = None if mode == 2 else None if mode == 3 else probability if mode == 4 else statistics if mode == 5 else priemer if mode == 6 else None if mode == 7 else None
        
        if mode == 0:raise ExitException("Exitting")
        elif mode == 1:
            filesaving = not filesaving
        elif mode == 2:
            printsv("Darko_Bynomic-calc",bynomic(input("\nZadaj príklad pre bynomickú vetu\n\nPoužitie:A B N (Rozdelené medzerami)\nPríklad (3+6)² By bol 3 6 2\n\nZlomky = (Vršok)/(Spodok)\nSinus = math.sin(číslo)\nCosinus = math.cos(číslo)\nTangens = math.tan(číslo)\nVykričník = math.factorial(číslo)\nNa druhú, tretiu atd = číslo**číslo   Napr = 5**2\n\nNapr: 1 10**-2 6\nNapr2: 2.4 -5 4\n\nPríklad: "),True))

        elif mode == 3:
            selmode = int(input("Select Mode\n1: Ip Calculator\n2: Subnet Calculator\nMode: "))
            if selmode == 1:mode1=ipcalc(input("\nEnter ip with mask\nExample: 192.168.1.1/24\nExample2: 10.178.94.122/26\nExample3: 192.255.13.21/22\nExample4: 11000000.10101000.00000001.00000001/24\nExample5: 11000000.10101000.00000001.00000001/255.255.255.0\nExample6: 11000000.10101000.00000001.00000001/11111111.11111111.11111111.00000000\nExample7: 192.168.1.1/255.255.255.0\nExample8: 192.168.1.1/11111111.11111111.11111111.00000000\nip: "))
            elif selmode == 2:mode2=subnetcalc(input("\nEnter ip with mask along with how many subnets\nExample: 192.168.1.1/24 4\nExample2: 10.178.94.122/26 6\nExample3: 192.255.13.21/22 2\nExample4: 11000000.10101000.00000001.00000001/24 2\nExample5: 11000000.10101000.00000001.00000001/255.255.255.0 2\nExample6: 11000000.10101000.00000001.00000001/11111111.11111111.11111111.00000000 2\nExample7: 192.168.1.1/255.255.255.0 2\nExample8: 192.168.1.1/11111111.11111111.11111111.00000000 2\nip: "))
            else:raise Exception("Please Select one of the 2 Ip Modes")

        elif mode == 4:
            selmode = int(input("Select Mode\n1: Manual Input\n2: Numbers in Dice\n3: Sum of numbers in Dices\n4: Count of numbers in Dices\n5: Manual multiple values\n6: Take ? Amount out of ? packs\n7: ? Amount of tries with certain chance\n8: Make Combinations out of given values and length\n9: Číslo pod číslom v zátvorke\n10: 2 čísla v zátvorke rozdelené bodkočiarkou\nMode: "))
            if selmode == 1:run.mode1(input("\nZadaj príklad pre šancu\n\nPoužitie:Počet_požadovaných_možností Počet_všetkých_možností (Rozdelené medzerami)\nŠanca že padne číslo 3 z 10 všetkých čísel by bolo 3 10\n\nZlomky = (Vršok)/(Spodok)\nSinus = math.sin(číslo)\nCosinus = math.cos(číslo)\nTangens = math.tan(číslo)\nVykričník = math.factorial(číslo)\nĆíslo pod číslom v zátvorke = nun(horné,spodné)\nNa druhú, tretiu atd = číslo**číslo   Napr = 5**2\nČíslo na percentá to_perc(číslo)\nPercentá na číslo from_perc(číslo alebo string(číslo%))\n2 čísla v zátvorke rozdelené bodkočiarkou nbn(lavé,pravé)\n\nNapr: 3 6**3\nNapr2: 1 5000\n\nPríklad: "))
            elif selmode == 2:run.mode2(int(input("\nKolko stranovú kocku máš ? (Vetšinou to je 6)\nStrany Kocky: ")))
            elif selmode == 3:run.mode3(int(input("\nAký máš počet kociek ? (Aspon 2)\n\nPočet Kociek: ")),int(input("\nKolko stranovú kocku máš ? (Vetšinou to je 6)\n\nStrany Kocky: ")))
            elif selmode == 4:run.mode4(int(input("\nAký máš počet kociek ? (Aspon 2)\n\nPočet Kociek: ")),int(input("\nKolko stranovú kocku máš ? (Vetšinou to je 6)\n\nStrany Kocky: ")))
            elif selmode == 5:run.mode5(input('\nZadaj Hodnoty\nNapr 2červené,3Zelené = r,r,g,g,g\n\n\nMôžeš použit cisla(od,do)\nNapr:cisla(1,5) = 1,2,3,4,5\n\nMôžeš aj napísať jednu vec x krát mult("text",kolko_krát)\nNapr mult("a",4) = a,a,a,a\n\nHodnoty: '),int(input("\nKolko toho vybrať? \n\nPočet: ")))
            elif selmode == 6:run.mode6(input("\nNapíš Kolko_Vybrať,Kolko_druhov\nNapr:Vybrať 14 z 9 Druhov: 14,9\n\nZlomky = (Vršok)/(Spodok)\nSinus = math.sin(číslo)\nCosinus = math.cos(číslo)\nTangens = math.tan(číslo)\nVykričník = math.factorial(číslo)\nĆíslo pod číslom v zátvorke = nun(horné,spodné)\nNa druhú, tretiu atd = číslo**číslo   Napr = 5**2\nČíslo na percentá to_perc(číslo)\nPercentá na číslo from_perc(číslo alebo string(číslo%))\n2 čísla v zátvorke rozdelené bodkočiarkou nbn(lavé,pravé)\n\nVstup: "))
            elif selmode == 7:run.mode7(input("\nNapíš Šancu,Počet_Pokusov\nNapr:Šanca 90% Počet Pokusov 5: 90%,5\n\nZlomky = (Vršok)/(Spodok)\nSinus = math.sin(číslo)\nCosinus = math.cos(číslo)\nTangens = math.tan(číslo)\nVykričník = math.factorial(číslo)\nĆíslo pod číslom v zátvorke = nun(horné,spodné)\nNa druhú, tretiu atd = číslo**číslo   Napr = 5**2\nČíslo na percentá to_perc(číslo)\nPercentá na číslo from_perc(číslo alebo string(číslo%))\n2 čísla v zátvorke rozdelené bodkočiarkou nbn(lavé,pravé)\n\nVstup: "))
            elif selmode == 8:run.mode8(input("\nZadaj Čísla\nNapr 1,2,3,4,5,6,7,8,9,10\n\nMôžeš použit cisla(od,do)\nNapr:cisla(1,5) = 1,2,3,4,5\n\nČísla: "),int(input("\nKolko ciferné čísla?(Velkosť)\n\nVelkosť: ")),int(input(f"\nVyber režim:\n1: Z Opakovaním(Permutácie)\n2: Bez Opakovania(Kombinacie)\n\nRežim: ")))
            elif selmode == 9:run.mode9(int(input("\nZadaj horné číslo\nNapr: 1\nNapr2: 6\n\nČíslo: ")),int(input("Zadaj spodné číslo\nNapr: 1\nNapr2: 6\n\nČíslo: ")))
            elif selmode == 10:run.mode10(int(input("\nZadaj lavé číslo\nNapr: 1\nNapr2: 6\n\nČíslo: ")),int(input("Zadaj pravé číslo\nNapr: 1\nNapr2: 6\n\nČíslo: ")))
            else:raise Exception("No valid Probability mode selected")

        elif mode == 5:
            selmode = int(input("Select Mode\n1: Get AritPriemer,Meidan,Modus,Rozptyl from given list\n2: Get AritPriemer,Meidan,Modus,Rozptyl from given UniqueList(Napr: 2 Dvojky,1 Trojka)\nMode: "))
            if selmode == 1:run.mode1(input('\nZadaj Hodnoty\nNapr 6 Chybnych = 0,0,2,3,5,1\n\n\nMôžeš použit cisla(od,do)\nNapr:cisla(1,5) = 1,2,3,4,5\n\nMôžeš aj napísať jednu vec x krát mult("text",kolko_krát)\nNapr mult("1",4) = 1,1,1,1\n\nHodnoty: '))
            elif selmode == 2:run.mode1(input('\nZadaj Hodnoty\nNapr 2 Nuly,1 Dvojka,1 Trojka,1 Petka,1 Jednotka = 0,2 2,1 3,1 5,1 1,1\n\nHodnoty: '),2)
            else:raise Exception("No valid Statistics mode selected")

        elif mode == 6:
            selmode = int(input("Select Mode\n1: Get Aritmeticky Priemer,Važeny Priemer,Harmonicky Priemer,Geometricky Priemer from given UniqueList(Napr: 2 Dvojky,1 Trojka)\n2: Get Aritmeticky Priemer,Važeny Priemer,Harmonicky Priemer,Geometricky Priemer from given List(Napr: 2 Dvojky,1 Trojka)\nMode: "))
            if selmode == 1:run.mode1(input('\nZadaj Hodnoty\nPoužitie: Čislo,počet,váha Čislo,počet,váha ....\nAk neurčíte váhu , automaticky to priradí váhu 1\n\nNapr: 2 Jednotky s vahou 2,1 Dvojka vahou 1,1 Trojka vahou 10,1 Petka vahou 7,1 Jednotka vahou 2 = 1,2,2 2,1,1 3,1,10 5,1,7 1,1,2\nNapr2: 1 Jednotka s vahou 2 a 2 Jednotky s vahou 3 = 1,1,2 1,2,3\nNapr3: 2 Petky s vahou 1 a 1 Jednotka s vahou 2 = 5,2 1,1,2\n\nHodnoty: '))
            elif selmode == 2:run.mode1(input('\nZadaj Hodnoty\nPoužitie: Čislo-váha,Čislo-váha ....\nAk neurčíte váhu , automaticky to priradí váhu 1\n\nNapr: 2 Jednotky s vahou 2,1 Dvojka vahou 1,1 Trojka vahou 10,1 Petka vahou 7,1 Jednotka vahou 2 = 1-2,1-2,2-1,3-10,5-7,1-2\nNapr2: 1 Jednotka s vahou 2 a 2 Jednotky s vahou 3 = 1-2,1-3,1-3\nNapr3: 2 Petky s vahou 1 a 1 Jednotka s vahou 2 = 5,5,1-2\n\nPokial je input napr Pracovník,Min tak stačí spočítat počet min,Napr: \nPracovnik:1 Minuty:6\nPracovnik:2 Minuty:8\nPracovnik:3 Minuty:6\nPracovnik:4 Minuty:12\n= 6,6,12,8\n(6 Minut maju 2 Pracovníci a 8,12 Minut má iba 1 pracovník)\n\nMôžeš aj napísať jednu vec x krát mult("text",kolko_krát)\nNapr mult("1-5",4) = 1,1,1,1\n\nHodnoty: '),2)
            else:raise Exception("No valid Priemer mode selected")
        
        elif mode == 7:
            mat_logic(int(input("Kolko hodnôt chcete ? (A,B,C...)\nMin: 2\nPočet: ")))

        else:raise Exception("No valid mode selected")

while True:
    wait_for_user = True
    system('cls||clear')
    try:c=activate()
    except ExitException:break
    except Exception as e:
        print_exc()
        print(f"\n\nChyba: {repr(e)}")
    except KeyboardInterrupt:wait_for_user = False
    if wait_for_user:
        try:input("Press enter to continue...")
        except KeyboardInterrupt:pass