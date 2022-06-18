#Traveller_toolkit.py

from random import randint

menu_options = {
    1: 'Generate Random Animal Encounters',
    2: 'Generate Random Patron Encounter',
    3: 'Generate Random Person Encounters',
    4: 'Generate Random Starship Encounters',
    5: 'Quit',
}

def print_menu():
    #prints a formatted main menu
    print ('What would you like to do?')
    for key in menu_options.keys():
        print (key, '--', menu_options[key])

def humanoid_reaction():
    '''Generates a random number between 2-12 inclusive and compares it
    against the Classic Traveller reaction table.
    
    A second 2-12 result is consulted when the table indicates a throw
    to determine whether a hostile character attacks.'''

    reaction_roll = randint(2, 12)
    attack = randint(2,12)

    if reaction_roll == 2:
        reaction = ('violent and immediately attacks!')
    if reaction_roll == 3: # Hostile. Attacks on 5+
        if attack < 4: 
            reaction = ('hostile.')
        else: 
            reaction = ('hostile and attacks after consideration!')
    if reaction_roll == 4: # Hostile. Attacks on 8+
        if attack < 7: 
            reaction = ('hostile.')
        else: 
            reaction = ('hostile and attacks after consideration!')
    if reaction_roll == 5: 
        reaction = ('hostile and may attack.')
    if reaction_roll == 6: 
        reaction = ('unreceptive.')
    if reaction_roll == 7: 
        reaction = ('non-committal.')
    if reaction_roll == 8: 
        reaction = ('interested.')
    if reaction_roll == 9: 
        reaction = ('intrigued.')
    if reaction_roll == 10: 
        reaction = ('responsive.')
    if reaction_roll == 11: 
        reaction = ('enthusiastic.')
    if reaction_roll == 12: 
        reaction = ('genuinely friendly.')

    return reaction

def get_gender():
    '''Assign these fuckers a gender at birth'''
    ratio = randint (1, 100)
    if ratio > 51:
        return 'he'
    else:
        return 'she'

# data and functions specific to the random animal encounter generator
def generate_random_animal_encounters():
    print(
        '''Oops! The Random Animal Encounter Generator is currently under 
        construction!\n'''
        )

# data and functions specific to the random patron encounter generator
patron_table_ct = {
'1, 1': 'an arsonist',
'1, 2': 'a crewman',
'1, 3': 'a shipowner',
'1, 4': 'a diplomat',
'1, 5': 'a mercenary',
'1, 6': 'a noble',
'2, 1': 'a cutthroat',
'2, 2': 'a peasant',
'2, 3': 'a tourist',
'2, 4': 'a courier',
'2, 5': 'a naval officer',
'2, 6': 'a playboy',
'3, 1': 'an assassin',
'3, 2': 'Rumor',
'3, 3': 'a merchant',
'3, 4': 'a spy',
'3, 5': 'a marine officer',
'3, 6': 'an avenger',
'4, 1': 'a hijacker',
'4, 2': 'a clerk',
'4, 3': 'a police officer',
'4, 4': 'a scholar',
'4, 5': 'a scout',
'4, 6': 'an emigre',
'5, 1': 'a smuggler',
'5, 2': 'a soldier',
'5, 3': 'a scout',
'5, 4': 'a governor',
'5, 5': 'an army officer',
'5, 6': 'a speculator',
'6, 1': 'a terrorist',
'6, 2': ' a shopkeeper',
'6, 3': 'Rumor',
'6, 4': 'an administrator',
'6, 5': 'a mercenary',
'6, 6': 'Rumor',
}

patron_table_ttb_1 = {
'1, 1': 'a naval officer',
'1, 2': 'a scout administrator',
'1, 3': 'a marine officer',
'1, 4': 'a hunter',
'1, 5': 'a starport warden',
'1, 6': 'a naval officer',
'2, 1': 'a reporter',
'2, 2': 'a technician',
'2, 3': 'a doctor',
'2, 4': 'a rogue',
'2, 5': 'a noble',
'2, 6': 'a government official',
'3, 1': 'a barbarian',
'3, 2': 'a scout pilot',
'3, 3': 'a pirate',
'3, 4': 'a researcher',
'3, 5': 'a writer',
'3, 6': 'a professor',
'4, 1': 'an underworld leader',
'4, 2': 'a scientist',
'4, 3': 'a belter',
'4, 4': 'a naval architect',
'4, 5': 'a steward',
'4, 6': 'a financier',
'5, 1': 'a navigator',
'5, 2': 'a swindler',
'5, 3': 'a broker',
'5, 4': 'an arms merchant',
'5, 5': 'a doctor',
'5, 6': 'a pilot',
'6, 1': 'a merchant',
'6, 2': 'a rogue',
'6, 3': 'an embezzler',
'6, 4': 'a belter',
'6, 5': 'a bureaucrat',
'6, 6': 'a diplomat',
}

patron_table_ttb_2 = {
'1, 1': 'an arsonist',
'1, 2': 'a cutthroat',
'1, 3': 'an assassin',
'1, 4': 'a hijacker',
'1, 5': 'a smuggler',
'1, 6': 'a terrorist',
'2, 1': 'a crewmember',
'2, 2': 'a peasant',
'2, 3': 'Rumor',
'2, 4': 'a clerk',
'2, 5': 'a soldier',
'2, 6': 'a shopkeeper',
'3, 1': 'a shipowner',
'3, 2': 'a tourist',
'3, 3': 'a merchant',
'3, 4': 'a police officer',
'3, 5': 'a scout',
'3, 6': 'Rumor',
'4, 1': 'a diplomat',
'4, 2': 'a courier',
'4, 3': 'a spy',
'4, 4': 'a scholar',
'4, 5': 'a governor',
'4, 6': 'an administrator',
'5, 1': 'a mercenary',
'5, 2': 'a naval officer',
'5, 3': 'a marine officer',
'5, 4': 'a scout',
'5, 5': 'an army officer',
'5, 6': 'a mercenary',
'6, 1': 'a noble',
'6, 2': 'a playboy',
'6, 3': 'an avenger',
'6, 4': 'an emigre',
'6, 5': 'a speculator',
'6, 6': 'Rumor',
}

rumor_matrix = {
'1, 1': 'A',
'1, 2': 'G',
'1, 3': 'I',
'1, 4': 'K',
'1, 5': 'M',
'1, 6': 'O',
'2, 1': 'B',
'2, 2': 'U',
'2, 3': 'U',
'2, 4': 'X',
'2, 5': 'X',
'2, 6': 'P',
'3, 1': 'C',
'3, 2': 'U',
'3, 3': 'Y',
'3, 4': 'Z',
'3, 5': 'X',
'3, 6': 'Q',
'4, 1': 'D',
'4, 2': 'W',
'4, 3': 'Y',
'4, 4': 'Z',
'4, 5': 'V',
'4, 6': 'R',
'5, 1': 'E',
'5, 2': 'W',
'5, 3': 'W',
'5, 4': 'V',
'5, 5': 'V',
'5, 6': 'S',
'6, 1': 'F',
'6, 2': 'H',
'6, 3': 'J',
'6, 4': 'L',
'6, 5': 'N',
'6, 6': 'T',
}

rumor_list = {
'A': 'some background information',
'B': 'a minor fact',
'C': 'a major fact',
'D': 'a partial (potentially misleading) fact',
'E': 'a veiled clue',
'F': 'some information leading to trap',
'G': 'some location data',
'H': 'an important fact',
'I': 'an obvious clue',
'J': 'some completely false information',
'K': 'new terminology',
'L': 'a library data reference',
'M': 'some helpful data',
'N': 'some location data',
'O': 'a reliable recommendation to action',
'P': 'a major fact',
'Q': 'some background information',
'R': 'a minor fact',
'S': 'a veiled clue',
'T': 'a misleading clue',
'U': 'some broad background information',
'V': 'some misleading background information',
'W': 'a reference to library data',
'X': 'some general location data',
'Y': 'some specific background data',
'Z': 'some misleading background data',
}

patron_generator_menu = {
    1: 'Classic Traveller (1977)',
    2: 'The Traveller Book (1981) Table One',
    3: 'The Traveller Book (1981) Table Two',
    4: 'The Traveller Book (1981) Rumor Matrix',
    5: 'Go Back',
}

ttb1_x_mod_menu = {
    1: 'Navy',
    2: 'Merchant Marine',
    3: 'Neither',
    4: 'Go Back',
}

ttb1_y_mod_menu = {
    1: 'Streetwise-1 +',
    2: 'Admin-1 +',
    3: 'Both',
    4: 'Neither',
    5: 'Go Back',
}

ttb2_x_mod_menu = {
    1: 'Merchant marine',
    2: 'Noble (Soc 11+)',
    3: 'Both',
    4: 'Neither',
    5: 'Go Back',
}

ttb2_y_mod_menu = {
    1: 'The "other" service',
    2: 'The army',
    3: 'The marines',
    4: 'None of the above',
    5: 'Go back',
}

def print_patron_menu():
    # Prints a formatted Starport Class selection menu

    print ('From which table would you like to generate a patron or rumor?\n')
    for key in patron_generator_menu.keys():
        print (key, '--', patron_generator_menu[key])

def get_rumor():
    x = randint(1, 6)
    y = randint(1, 6)
    rumor_key = str(x) +', '+ str(y)
    rumor_type = rumor_matrix[rumor_key]
    print ("You overhear:", rumor_list[rumor_type])

def get_rumor_number():
    number_of_rumors = 0
    while number_of_rumors < 1: 
        number_of_rumors_input = input('''
        How many rumors would you like to generate?
        Enter "go back" to return to patron menu.\n
        ''')
        try:
            number_of_rumors = int(number_of_rumors_input)
        except:
            if number_of_rumors_input.lower() == 'go back':
                break
            else:
                print('\nPlease input numbers or "go back" only.')
    print('\n Generating rumors...')
    
    rumor_id = 1
    while (rumor_id <= number_of_rumors):
        print('\nRumor', rumor_id, ':')
        rumor_check = randint(2, 12)
        if rumor_check < 7:
            print('No rumor.')
        else:
            get_rumor()
        rumor_id = rumor_id + 1
    else:
        print('\nReturning to patron menu...')

def get_ct_patron():
    '''Doc string'''
    x = randint(1, 6)
    y = randint(1, 6)
    patron_key = str(x) +', '+ str(y)
    if patron_table_ct[patron_key].lower() != 'rumor':
        reaction = humanoid_reaction()
        patron_gender = get_gender()
        print("You spend a week looking for employment. You're approached by", patron_table_ct[patron_key] + '.')
        print('After considering your group,', patron_gender, 'is', reaction)
    else:
        print('Generating Rumor...')
        get_rumor()
    
def get_ct_patron_number():
    number_of_patron_encounters = 0
    while number_of_patron_encounters < 1: 
        number_of_patron_encounters_input = input('''
        How many patrons would you like to generate?
        Enter "go back" to return to patron menu.\n
        ''')
        try:
            number_of_patron_encounters = int(
                number_of_patron_encounters_input
                )
        except:
            if number_of_patron_encounters_input.lower() == 'go back':
                break
            else:
                print('\nPlease input numbers or "go back" only.')
    print('\n Generating encounters...')
    
    patron_encounter_id = 1
    while (patron_encounter_id <= number_of_patron_encounters):
        print('\nEncounter', patron_encounter_id, ':')
        patron_encounter_check = randint(1, 6)
        if patron_encounter_check < 5:
            print('No encounter.')
        else:
            get_ct_patron()
        patron_encounter_id = patron_encounter_id + 1
    else:
        print('\nReturning to patron menu...')

def print_ttb1_x_menu():
    print ('\nIs the character a veteran of either the:\n')
    for key in ttb1_x_mod_menu.keys():
        print (key, '--', ttb1_x_mod_menu[key])

def print_ttb1_y_menu():
    print ('\nDoes the character possess:\n')
    for key in ttb1_y_mod_menu.keys():
        print (key, '--', ttb1_y_mod_menu[key])

def get_ttb1_patron(a, b):
    '''Doc string'''
    x_mod = a
    y_mod = b
    x = randint(1, 6) + int(x_mod)
    y = randint(1, 6) + int(y_mod)
    if x < 1: 
        x = 1
    if x > 6:
        x = 6
    if y < 1:
        y = 1
    if y > 6:
        y = 6
    patron_key = str(x) +', '+ str(y)
    if patron_table_ttb_1[patron_key].lower() != 'rumor':
        reaction = humanoid_reaction()
        patron_gender = get_gender()
        print("You spend a week looking for employment. You're approached by", patron_table_ttb_1[patron_key] + '.')
        print('After considering your group,', patron_gender, 'is', reaction)
    else:
        print('Generating Rumor...')
        get_rumor()

def get_ttb1_patron_number(a, b):
    x_mod = a
    y_mod = b
    number_of_patron_encounters = 0
    while number_of_patron_encounters < 1: 
        number_of_patron_encounters_input = input('''
        How many patrons would you like to generate?
        Enter "go back" to return to patron menu.\n
        ''')
        try:
            number_of_patron_encounters = int(
                number_of_patron_encounters_input
                )
        except:
            if number_of_patron_encounters_input.lower() == 'go back':
                break
            else:
                print('\nPlease input numbers or "go back" only.')
    print('\n Generating encounters...')
    
    patron_encounter_id = 1
    while (patron_encounter_id <= number_of_patron_encounters):
        print('\nEncounter', patron_encounter_id, ':')
        patron_encounter_check = randint(1, 6)
        if patron_encounter_check < 5:
            print('No encounter.')
        else:
            get_ttb1_patron(x_mod, y_mod)
        patron_encounter_id = patron_encounter_id + 1
    else:
        print('\nReturning to patron menu...')

def get_ttb1_mods():
    print ('''
    The patron tables in The Traveller Book are modified
    by the character responsible for finding the patron.
    Let's determine those modifiers now.''')
    x_mod = None
    y_mod = None
    while x_mod == None:
        print_ttb1_x_menu()
        x_mod_input = input()
        try:
            x_mod_int = int(x_mod_input)
        except:
            if x_mod_input.lower() == 'go back':
                generate_random_patron_encounters()
            else:
                print('Please input numbers or "go back" only.')
                continue
        if x_mod_int == 4:
            generate_random_patron_encounters()

        elif x_mod_int == 1:
            x_mod = -1
        elif x_mod_int == 2:
            x_mod = 1
        elif x_mod_int == 3:
            x_mod = 0
        else:
            print('Please enter a valid selection.')
            continue

    while y_mod == None:
        print_ttb1_y_menu()
        y_mod_input = input('Input:\n')

        try:
            y_mod_int = int(y_mod_input)
        except:
            if y_mod_input.lower() == 'go back':
                generate_random_patron_encounters()
            else:
                print('Please input numbers or "go back" only.')
                continue

        if y_mod_int == 5:
            generate_random_patron_encounters()
        elif y_mod_int == 1:
            y_mod = -1
        elif y_mod_int == 2:
            y_mod = 1
        elif y_mod_int < 5:
            y_mod = 0
        else:
            print('Please enter a valid selection.')
            continue
        get_ttb1_patron_number(x_mod, y_mod)
    
def print_ttb2_x_menu():
    print ('\nWhich applies to the character?\n')
    for key in ttb2_x_mod_menu.keys():
        print (key, '--', ttb2_x_mod_menu[key])

def print_ttb2_y_menu():
    print ('\nDid the character serve in:\n')
    for key in ttb2_y_mod_menu.keys():
        print (key, '--', ttb2_y_mod_menu[key])

def get_ttb2_patron(a, b):
    '''Doc string'''
    x_mod = a
    y_mod = b
    x = randint(1, 6) + int(x_mod)
    y = randint(1, 6) + int(y_mod)
    if x <= 0:
        x = 1
    if x > 6:
        x = 6
    if y <= 0:
        y = 1
    if y > 6:
        y = 6
    patron_key = str(x) +', '+ str(y)
    if patron_table_ttb_2[patron_key].lower() != 'rumor':
        reaction = humanoid_reaction()
        patron_gender = get_gender()
        print("You spend a week looking for employment. You're approached by", patron_table_ttb_2[patron_key] + '.')
        print('After considering your group,', patron_gender, 'is', reaction)
    else:
        print('Generating Rumor...')
        get_rumor()

def get_ttb2_patron_number(a, b):
    x_mod = a
    y_mod = b
    number_of_patron_encounters = 0
    while number_of_patron_encounters < 1: 
        number_of_patron_encounters_input = input('''
        How many patrons would you like to generate?
        Enter "go back" to return to patron menu.\n
        ''')
        try:
            number_of_patron_encounters = int(
                number_of_patron_encounters_input
                )
        except:
            if number_of_patron_encounters_input.lower() == 'go back':
                break
            else:
                print('\nPlease input numbers or "go back" only.')
    print('\n Generating encounters...')
    
    patron_encounter_id = 1
    while (patron_encounter_id <= number_of_patron_encounters):
        print('\nEncounter', patron_encounter_id, ':')
        patron_encounter_check = randint(1, 6)
        if patron_encounter_check < 5:
            print('No encounter.')
        else:
            get_ttb2_patron(x_mod, y_mod)
        patron_encounter_id = patron_encounter_id + 1
    else:
        print('\nReturning to patron menu...')

def get_ttb2_mods():
    print ('''
    The patron tables in The Traveller Book are modified
    by the character responsible for finding the patron.
    Let's determine those modifiers now.''')
    x_mod = None
    y_mod = None
    while x_mod == None:
        print_ttb2_x_menu()
        x_mod_input = input()
        try:
            x_mod_int = int(x_mod_input)
        except:
            if x_mod_input.lower() == 'go back':
                generate_random_patron_encounters()
            else:
                print('Please input numbers or "go back" only.')
                continue
        if x_mod_int == 5:
            generate_random_patron_encounters()
        elif x_mod_int == 1:
            x_mod = -1
        elif x_mod_int == 2:
            x_mod = 1
        elif x_mod_int < 5:
            x_mod = 0
        else:
            print('Please enter a valid selection.')
            continue

    while y_mod == None:
        print_ttb1_y_menu()
        y_mod_input = input()
        try:
            y_mod_int = int(y_mod_input)
        except:
            if y_mod_input.lower() == 'go back':
                generate_random_patron_encounters()
            else:
                print('Please input numbers or "go back" only.')
                continue
        if y_mod_int == 5:
            generate_random_patron_encounters()
        elif y_mod_int == 1:
            y_mod = -1
        elif y_mod_int < 4:
            y_mod = 1
        elif y_mod_int == 4:
            y_mod = 0
        else:
            print('Please enter a valid selection.')
            continue
        get_ttb2_patron_number(x_mod, y_mod)
   
def get_patron_table():

    '''This function prompts the user to select which patron table
    to use for the generation of encounters.
    
    It loops until valid input is received, then calls the appropriate
    function.'''

    patron_table = 0
    while patron_table != [1, 2, 3, 4, 5]:
        print_patron_menu()
        patron_table_input = (input('Input: '))
        try:
            patron_table = int(patron_table_input)
        except:
            if patron_table_input.lower() == 'go back':
                return 5
            else:
                print(
                    '\nIt would be less work for you to enter a digit between 1 and 5. :3'
                    )
                continue
        if patron_table == 1:
            print('\nConsulting the Classic Traveller Patron Table...')
            get_ct_patron_number()
        elif patron_table == 2:
            print('\nConsulting the The Traveller Book Patron Table One...')
            get_ttb1_mods()
        elif patron_table == 3:
            print('\nConsulting the The Traveller Book Patron Table Two...')
            get_ttb2_mods()
        elif patron_table == 4:
            print('\nConsulting the Rumor Matrix...')
            get_rumor_number()
        elif patron_table == 5:
            return 5
        else:
            print(
                '\nInvalid input. Please enter a number between 1 and 5.\n'
                )

def generate_random_patron_encounters():
    go_back_patron = get_patron_table()
    if go_back_patron == 5:
        return

#data and functions specific to the random patron encounter generator
def generate_random_person_encounters():
    print(
        '''Oops! The Random Person Encounter Generator is currently under 
        construction!\n'''
        )

# data and functions specific to the random starship encounter generator
starport_class_menu = {
    1: 'A',
    2: 'B',
    3: 'C',
    4: 'D',
    5: 'E',
    6: 'X',
    7: 'Go Back'
}

def print_starport_menu():
    # Prints a formatted Starport Class selection menu

    print ('\nSelect Starport Class:\n')
    for key in starport_class_menu.keys():
        print (key, '--', starport_class_menu[key])

def get_starport_class():

    '''This function prompts the user to select which Starport Class
    is in the system for which they are generating starship encounters.
    
    It loops until valid input is received, and returns the Starport's
    corresponding dice modifier for the encounter table.'''

    starport_class = 0
    while starport_class != [1, 2, 3, 4, 5, 6]:
        print_starport_menu()
        starport_class_input = (input('Input: '))
        try:
            starport_class = int(starport_class_input)
        except:
            if starport_class_input.lower() == 'a':
                return 6
            elif starport_class_input.lower() == 'b':
                return 4
            elif starport_class_input.lower() == 'c':
                return 2
            elif starport_class_input.lower() == 'd':
                return 1
            elif starport_class_input.lower() == 'e':
                return -2
            elif starport_class_input.lower() == 'x':
                return -4
            elif starport_class_input.lower() == 'go back':
                return 7
            else:
                print(
                    '''\nThe Society of Many Journeys currently classifies
                    starports as A, B, C, D, E, or X.'''
                )
                continue
        if starport_class == 1:
            return 6
        elif starport_class == 2:
            return 4
        elif starport_class == 3:
            return 2
        elif starport_class == 4:
            return 1
        elif starport_class == 5:
            return -2
        elif starport_class == 6:
            return -4   
        elif starport_class == 7:
            return 7
        else:
            print(
                '\nInvalid input. Please enter a number between 1 and 7.\n'
                )

def get_starship_encounter(starport_modifier):

    '''This function determines the specific ship class encountered
    by randomly generating a number between 2-12 inclusive and comparing it
    to the Classic Traveller starship encounter table. 
    
    If an integer is passed into the function, it will modify this roll.
    
    If an encounter is rolled, it calls the humanoid_reaction() function,
    generates a reaction, and prints both the ship encounted and the reaction
    of it's crew.'''

    starship_roll = randint(2, 12) + starport_modifier
    starship_subtype_roll = randint(2, 12)

    if starship_roll <= 8: 
        print("No Encounter.")
    else:
        if starship_roll <= 11: 
            shipclass = 'Type-A Free Trader.'
        elif starship_roll == 12:
            if starship_subtype_roll <=6: 
                shipclass = 'Type-S Scout/Courier (Pirate).'
            elif starship_subtype_roll == 7:
                shipclass = 'Type-Y Yacht (Pirate).'
            elif starship_subtype_roll >= 8:
                shipclass = 'Type-C Cruiser (Pirate).'
        elif starship_roll == 13:
            if starship_roll >= 8:
                shipclass = 'Type-M Subsidized Merchant.'
            elif starship_subtype_roll < 8:
                shipclass = 'Type-R Subsidized Liner.'
        elif starship_roll == 14:
            if starship_subtype_roll <=6:
                shipclass = 'Type-S Scout/Courier on patrol.'
            elif starship_subtype_roll == 7:
                shipclass = 'Type-Y Yacht on patrol.'
            elif starship_subtype_roll >= 8:
                shipclass = 'Type-C Cruiser on patrol.'
        elif starship_roll == 15:
            if starship_subtype_roll >= 8:
                shipclass = 'Type-M Subsidized Merchant.'
            elif starship_subtype_roll < 8:
                shipclass = 'Type-R Subsidized Liner.'
        elif starship_roll <= 17:
            shipclass = 'Type-Y Yacht.'
        elif starship_roll == 18:
            if starship_subtype_roll <=6:
                shipclass = 'Type-S Scout/Courier on patrol.'
            elif starship_subtype_roll == 7:
                shipclass = 'Type-Y Yacht on patrol.'
            elif starship_subtype_roll >= 8:
                shipclass = 'Type-C Cruiser on patrol.'

        print("Scanners detecting:", shipclass)
        print("It's crew is", humanoid_reaction(),)

def generate_random_starship_encounters():

    '''Starship Encounters in Traveller are generated by comparing the value
    of two 6-sided dice against a table that ranges from 2-18. This dice roll
    is further modified by the class of the system's starport to simulate
    the volume of in-system traffic.
    
    This function captures the starport class modifier by calling
    get_starport_class() and outputs a user-specified number of
    encounters for that port class before returning to the main
    menu.
    '''
    starport_dice_mod = get_starport_class()
    if starport_dice_mod == 7:
        print('\nReturning to main menu...\n')
        return
    else:
# Ask user how many encounters to generate, then convert their answer to 
# an integer.
        number_of_starship_encounters = 0
        while number_of_starship_encounters < 1: 
            number_of_starship_encounters_input = input(
                '\nHow many starship encounters would you like to generate?\n'
                )
            try:
                number_of_starship_encounters = int(
                    number_of_starship_encounters_input
                    )
            except:
                print('\nPlease input numbers only.')
        print('\n Generating encounters...\n')
    
# Call get_starship_encounters() to generate starships encounted and their
# reactions to the player characters and label each result with an
# incremented header.
    starship_encounter_id = 1
    while (starship_encounter_id <= number_of_starship_encounters):
        print('\nEncounter', starship_encounter_id, ':')
        get_starship_encounter(starport_dice_mod)
        starship_encounter_id = starship_encounter_id + 1
    else:
        print('\nReturning to main menu...\n')
    
# Main Menu
if __name__ == "__main__":
    while(True):
        print("Welcome to the Classic Traveller Toolkit!\n")
        print_menu()
        option = ''
        try:
            option = int(input('\nInput: '))
        except:
            print(
                '\nPlease enter numbers only.\n'
                )
            continue
        # Check which choice was entered and act accordingly        
        if option == 1: 
            print('\nInitializing Random Animal Encounter Generator...\n')
            generate_random_animal_encounters()
        elif option == 2:
            print('\nInitializing Random Patron Encounter Generator...\n')
            generate_random_patron_encounters()
        elif option == 3:
            print('\nInitializing Random Person Encounter Generator...\n')
            generate_random_person_encounters()
        elif option == 4:
            print('\nInitializing Random Starport Encounter Generator...\n')
            generate_random_starship_encounters()
        elif option == 5:
            print('\nExiting...')
            exit()
        else: 
            print(
                '\nInvalid input. Please enter a number between 1 and 5.\n'
                )