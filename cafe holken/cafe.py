def FunctionalCafe():
    #decide cost of different coffe
    small = 10
    regular = 15
    large = 20
   
    #input för användarens budget
    user_budget = input('Hur mycket pengar kan du använda? ')
    
    try: #check if variable is an integer
        user_budget = int(user_budget)
    except: #if not...
        print('Skriv ett numeriskt värde!')
        exit()
    
    #om användarens budget är större än 0
    if user_budget > 0:
        #om användarens budget är större än eller lika med large (20)
        if user_budget >= large:
            #svara;
            print('Du har råd med en stor kaffe.')
            #om användarens budget är lika med large (20)
            if user_budget == large:
                #svara;
                print('Det är precis.')
            #annars;
            else:
                #svara; användarens budget - priset för kaffet
                print('Din växel blir ', user_budget - large)
        #om användarens budget är större än eller lika med regular (15)
        elif user_budget >= regular:
            #svara;
            print('Du har råd med en normal kaffe.')
            #om användarens budget är lika med regular (15)
            if user_budget == small:
                #svara;
                print('Det är precis.')
            #annars;
            else:
                #svara; användarens budget - priset för kaffet
                print('Din växel blir ', user_budget - small)
        #om användarens budget är större än eller lika med small (10)
        elif user_budget >= small:
            #svara;
            print('Du har råd med en normal kaffe.')
            #om användarens budget är lika med small (10)
            if user_budget == small:
                #svara;
                print('Det är precis.')
            #annars;
            else:
                #svara; användarens budget - priset för kaffet
                print('Din växel blir ', user_budget - small)
  