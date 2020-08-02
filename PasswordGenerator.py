# Password Generator

# strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.

# Extra: Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.



def have_internet():
    try:
        import httplib
    except:
        import http.client as httplib

    conn = httplib.HTTPConnection("www.google.com", timeout=5)
    try:
        conn.request("HEAD", "/")
        conn.close()
        return True
    except:
        conn.close()
        return False
		
def capitalz(temp,tero):

    import random

    if not temp[tero].isupper():
        temp[tero] = temp[tero].upper()
    else:
        tero = random.randint(0, len(temp) - 3)
        capitalz(temp, tero)
    return temp

def rand_maiusc(temp):
    import random

    pl2 = int(input('\t La password è lunga %d caratteri (senza contare i numeri). Quante maiuscole? \n\n' % (len(temp))))

    if pl2 <= len(temp):

        print('\n Valore valido!\n')

        temp = list(temp)

        for i in range(0, pl2):

            tero = random.randint(0, len(temp) - 1)
            temp = capitalz(temp, tero)

        rand_name = ''.join(temp)

        return rand_name
    else:
        print('\n Valore NON valido!\n')

        return 0

def maiuscolator(temp, name1, name2):
    pl1 = int(input(
        "\t Vuoi che: \n \t • L'iniziale della prima parola sia maiuscola    \t [1] \n \t • L'iniziale della seconda parola sia maiuscola \t [2] \n \t • Entrambe le cose                                \t [3] \n \t • Ci siano maiuscole a caso            \t\t [4] \n"))
    if pl1 == 1:
        rand_name = ''.join([name1.capitalize(), name2])
    elif pl1 == 2:
        rand_name = ''.join([name1, name2.capitalize()])
    elif pl1 == 3:
        rand_name = ''.join([name1.capitalize(), name2.capitalize()])
    elif pl1 == 4:
        rand_name = rand_maiusc(temp)

        while rand_name == 0:
            rand_name = rand_maiusc(temp)
    else:
        print("\t Valore non valido.\n")
        rand_name = 0

    return rand_name

def easy_pass():
    import random
    import urllib.request

    cont = have_internet()
    while not cont:
        print("\n Error: Internet Connection is not Avaiable. \n")
        check = input("\n Please type 1 to check again if Internet is avaiable or press any other key to close. \n")

        if int(check):
            cont = have_internet()
        else:
            break

    word_url = "https://raw.githubusercontent.com/napolux/paroleitaliane/master/paroleitaliane/60000_parole_italiane.txt"  # simply a url
    response = urllib.request.urlopen(word_url)             # opens the url: it is HTTP Response type
    long_txt = response.read().decode()                     # string: it is of the type 'a\nAAA\nAAAS\n...'
    words = long_txt.splitlines()                           # list: splitlines takes '\n' as a separator for elements
    #upper_words = [word for word in words if word[0].isupper()]                 # subset of words
    #name_words = [word for word in upper_words if not word.isupper()]           # subset of upper_words

    #rand_name = ''.join([words[random.randint(0, len(words))], words[random.randint(0, len(words))], str(random.randint(0, 100))])

    name1 = words[random.randint(0, len(words))]
    name2 = words[random.randint(0, len(words))]
    num = random.randint(0, 99)

    if num < 10:
        ''.join([0, num])

    temp = ''.join([name1, name2])

    pl = input('\t La password generata è: \n\n \t %s \n\n \t Vuoi che ci siano anche maiuscole? [Y] Sì , [Tasto Qualunque] No.\n\n' % ''.join([temp, str(num)]))

    if pl.upper() == 'Y':
        temp1 = maiuscolator(temp, name1, name2)

        while temp1 == 0:
            temp1 = maiuscolator(temp, name1, name2)

        rand_name = ''.join([temp1, str(num)])
    else:
        rand_name = ''.join([temp, str(num)])
    print('\t Password: \n\n \t %s \n' % rand_name)

    return 0

def rand_ins(name1, name2):
    import random
    control = random.randint(0, 1)
    if not control:
        temp = ''.join([name1, name2])
    else:
        temp = ''.join([name2, name1])
    return [temp, control]

def num_maiusc(name1, name2):
    import random

    num1 = random.randint(1, 99)
    num2 = random.randint(1, 99)

    if num1 < 10:
        num1 = ''.join([0, str(num1)])
    if num2 < 10:
        num2 = ''.join([0, str(num2)])

    r_ins = rand_ins(name1, name2)              # Randomly insterts either name2 after name1 or vice versa -> see doc

    # Here I give the preview

    control = random.randint(0, 1)
    if not control:
        print("\t La password generata è: \n\n \t %s \n\n" % (''.join([str(num1), r_ins[0], str(num2)])))
    else:
        print("\t La password generata è: \n\n \t %s \n\n" % (''.join([str(num2), r_ins[0], str(num1)])))

    pl = input('\t Vuoi che ci siano anche maiuscole? [Y] Sì , [Tasto Qualunque] No.\n\n')

    if pl.upper() == 'Y':

        while True:

            if not control:
                if not r_ins[1]:
                    rand_name = ''.join([str(num1), maiuscolator(r_ins[0], name1, name2), str(num2)])
                    break
                else:
                    rand_name = ''.join([str(num1), maiuscolator(r_ins[0], name2, name1), str(num2)])
                    break
            else:
                if not r_ins[1]:
                    rand_name = ''.join([str(num2), maiuscolator(r_ins[0], name1, name2), str(num1)])
                    break
                else:
                    rand_name = ''.join([str(num2), maiuscolator(r_ins[0], name2, name1), str(num1)])
                    break
    else:
        if not control:
            if not r_ins[1]:
                rand_name = ''.join([str(num1), name1, name2, str(num2)])

            else:
                rand_name = ''.join([str(num1), name2, name1, str(num2)])

        else:
            if not r_ins[1]:
                rand_name = ''.join([str(num2), name1, name2, str(num1)])

            else:
                rand_name = ''.join([str(num2), name2, name1, str(num1)])

    return rand_name

def choosator(words_1, words_2):
    import random

    pl1 = int(input("\t Vuoi che: \n \t • La password sia composta da due nomi comuni             	    \t [1] \n \t • La password sia composta da due nomi propri (località e persone) \t [2] \n \t • La password sia composta da un nome comune e uno proprio   \t\t [3] \n"))

    if pl1 == 1:
        name1 = words_1[random.randint(0, len(words_1))]
        name2 = words_1[random.randint(0, len(words_1))]

        temp = num_maiusc(name1, name2)
    elif pl1 == 2:
        name1 = words_2[random.randint(0, len(words_2))]
        name2 = words_2[random.randint(0, len(words_2))]

        temp = num_maiusc(name1, name2)
    elif pl1 == 3:
        name1 = words_1[random.randint(0, len(words_1))]
        name2 = words_2[random.randint(0, len(words_2))]

        temp = num_maiusc(name1, name2)

    else:
        print("\t Valore non valido.\n")
        temp = 0

    return temp

def mid_pass():
    import random
    import urllib.request

    cont = have_internet()

    while not cont:
        print("\n Error: Internet Connection is not Avaiable. \n")
		
        check = input("\n Please type 1 to check again if Internet is avaiable or press any other key to close. \n")
		
        if int(check):
            cont = have_internet()
			
        else:
            break

    print("\n Internet Connection Detected!\n")

    print('\t Accessing Internet repository. May take a while.\n')

    #word_url = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"    # simply a url

    word_url_1 = "https://raw.githubusercontent.com/napolux/paroleitaliane/master/paroleitaliane/660000_parole_italiane.txt"
    word_url_2 = "https://raw.githubusercontent.com/napolux/paroleitaliane/master/paroleitaliane/9000_nomi_propri.txt"

    response_1 = urllib.request.urlopen(word_url_1)             # opens the url: it is HTTP Response type
    long_txt_1 = response_1.read().decode()                     # string: it is of the type 'a\nAAA\nAAAS\n...'
    words_1 = long_txt_1.splitlines()                           # list: splitlines takes '\n' as a separator for elements

    response_2 = urllib.request.urlopen(word_url_2)  # opens the url: it is HTTP Response type
    long_txt_2 = response_2.read().decode()  # string: it is of the type 'a\nAAA\nAAAS\n...'
    words_2 = long_txt_2.splitlines()  # list: splitlines takes '\n' as a separator for elements

    rand_name = choosator(words_1, words_2)

    while not rand_name:
        rand_name = choosator(words_1, words_2)

    print('\t Password: \n\n \t %s \n' % rand_name)

def hard_pass():
    import secrets
    import string


    ttt = 0
    L=0

    while L <= ttt:
        L = int(input('\t Specificare la lunghezza della password:\n'))
        mais = int(input('\t Specificare il numero di maiuscole desiderato:\n'))
        numm = int(input('\t Specificare il numero di caratteri numerici desiderato:\n'))
        ssy = int(input('\t Specificare il numero di caratteri speciali desiderato:\n'))

        ttt = mais+numm+ssy

        if L <= ttt:
            print('\n Errore! La somma dei valori inseriti non può essere pari o maggiore a L lunghezza richiesta.\n')

    tot = string.printable

    # AABB = string.ascii_uppercase
    # aabb = string.ascii_lowercase
	
    symbs = string.punctuation
			
    list_sym = list(tot)
    list_sym = list_sym[1:94]

    print('\n Caricamento: ')
    while True:
        password = ''.join(secrets.choice(list_sym) for i in range(L))

        if (any(c.islower() for c in password)
                and sum(c.isupper() for c in password) == mais
                and sum(c.isdigit() for c in password) == numm
                and sum(c in string.punctuation for c in password) == ssy):
            break


    print('\n Password: \n\n \t %s \n' % repr(password))
	
###########################################      HERE THE MAIN PART         ##########################################

import string

while True:
    print('\n\n\t ======================== Benevenuto nel PassWord Generator Utility! ========================\n\n')
    print('\n\n\t ================================ REQUIRES INTERNET CONNECTION ==============================\n\n')

    pl1 = input("\t Scegli tra: \n \t • Password semplice        \t [1] \n \t • Password medio-difficile \t [2] \n \t • Password molto difficile \t [3] \n \t • Chiudi Utility \t [Qualsiasi tasto] \n")

    if pl1 in string.punctuation:
        print('\n\n\t =========================================== END ============================================ \n\n')
        input()  # works as: System('PAUSE')
        break
    else:
        if int(pl1) == 1:
            easy_pass()
            input()                 # works as: System('PAUSE')
        elif int(pl1) == 2:
            mid_pass()
            input()  # works as: System('PAUSE')
        elif int(pl1) == 3:
            hard_pass()
            input()  # works as: System('PAUSE')
        else:
            print(
                '\n\n\t =========================================== END ============================================ \n\n')
            input()  # works as: System('PAUSE')
            break
