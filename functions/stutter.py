def stutter(word):
    first=word[0:2] 
    word=f"{first}... {first}... {word}?"
    return word

a = input("Kelime giriniz: ")
print(stutter(a))

x = 10
asdd = 5