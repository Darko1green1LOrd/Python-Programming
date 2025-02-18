from time import time
from pyperclip import copy

timestamp = int(time())

copy(f"<t:{timestamp}:F> / <t:{timestamp}:R>")
