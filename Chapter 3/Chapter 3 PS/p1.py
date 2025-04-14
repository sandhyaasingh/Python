a = input("enter ur name")
b = input("enter ur name")
print("Good afternoon", a + b)
print(f"Good afternoon {a+b}")


letter = '''Dear <|Name|>,
    You are selected!
    <|Date|>'''

print(letter.replace("<|Name|>", "Sandhya Singh").replace("<|Date|>", "1st May 2025")) #chaining