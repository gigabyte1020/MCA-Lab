txt="Jelloing"
if (txt[-3:]!="ing"):
    txt=txt+"ing"
    print(txt)
else:
    txt=txt+"ly"
    print(txt)