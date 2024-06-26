"""

projekt_2.py: druhý projekt do Engeto Online Python Akademie: Bulls & Cows
author: Vratislav Peška
email: vpeska@gmail.com
discord: Vratislav Peška vratislavpeska_11865

"""
### moduly
import random
import datetime

### funkce

def Get_comp_num():
    
    """Funkce, ktera vraci pocitacem 
    nahodne vybrane 4ciferne cislo, 
    ktere nezacina nulou a neobsahuje 
    duplicitni cislice."""

    while True:

        Num = random.randint(1023, 9876) # vygeneruje nahodne 4ciferne cislo
        Digits = set(str(Num))
           
        if len(Digits) != 4: 
            continue # pokud cislo neobsahuje unikatni cislice, generuje se nove nahodne cislo
        break # ukonci se zadavani hracova cisla
    return Num # cislo se vraci jako hodnota z funkce



def Get_player_num():
    
    """Funkce, ktera zada od uzivatele 
    4ciferne cislo, ktere nezacina nulou 
    a neobsahuje duplicitni cislice. Pocita
    se kazdy pokus zadani."""

    num_of_attempts = 1
    while True: # uzivatel vklada cislo

        Num = input("Enter a number: ") # uzivatel vlozi cislo
        print(f"-----------------------------------------------")

        if not Num.isdecimal():
            print(f"This is not a number.") # upozorneni pokud to neni cislo a znova na zadani
            num_of_attempts += 1
            continue
        elif Num[0] == "0":
            print("The number must not start with zero.")
            num_of_attempts += 1
            continue
        elif int(Num) < 1000 or int(Num) > 9999: # upozorneni pokud to neni 4ciferne cislo a znovu na zadani
            print(f"The number must be 4-digits.")
            num_of_attempts += 1
            continue
        
        Digits = set(list(Num))
            
        if len(Digits) != 4: # upozorneni pokud nejsou jen unikatni cislice v cisle a znova na zadani
            print(f"The digits must be unique.")
            num_of_attempts += 1
            continue
        break # pokud vse predchozi ok, pokracujeme ke hre
    return {'Number_of_attempts': num_of_attempts, 'Number_input':Num}



def Game(Computer_num, Player_num):

    """Funkce, ktera porovnava cislo 
    od pocitace a hrace, pocita bulls
    a cows a vypisuje vysledek pro 
    spravne zadane cislo."""
    
    # promenne pro nasledujici smycku for
    bulls = 0 # vynulovane pocitadlo buliku
    i = 0 # indexuje hodnotu z Computer_num a porovnava ji s hodnotou na stejne pozici z iterovaneho Player_num
    nPlayer_num = [] # list, ktery se postupne bude plnit vsim, co neni bulik

    # cyklus, ktery spocita buliky
    for bull in list(str(Player_num)):
        if bull == list(str(Computer_num))[i]: 
            bulls += 1
            i += 1
        else:
            nPlayer_num.append(bull)
            i += 1
    
    cows = 0 # vynulovane pocitadlo krav
    
    # cyklus, ktery spocita kravy
    for cow in nPlayer_num:
        if cow in set(str(Computer_num)):
            cows += 1
    
    # promenne pro spravne pouzivani singularu/pluralu
    if cows == 1:
        Cows = "cow"
    else:
        Cows = "cows"

    if bulls < 4: # pokud zadane cislo neni vyherni, tak se vypisou bulici a kravy
        if bulls == 1:
            Bulls = "bull"
        else:
            Bulls = "bulls"

        
        print(f"{bulls} {Bulls}, {cows} {Cows}")
        stop_game = 0
        return stop_game
        
    else: # pokud je pocet buliku 4, tj. zadane cislo je vyherni, vypise se oznameni s vysledky hry
        print(f"Correct, you've guessed the right number")
        stop_game = 1
        return stop_game
        
def Evaluation(Guesses):
    
    """Function for evaluation of the player's results"""

    if Guesses == 1:
        Eval = "an improbable luck"
    elif Guesses <= 4:
        Eval = "a luck"
    elif Guesses <= 10:
        Eval = "an excellent result"
    elif Guesses <= 30:
        Eval = "a good result"
    elif Guesses <= 90:
        Eval = "an average result"
    else:
        Eval = "not so good"
    return Eval






#program pozdraví užitele a vypíše úvodní text
print(f"\n\n\n\n\n"
      f"Hi there!\n" \
      f"-----------------------------------------------\n" \
      f"I've generated a random 4 digit number for you.\n" \
      f"It does not start with zero and the digits are unique.\n" \
      f"Let's play a bulls and cows game.\n" \
      f"-----------------------------------------------\n") 


#program dále vytvoří tajné 4místné číslo (číslice musí být unikátní a nesmí začínat 0)
Comp_num = Get_comp_num()

print(Comp_num) # nakonec odstranit!!!

stop = 0 # hra pobezi tak dlouho, dokud hrac neuhadne cislo
attempt = 0 # pocitadlo vsech pokusu, tj. vcetne nesmyslu typu 0123, 123a, 12345, 1123 atd.
Num_guess = 0 # pocitadlo pokusu se spravnymi cisly
Start_T = datetime.datetime.now() # Start mereni casu od prvniho pokusu 


while stop == 0:
    get_play_num = Get_player_num() # vrati cislo od hrace a pocet pokusu o jeho zadani ve forme dictionary {'Number_of_attempts': num_of_attempts, 'Number_input':Num}
    Play_num = get_play_num['Number_input']
    stop = Game(Comp_num, Play_num) # ma hra pokracovat?
    attempt = attempt + get_play_num['Number_of_attempts']
    Num_guess += 1

Stop_T = datetime.datetime.now()

Time = Stop_T - Start_T
hours, remainder = divmod(Time.seconds, 3600)
minutes, seconds = divmod(remainder, 60)


Eval_final = Evaluation(attempt)

if attempt == 1:
    attempts = "guess"
else:
    attempts = "guesses"

# Cas ve formatu hr:min:sec
Final_time = f"{hours:02}h:{minutes:02}min:{seconds:02}sec"
print(f"in {attempt} {attempts}, from that {Num_guess} of relevant numbers, in total {Final_time}\n" \
      f"-----------------------------------------------\n"
      f"That's {Eval_final}")


    

    



