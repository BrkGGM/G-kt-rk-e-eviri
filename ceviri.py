x = input ('Metini girin : ').lower()
x_list = x.split()


yuvarlaklar = ['o','ö','u','ü']
duzler = ['a','e', 'ı','i']
kalinlar = ['a', 'ı', 'u', 'o']
inceler = ['e', 'i', 'ü', 'ö']
def alfabe_degistir(cumle):
    cumle = cumle.lower()
    
    cumle = cumle.replace("f", "p")
    cumle = cumle.replace("v","b")
    cumle = cumle.replace("h","k")
    cumle = cumle.replace("j","ç")
    cumle = cumle.replace("c","ç")
    cumle = cumle.replace("ğ","g")
    cumle = cumle.replace("ng", "𐰭")
    cumle = cumle.replace("ny","𐰪")
    cumle = cumle.replace("nc","𐰨")
    cumle = cumle.replace("nç","𐰨")
    cumle = cumle.replace("nd","𐰦")
    cumle = cumle.replace("nt","𐰦")
    cumle = cumle.replace("ld","𐰡")
    cumle = cumle.replace("lt","𐰡")
    cumle = cumle.replace("iç","𐰱")
    cumle = cumle.replace("ic","𐰱")
    cumle = cumle.replace("ık","𐰶")
    cumle = cumle.replace("ok","𐰸")
    cumle = cumle.replace("uk","𐰸")
    cumle = cumle.replace("ük","𐰰")
    cumle = cumle.replace("ç","𐰲")
    cumle = cumle.replace("m","𐰢")
    cumle = cumle.replace("p","𐰯")
    cumle = cumle.replace("ş","𐱁")
    cumle = cumle.replace("z","𐰔")
    
    liste = list(cumle)
    y_liste = []
    for i in range(len(liste)):
        if liste[i] == 'b':
            if len(liste) >= i+2:
                if liste[i+1] in kalinlar:
                    y_liste.append("𐰉")
                elif liste[i+1] in inceler:
                    y_liste.append("𐰋")
                else:
                    h_no = i
                    tersine = False
                    while True:
                        if h_no < 0:
                            tersine = True
                        if not tersine:
                            h_no -= 1
                        else:
                            h_no += 1
                        if liste[h_no] in kalinlar:
                            y_liste.append("𐰉")
                            break
                        elif liste[h_no] in inceler:
                            y_liste.append("𐰋")
                            break
                        if h_no == len(liste) - 1:
                            y_liste.append("𐰋")
                            break  
            else:
                h_no = i
                tersine = False
                while True:
                    if h_no < 0:
                        tersine = True
                    if not tersine:
                        h_no -= 1
                    else:
                        h_no += 1
                    if liste[h_no] in kalinlar:
                        y_liste.append("𐰉")
                        break
                    elif liste[h_no] in inceler:
                        y_liste.append("𐰋")
                        break
                    if h_no == len(liste) - 1:
                        y_liste.append("𐰋")
                        break
        elif liste[i] == 'd':
            if len(liste) >= i+2:
                if liste[i+1] in kalinlar:
                    y_liste.append("𐰑")
                elif liste[i+1] in inceler:
                    y_liste.append("𐰓")
                else:
                    h_no = i
                    tersine = False
                    while True:
                        if h_no < 0:
                            tersine = True
                        if not tersine:
                            h_no -= 1
                        else:
                            h_no += 1
                        if liste[h_no] in kalinlar:
                            y_liste.append("𐰑")
                            break
                        elif liste[h_no] in inceler:
                            y_liste.append("𐰓")
                            break
                        if h_no == len(liste) - 1:
                            y_liste.append("𐰓")
                            break  
            else:
                h_no = i
                tersine = False
                while True:
                    if h_no < 0:
                        tersine = True
                    if not tersine:
                        h_no -= 1
                    else:
                        h_no += 1
                    if liste[h_no] in kalinlar:
                        y_liste.append("𐰑")
                        break
                    elif liste[h_no] in inceler:
                        y_liste.append("𐰓")
                        break
                    if h_no == len(liste) - 1:
                        y_liste.append("𐰓")
                        break            

        elif liste[i] == 'g':
            if len(liste) >= i+2:
                if liste[i+1] in kalinlar:
                    y_liste.append("𐰍")
                elif liste[i+1] in inceler:
                    y_liste.append("𐰏")
                else:
                    h_no = i
                    tersine = False
                    while True:
                        if h_no < 0:
                            tersine = True
                        if not tersine:
                            h_no -= 1
                        else:
                            h_no += 1
                        if liste[h_no] in kalinlar:
                            y_liste.append("𐰍")
                            break
                        elif liste[h_no] in inceler:
                            y_liste.append("𐰏")
                            break
                        if h_no == len(liste) - 1:
                            y_liste.append("𐰏")
                            break  
            else:
                h_no = i
                tersine = False
                while True:
                    if h_no < 0:
                        tersine = True
                    if not tersine:
                        h_no -= 1
                    else:
                        h_no += 1
                    if liste[h_no] in kalinlar:
                        y_liste.append("𐰍")
                        break
                    elif liste[h_no] in inceler:
                        y_liste.append("𐰏")
                        break
                    if h_no == len(liste) - 1:
                        y_liste.append("𐰏")
                        break  

        elif liste[i] == 'k':
            if len(liste) >= i+2:
                if liste[i+1] in kalinlar:
                    y_liste.append("𐰴")
                elif liste[i+1] in inceler:
                    y_liste.append("𐰚")
                else:
                    h_no = i
                    tersine = False
                    while True:
                        if h_no < 0:
                            tersine = True
                        if not tersine:
                            h_no -= 1
                        else:
                            h_no += 1
                        if liste[h_no] in kalinlar:
                            y_liste.append("𐰴")
                            break
                        elif liste[h_no] in inceler:
                            y_liste.append("𐰚")
                            break
                        if h_no == len(liste) - 1:
                            y_liste.append("𐰚")
                            break  
            else:
                h_no = i
                tersine = False
                while True:
                    if h_no < 0:
                        tersine = True
                    if not tersine:
                        h_no -= 1
                    else:
                        h_no += 1
                    if liste[h_no] in kalinlar:
                        y_liste.append("𐰴")
                        break
                    elif liste[h_no] in inceler:
                        y_liste.append("𐰚")
                        break
                    if h_no == len(liste) - 1:
                        y_liste.append("𐰚")
                        break  
        elif liste[i] == 'l':
            if len(liste) >= i+2:
                if liste[i+1] in kalinlar:
                    y_liste.append("𐰞")
                elif liste[i+1] in inceler:
                    y_liste.append("𐰠")
                else:
                    h_no = i
                    tersine = False
                    while True:
                        if h_no < 0:
                            tersine = True
                        if not tersine:
                            h_no -= 1
                        else:
                            h_no += 1
                        if liste[h_no] in kalinlar:
                            y_liste.append("𐰞")
                            break
                        elif liste[h_no] in inceler:
                            y_liste.append("𐰠")
                            break
                        if h_no == len(liste) - 1:
                            y_liste.append("𐰠")
                            break  
            else:
                h_no = i
                tersine = False
                while True:
                    if h_no < 0:
                        tersine = True
                    if not tersine:
                        h_no -= 1
                    else:
                        h_no += 1
                    if liste[h_no] in kalinlar:
                        y_liste.append("𐰞")
                        break
                    elif liste[h_no] in inceler:
                        y_liste.append("𐰠")
                        break
                    if h_no == len(liste) - 1:
                        y_liste.append("𐰠")
                        break  
        elif liste[i] == 'n':
            if len(liste) >= i+2:
                if liste[i+1] in kalinlar:
                    y_liste.append("𐰣")
                elif liste[i+1] in inceler:
                    y_liste.append("𐰤")
                else:
                    h_no = i
                    tersine = False
                    while True:
                        if h_no < 0:
                            tersine = True
                        if not tersine:
                            h_no -= 1
                        else:
                            h_no += 1
                        if liste[h_no] in kalinlar:
                            y_liste.append("𐰣")
                            break
                        elif liste[h_no] in inceler:
                            y_liste.append("𐰤")
                            break
                        if h_no == len(liste) - 1:
                            y_liste.append("𐰤")
                            break  
            else:
                h_no = i
                tersine = False
                while True:
                    if h_no < 0:
                        tersine = True
                    if not tersine:
                        h_no -= 1
                    else:
                        h_no += 1
                    if liste[h_no] in kalinlar:
                        y_liste.append("𐰣")
                        break
                    elif liste[h_no] in inceler:
                        y_liste.append("𐰤")
                        break
                    if h_no == len(liste) - 1:
                        y_liste.append("𐰤")
                        break  
        elif liste[i] == 'r':
            if len(liste) >= i+2:
                if liste[i+1] in kalinlar:
                    y_liste.append("𐰺")
                elif liste[i+1] in inceler:
                    y_liste.append("𐰼")
                else:
                    h_no = i
                    tersine = False
                    while True:
                        if h_no < 0:
                            tersine = True
                        if not tersine:
                            h_no -= 1
                        else:
                            h_no += 1
                        if liste[h_no] in kalinlar:
                            y_liste.append("𐰺")
                            break
                        elif liste[h_no] in inceler:
                            y_liste.append("𐰼")
                            break
                        if h_no == len(liste) - 1:
                            y_liste.append("𐰼")
                            break  
            else:
                h_no = i
                tersine = False
                while True:
                    if h_no < 0:
                        tersine = True
                    if not tersine:
                        h_no -= 1
                    else:
                        h_no += 1
                    if liste[h_no] in kalinlar:
                        y_liste.append("𐰺")
                        break
                    elif liste[h_no] in inceler:
                        y_liste.append("𐰼")
                        break
                    if h_no == len(liste) - 1:
                        y_liste.append("𐰼")
                        break  

        elif liste[i] == 's':
            if len(liste) >= i+2:
                if liste[i+1] in kalinlar:
                    y_liste.append("𐰽")
                elif liste[i+1] in inceler:
                    y_liste.append("𐰾")
                else:
                    h_no = i
                    tersine = False
                    while True:
                        if h_no < 0:
                            tersine = True
                        if not tersine:
                            h_no -= 1
                        else:
                            h_no += 1
                        if liste[h_no] in kalinlar:
                            y_liste.append("𐰽")
                            break
                        elif liste[h_no] in inceler:
                            y_liste.append("𐰾")
                            break
                        if h_no == len(liste) - 1:
                            y_liste.append("𐰾")
                            break  
            else:
                h_no = i
                tersine = False
                while True:
                    if h_no < 0:
                        tersine = True
                    if not tersine:
                        h_no -= 1
                    else:
                        h_no += 1
                    if liste[h_no] in kalinlar:
                        y_liste.append("𐰽")
                        break
                    elif liste[h_no] in inceler:
                        y_liste.append("𐰾")
                        break
                    if h_no == len(liste) - 1:
                        y_liste.append("𐰾")
                        break  
        elif liste[i] == 't':
            if len(liste) >= i+2:
                if liste[i+1] in kalinlar:
                    y_liste.append("𐱃")
                elif liste[i+1] in inceler:
                    y_liste.append("𐱅")
                else:
                    h_no = i
                    tersine = False
                    while True:
                        if h_no < 0:
                            tersine = True
                        if not tersine:
                            h_no -= 1
                        else:
                            h_no += 1
                        if liste[h_no] in kalinlar:
                            y_liste.append("𐱃")
                            break
                        elif liste[h_no] in inceler:
                            y_liste.append("𐱅")
                            break
                        if h_no == len(liste) - 1:
                            y_liste.append("𐱅")
                            break  
            else:
                h_no = i
                tersine = False
                while True:
                    if h_no < 0:
                        tersine = True
                    if not tersine:
                        h_no -= 1
                    else:
                        h_no += 1
                    if liste[h_no] in kalinlar:
                        y_liste.append("𐱃")
                        break
                    elif liste[h_no] in inceler:
                        y_liste.append("𐱅")
                        break
                    if h_no == len(liste) - 1:
                        y_liste.append("𐱅")
                        break
        elif liste[i] == 'y':
            if len(liste) >= i+2:
                if liste[i+1] in kalinlar:
                    y_liste.append("𐰖")
                elif liste[i+1] in inceler:
                    y_liste.append("𐰘")
                else:
                    h_no = i
                    tersine = False
                    while True:
                        if h_no < 0:
                            tersine = True
                        if not tersine:
                            h_no -= 1
                        else:
                            h_no += 1
                        if liste[h_no] in kalinlar:
                            y_liste.append("𐰖")
                            break
                        elif liste[h_no] in inceler:
                            y_liste.append("𐰘")
                            break
                        if h_no == len(liste) - 1:
                            y_liste.append("𐰘")
                            break  
            else:
                h_no = i
                tersine = False
                while True:
                    if h_no < 0:
                        tersine = True
                    if not tersine:
                        h_no -= 1
                    else:
                        h_no += 1
                    if liste[h_no] in kalinlar:
                        y_liste.append("𐰖")
                        break
                    elif liste[h_no] in inceler:
                        y_liste.append("𐰘")
                        break
                    if h_no == len(liste) - 1:
                        y_liste.append("𐰘")
                        break
        else:
            y_liste.append(liste[i])

    cumle = ''.join(y_liste)    
    cumle = cumle.replace("a","𐰀")
    cumle = cumle.replace("e","𐰀")
    cumle = cumle.replace("ı","𐰃")
    cumle = cumle.replace("i","𐰃")
    cumle = cumle.replace("o","𐰆")
    cumle = cumle.replace("u","𐰆")
    cumle = cumle.replace("ö","𐰇")
    cumle = cumle.replace("ü","𐰇")

    return(cumle)

def turkcelestir(kelime):
    duz_unluler = False
    yuvarlar_unluler = False

    parcalanmis_kelime = list(kelime)
    sonuc_list = []
    for i in range(len(parcalanmis_kelime)):
        dur = False

        if  parcalanmis_kelime[i] == '𐰀':

            dur = True
        
        if parcalanmis_kelime[i] == '𐰀' or parcalanmis_kelime[i] == '𐰃' :
            if not duz_unluler:
                duz_unluler = True
            else:
                dur = True

        if parcalanmis_kelime[i] == '𐰆' or parcalanmis_kelime[i] == '𐰇' :
            if not yuvarlar_unluler:
                yuvarlar_unluler = True
            else:
                dur = True
        if not dur:    
            sonuc_list.append(parcalanmis_kelime[i])
        else:
            if i == len(parcalanmis_kelime) - 1:
                sonuc_list.append(parcalanmis_kelime[i])

#hayatında görüp görebileceğiniz en saçma kod
        
    cevrilmis = ''.join(sonuc_list)
    return cevrilmis[::-1]
sonuc = []

for kelime in x_list:
    
    
    sonuc.append(turkcelestir(alfabe_degistir(kelime)))
    #sonuc.append(turkcelestir(kelime))
   
    
sonuc.reverse()
print(':'.join(sonuc))
