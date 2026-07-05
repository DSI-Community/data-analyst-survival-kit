import string

# text = input("Welcher Text soll bereinigt werden?") # Falls text als input eingegeben werden soll

to_be_cleaned = set(string.punctuation) # enthält alle Sonderzeichen

s_cleaned = ""
for s in text:
    if s not in to_be_cleaned:
        s_cleaned += s

print(s_cleaned)
