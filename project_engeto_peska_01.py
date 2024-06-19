"""

projekt_1.py: první projekt do Engeto Online Python Akademie
author: Vratislav Peška
email: vpeska@gmail.com
discord: Vratislav Peška vratislavpeska_11865

"""
from task_template import TEXTS


# Promenne
len_TEXTS = len(TEXTS)
users = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}

login = input("username: ") # Vyžádá si od uživatele přihlašovací jméno a heslo,
password = input("password: ")


if login in users: # overovani loginu
    if users[login] != password: # overovani hesla
        print("wrong password")
    else:
        # Program nechá uživatele vybrat mezi texty, uloženými v proměnné TEXTS:
         
        print(f"----------------------------------------\n" \
              f"Welcome to the app, {login},\n" \
              f"We have {len_TEXTS} texts to be analyzed.\n" \
              "----------------------------------------")

        TEXT_num = input(f"Enter a number between 1 and {len_TEXTS} to select: ")
        print("----------------------------------------")

        if TEXT_num.isdecimal() and int(TEXT_num) in range(1, (len_TEXTS + 1)):
                        
            # Pro vybraný text spočítá následující statistiky:
            # promenne pro .translate
            to_remove = ".,"
            to_find = "\n"
            to_put = " "
            # promenne pro modifikovany text
            TEXTS_strip = []
            
            # vlozi do TEXTS_strip text bez mezer na zacatku a na konci
            for text in TEXTS:
                TEXTS_strip.append(text.strip())
            
            TEXT_cl_str = TEXTS_strip[int(TEXT_num) - 1].translate(str.maketrans(to_find, to_put, to_remove))
            TEXT_w_list = TEXT_cl_str.rsplit(" ")
            
            # promenne pro pocitani specifickych slov
            words_upper = 0
            words_st_upper = 0
            words_lower = 0
            numbers = []
            words = []
            total_clean_numbers = 0

            # pocet slov ve vybranem textu
            print(f"There are {len(TEXT_w_list)} words in the selected number {TEXT_num}.")

            # napln seznam words jednotlivymi slovy kvuli pocitani delek a grafu
            for slovo in TEXT_w_list:
                if slovo:
                    words.append(slovo.strip())
            
            # pocet specifickych slov
            for word in TEXT_w_list:                         
                if word and word[0].isupper(): # začínajících velkým písmenem
                    words_st_upper += 1
                    if word.isupper(): # psaných velkými písmeny
                        words_upper += 1        
                elif word.islower(): # psaných malými písmeny
                    words_lower += 1        
                elif word.isalpha() == False: # počet čísel (ne cifer), - slov co nejsou jen pismena
                    numbers.append(word)
                else:
                    break
                
            print(f"There are {words_st_upper} titlecase words.")
            print(f"There are {words_upper} uppercase words.")
            print(f"There are {words_lower} lowercase words")
            print(f"There are {len(numbers)} numeric strings.")

            # soucet cisel
            for number_to_clean in numbers:
                number_clean = ''.join([char for char in number_to_clean if char.isdigit()]) 
                total_clean_numbers += int(number_clean)
            print(f"The sum of all the numbers is {total_clean_numbers}")

            # graf

            print("----------------------------------------\n" \
                  "LEN|  OCCURENCES  |NR.\n" \
                  "----------------------------------------")
            
            ewords = list(enumerate(words)) # list tuplu napr.: (0, 'Situated')
            dict_lengths = dict() # slovnik delek klic je vzdy urcita zaznamenana delka (int) a hodnota je jeji +1 vyskyt
            
            for Slovo in range(len(words)): # prochazi tuply a zaznamenava vyskyt delek slov
                length = len(ewords[Slovo][1])
                if length in dict_lengths:
                    dict_lengths[length] += 1
                else:
                    dict_lengths[length] = 1
            print('\n')
                               
            # extrahuj klice a sortuj je
            lengths_sorted = sorted(dict_lengths.keys())
            
            # vytvor novy slovnik se sortovanymi klici pomoci komprehence
            dict_lengths_sorted = {key: dict_lengths[key] for key in lengths_sorted}
            
            for klic in dict_lengths_sorted:
                stars = dict_lengths_sorted[klic] * "*"
                if klic < 10:
                    print(f" {klic}| {stars} {dict_lengths_sorted[klic]}")
                else:
                    print(f"{klic}| {stars} {dict_lengths_sorted[klic]}")
           
        else:
            print("wrong input")          
else:
    print("unregistered user, terminating the program..")



