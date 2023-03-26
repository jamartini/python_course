with open("Input/Letters/starting_letter.txt") as sl:
    text = sl.read()
    print(text)

with open("Input/Names/invited_names.txt") as n:
    names = n.read().splitlines()
print(names)

for i in range(0, len(names)):
    with open(f"Output/ReadyToSend/letter{i}.txt", mode="w") as fl:
        fl.write(text.replace("[name]", f"{names[i]}"))
