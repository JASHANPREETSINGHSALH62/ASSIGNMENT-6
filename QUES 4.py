str=input("ENTER A STRING TO CHECK PANGRAM: ")
alphabet="abcdefghijklmnopqrstuvwxyz"
a=True
for char in alphabet:
    if char not in str.lower():
        a=False
if(a==True):
    print("PANGRAM")
else:
    print("NOT PANGRAM")            