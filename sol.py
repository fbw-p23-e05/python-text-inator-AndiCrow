word = input("Enter a sinlge word:")

if word[-1] in "aeiou":
    print(f"{word}-inator {len(word)}000")
else:
    print(f"{word}inator {len(word)}000")
          