import os.path

filename = input("Welcome to Darko s text reverser made to troll copy paste train texts\n\nThis reverses the text, but also adds RIGHT-TO-LEFT OVERRIDE so it should look the same\nText affected by this acts weird with backspace delete and moving around with arrows\nthis can only see files in the same folder as the python script is in\n\nPlease specify file to expand text in\nMake sure to specify if its .txt or whatever filetype it is\nAlso , capital letters matter\nExample: filE.txt\n\nFile: ")


file_existing = os.path.exists(filename)
if file_existing == True:
    pass
else:
    print("Specified file doesnt exist, exitting")
    exit()


file = open(filename, "r")
string = (file.read())

reversechar = "‮"
stringletters,tmpstringletters = [],[]

def custom_reverse(in_str: str) -> str:
    reversed = in_str[::-1]
    modify = {
        "(": ")", ")": "(",
        "[": "]", "]": "[",
        "{": "}", "}": "{",
        "<": ">", ">": "<",
        "‹": "›", "›": "‹",
        "«": "»", "»": "«",
        "（": "）", "）": "（",
        "［": "］", "］": "［",
        "｛": "｝", "｝": "｛",
        "｟": "｠", "｠": "｟",
        "⦅": "⦆", "⦆": "⦅",
        "〚": "〛", "〛": "〚",
        "⦃": "⦄", "⦄": "⦃",
        "「": "」", "」": "「",
        "〈": "〉", "〉": "〈",
        "《": "》", "》": "《",
        "【": "】", "】": "【",
        "〔": "〕", "〕": "〔",
        "⦗": "⦘", "⦘": "⦗",
        "『": "』", "』": "『",
        "〖": "〗", "〗": "〖",
        "〘": "〙", "〙": "〘",
        "｢": "｣", "｣": "｢",
        "⟦": "⟧", "⟧": "⟦",
        "⟨": "⟩", "⟩": "⟨",
        "⟪": "⟫", "⟫": "⟪",
        "⟮": "⟯", "⟯": "⟮",
        "⟬": "⟭", "⟭": "⟬",
        "⌈": "⌉", "⌉": "⌈",
        "⌊": "⌋", "⌋": "⌊",
        "⦇": "⦈", "⦈": "⦇",
        "⦉": "⦊", "⦊": "⦉",
        "❨": "❩", "❩": "❨",
        "❪": "❫", "❫": "❪",
        "❴": "❵", "❵": "❴",
        "❬": "❭", "❭": "❬",
        "❮": "❯", "❯": "❮",
        "❰": "❱", "❱": "❰",
        "❲": "❳", "❳": "❲",
        "〈": "〉", "〉": "〈",
        "⦑": "⦒", "⦒": "⦑",
        "⧼": "⧽", "⧽": "⧼",
        "﹙": "﹚", "﹚": "﹙",
        "﹛": "﹜", "﹜": "﹛",
        "﹝": "﹞", "﹞": "﹝",
        "⁽": "⁾", "⁾": "⁽",
        "₍": "₎", "₎": "₍",
        "⦋": "⦌", "⦌": "⦋",
        "⦍": "⦎", "⦎": "⦍",
        "⦏": "⦐", "⦐": "⦏",
        "⁅": "⁆", "⁆": "⁅",
        "⸢": "⸣", "⸣": "⸢",
        "⸤": "⸥", "⸥": "⸤",
        "⟅": "⟆", "⟆": "⟅",
        "⦓": "⦔", "⦔": "⦓",
        "⦕": "⦖", "⦖": "⦕",
        "⸦": "⸧", "⸧": "⸦",
        "⸨": "⸩", "⸩": "⸨",
        "⧘": "⧙", "⧙": "⧘",
        "⧚": "⧛", "⧛": "⧚",
        "⸜": "⸝", "⸝": "⸜",
        "⸌": "⸍", "⸍": "⸌",
        "⸂": "⸃", "⸃": "⸂",
        "⸄": "⸅", "⸅": "⸄",
        "⸉": "⸊", "⸊": "⸉",
        "᚛": "᚜", "᚜": "᚛",
        "༺": "༻", "༻": "༺"
    }
    for i, char in enumerate(reversed):
        if char in modify.keys():
            reversed = reversed[:i] + modify[char] + reversed[i+1:]
    return reversed

for letter in string:
    if letter != "\n":
        tmpstringletters.append(letter+reversechar)
    else:
        stringletters.append(custom_reverse(''.join([str(each) for each in tmpstringletters])))
        tmpstringletters = []
        stringletters.append(letter)
del stringletters[-1]

string = ""
for x in stringletters:string += ""+x

checker = input("\nApply changes?\nAnswer Y or N: ").lower()
if checker == "y":
    with open(filename, 'w') as f:
        f.write(string)
elif checker == "n":exit()
else:print("Please enter Y or N.")
