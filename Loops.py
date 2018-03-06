print("CONTINUE STATEMENT:\n")
LetterNum = 1
for Letter in "Howdy!":
    if Letter == "w":
        continue
        print("Encountered w, not processed.")
    print("Letter ", LetterNum, " is ", Letter)
    LetterNum+=1
print()

print("PASS STATEMENT:\n")
LetterNum = 1
for Letter in "Howdy!":
    if Letter == "w":
        pass
        print("Encountered w, not processed.")
    print("Letter ", LetterNum, " is ", Letter)
    LetterNum+=1
print()

print("ELSE STATEMENT:\n")
Value = input("Type Any String: ")
LetterNum = 1
for Letter in Value:
    print("Letter ", LetterNum, " is ", Letter)
    LetterNum+=1
else:
    print("END OF STRING", end="\n\n")

print("NESTED LOOPS:\n")
for i in range(int(input("Enter a number:"))):
    for j in range(i+1):
        print("* ", end=" ")
    print()
