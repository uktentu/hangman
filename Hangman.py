import random as rd

def drawing(guess_chances):
    for i in range(4):
        print(' _',end=' ')
    print('\n|          |')
    if guess_chances==6:
        for i in range(5):
            print('|')
    elif guess_chances==5:
        print('|          O')
        for i in range(4):
            print('|')
    elif guess_chances==4:
        print('|          O')
        print('|          |')
        for i in range(4):
            print('|')
    elif guess_chances==3:
        print('|          O')
        print('|         /|')
        for i in range(3):
            print('|')
    elif guess_chances==2:
        print('|          O')
        print('|         /|'+str(chr(92)))
        for i in range(2):
            print('|')
    elif guess_chances==1:
        print('|          O')
        print('|         /|'+str(chr(92)))
        print('|         /')
        for i in range(1):
            print('|')

    elif guess_chances==0:
        print('|          O')
        print('|         /|'+str(chr(92)))
        print('|         / '+str(chr(92)))
        print('|')

def play():
    
# Word lists
    Places = [['Places'],['Paris','France','Peru','New Zealand','Colosseum','London','Australia','Iceland','Maldives','Turkey','Thailand','New York City',
            'Netherlands','Mumbai','Maharastra','Bangkok','Dubai','Hong Kong','Egypt','Kolkata','West Bengal'],
            ['MachuPicchu','The Grand Canyon','Great Barrier Reef','Pamukalle','Santorini','Florence','Toronto','Victoria',"British Columbia",'Whistler'],
            ['The Independence Mountains','Dogon Country Mali',"Tiger Nest Monastery",'Bobbili','The Amazon And Rupununi Savannah','The Great Dune','Baliem Valley','Mt Bisoke','Forbidden Valley']]

    Finance=[['Finance related terms'],['Compound interest','Net worth','Capital gains','Stocks','Balance','Insurance','Principle','World Trade Organization'],
            ['Gross domestic product','Free trade area','International Trade Administration','Least Developed Country'],
            ['United Nations Conference on Trade and Development','Multinational Enterprise','Advance pricing agreement','Alternative minimum tax']]

    Games=[['Games'],['Pubg','Call of Duty','Valorant','Temple Run','Subway Surfers','War Robots','Minecraft','Among Us','Clash of clans','GTA','Pokemon Go','Flappy Bird','Candy Cruch','Fortuite'],
        ['Fortnite','Genshin Impact','Clash Royale','Brawl Stars','Mobile Legends','Plants vs Zombies','Asphalt legends','Pokemon Go','FiFA'],
        ["Altos Odyssey",'Metal Slug Anthology','Pirates of Black Cove','Wonder Boy in Monster World','Red Dead Redemption','Hitman']]

    total = Places,Finance,Games

    guess_chances=6 # defining chances limit to 6

    mode = int(input('''Choose the Mode of play
    1 --- Easy
    2 --- Medium
    3 --- Hard
    '''))
    #taking the input for choosing the category
    c=int(input('''\nIf you want to play RANDOMLY Enter 0 Or If you want play in the categories ,
    Choose
    1 --- Places 
    2 --- Finance related terms
    3 --- Names of Games
    '''))
    # picking the random word from the list choosen or randomly
    if c == 0:
        category = rd.choice(total)
        word=(rd.choice(category[mode]))
    elif c == 1:
        category = Places
        word=(rd.choice(category[mode]))
    elif c == 2:
        category = Finance
        word=(rd.choice(category[mode]))
    elif  c== 3:
        category = Games
        word=(rd.choice(category[mode]))
    else:
        print('You enterd a innput that not in the list,So we considering the random category')
        category = rd.choice(total)
        word=(rd.choice(category[mode]))

    a=[] # For storing alphabets
    b=[] # For storing leters not in actuall word
    guessed_word = [] # For storing guessed word
    check=True
    #Creating a list containing Alphabets
    for i in range(65,91):
        a.append(chr(i))

    l=list(word.upper())

    # Generating the guess word
    for i in l:
        if i.isalpha():
            guessed_word.append('_')
        else:
            guessed_word.append(i)

    # telling the No.of letters that the word contain
    print('The Number of letters in the word is ',guessed_word.count('_'),' in the category of ',''.join(category[0]))
    print('\n\n',guessed_word)
    #Main
    while guess_chances>0:

        if guess_chances==1 and check:
            print('''\t\t\tOptional : If you want Hint enter 0
            \t\t\tNote: Hint will removes 5 random letters which are not a part of the word\n''')

    
        if word.upper()==(''.join(guessed_word)):
            print('\nYou guessed it right !!!','Yes the word is ',word,'\n\nYOU WON,\t\t YOU SAVED HIS LIFE\n\n')
            break

        print('\nEnter a letter in ',a,"\n")
        guess=input().upper()
    
        if guess not in a and guess!='0':
            print('\n',guess,' is not in the Shown list of letters , Check once again and carry on, You have only ',guess_chances,' chances.')
    
        if guess=='0'and check==False:
            print('\n You have used chance of using Hints, So carry on Guessing')
        
        if guess in a:
            if guess not in l:
                guess_chances-=1

            else:
                for i in range(l.count(guess)):
                    guessed_word[l.index(guess)]=guess
                    l[l.index(guess)]='_'

            drawing(guess_chances)
            a[a.index(guess)]="_"   
            print('\n',' '.join(guessed_word))
    
            print('\nYou have only ',guess_chances,' Chance left')
    
        # Block For Hint
        if guess_chances==1 and check and guess=='0':
            for i in a:
                if (i not in l) and i!='_':
                    b.append(i)
            for j in range(4):
                k=rd.choice(b)
                a[a.index(k)]="_"
                b.pop(b.index(k))
            check =False
    

    if guess_chances==0:
        print('\nThe word is ',word,'\n\n!!! Sorry,You ran out of chances !!!\t YOU KILLED HIM\n\n')
    
    p=input('Do you want to play again Y or N:  ')
    if p=='Y' or p=='y':
        play()
    else:
        print('\n\nThank for playing the game.\n\n')

#for first time
play()

