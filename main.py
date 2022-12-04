print('')
print('----------------------------')
print("Dobro dosli u program koji odredjuje najveci zajednicki delilac dva prirodna broja")
print('----------------------------')
print('')

inputX = input("Unesite prvi broj ")
inputY = input("Unesite drugi broj ")
x = int(inputX)
y = int(inputY)

reminder = ''

while not reminder == 0:
    reminder = x % y

    if not reminder == 0:
        x = y
        y = reminder

print(f"Najveci zajednicki delilac brojeva {inputX} i {inputY} = {y}")

