HEXA_CODE = {'AliceBlue': '#f0f8ff',
             'AntiqueWhite': '#faebd7',
             'aquamarine1': '#7fffd4',
             'beige': '#f5f5dc',
             'black': '#000000',
             'brown': '#a52a2a',
             'burlywood': '#deb887',
             'CadetBlue': '#5f9ea0',
             'chocolate': '#d2691e',
             'coral': '#ff7f50'}


user_inp = input("Enter color name")
if user_inp in HEXA_CODE:
    print(HEXA_CODE[user_inp])
else:
    print("Not in the list")