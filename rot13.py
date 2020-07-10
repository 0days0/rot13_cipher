print("""
##########################
##### ROT13 Chipher  #####
##########################""")
# 10.04.2020
alfabe = str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz', 
                       'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm')

def rot13(yazi):
    return yazi.translate(alfabe)

def cümle():
    yazi = input("Şifrelemek istediğiniz cümleyi giriniz('Türkçe karakterler hariç'): ")
  # yazi = yazi.lower() (şifrelenen harfleri küçültür)
    print("Şifreli metniniz: ", rot13(yazi))

cümle()
