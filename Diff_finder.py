from argparse import ArgumentParser,RawTextHelpFormatter
from string import ascii_uppercase,ascii_lowercase,digits
from random import choice
main_parser = ArgumentParser(description="Darko s file difference finder",formatter_class=RawTextHelpFormatter)
main_parser.add_argument("-f1",type=str,required=True,nargs="?",help="Give file 1 s path\nUsage : python3 %(prog)s -f1 path")
main_parser.add_argument("-f2",type=str,required=True,nargs="?",help="Give file 2 s path\nUsage : python3 %(prog)s -f2 path")
main_parser.add_argument("--save",action="store_true",help="Include this to attempt to save to a new file (Usage : python3 %(prog)s --save)")
main_parser.add_argument("--first",action="store_true",help="Include this to only check first word of each line (Usage : python3 %(prog)s --first)")
args = main_parser.parse_args()
with open(args.f1, 'r') as f:f1 = [line.split(" ",1)[0].strip() for line in f] if args.first else [line.strip() for line in f]
with open(args.f2, 'r') as f:f2 = [line.split(" ",1)[0].strip() for line in f] if args.first else [line.strip() for line in f]

result = set(f1).difference(set(f2))
if result == set():result = set(f2).difference(set(f1))

[print(each) for each in result]
if args.save:
    randomname = ''.join(choice(ascii_lowercase + ascii_uppercase + digits) for _ in range(5))
    with open(f"difference_{randomname}.txt", 'w') as f:
        f.writelines("".join([f"{each}\n" for each in result]).strip())
