# Submitter: ecsonh(Hsu, Ecson)
# Partner  : ricarddr(Reyes, Ricardo)
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming
import prompt
import goody

match = 0   # Index 0 of list associate with name is match (str)
prefs = 1   # Index 1 of list associate with name is preferences (list of str)


def read_match_preferences(open_file : open) -> {str:[str,[str]]}:
    dict1={}
    with open_file as file:
        for line in file:
            list1 = []
            man = line.rstrip('\n').split(';')[0]
            for i in line.rstrip('\n').split(';'):
                list1.append(i)
            del list1[0]
            dict1[man] = list1
    return {v:[None,[i for i in dict1[v]]] for v in sorted(dict1.keys(), key = lambda x: x[0])}
    


def dict_as_str(d : {str:[str,[str]]}, key : callable=None, reverse : bool=False) -> str:
    dict1 = {v:d[v] for v in sorted(d.keys(),key= key, reverse = reverse)}
    string = ''
    for i,j in dict1.items():
        string += '  '+str(i) +' -> ' + str(j)+'\n'
    return string


def who_prefer(order : [str], p1 : str, p2 : str) -> str:
    if order.index(p1) < order.index(p2): #current rank before new rank
        return p1
    elif order.index(p1) > order.index(p2):
        return p2


def extract_matches(men : {str:[str,[str]]}) -> {(str,str)}:
    a = set()
    for i,j in men.items():
        a.add((i,j[0]))
        
    return a

        
        
    


def make_match(men : {str:[str,[str]]}, women : {str:[str,[str]]}, trace : bool = False) -> {(str,str)}:
    match_dict_men = men.copy()
    final_match = set()
    unmatched = set()
    
    for i in men.keys():
        unmatched.add(i)
    #for i,j in match_dict_men.items(): #new match
    while len(unmatched) != 0:
        for i in unmatched: #men has no match
            for g in match_dict_men[i][1]: #loop through men's list of girl
                if women[g][0]==None:
                    final_match.add((i,g))
                    women[g][0] = i #assign new man
                    match_dict_men[i][0] = g
                    match_dict_men[i][1].remove(g)
                    unmatched.remove(i)
                    if trace == "True":
                        print(f'{i} proposes to {g} (an unmatched woman); so she accepts the proposal')
                        if len(unmatched) !=0:
                            print('\nMen Preferences (current)\n')
                            print(dict_as_str(match_dict_men))
                            print('unmatched men =',unmatched,'\n')
                    break
                else:
                    match = who_prefer(women[g][1], women[g][0],i) #list, current, new
                    if match != women[g][0]:
                        unmatched.add(women[g][0])#add previous man to unmatched
                        unmatched.remove(match)

                        match_dict_men[match][0] = g #new man list 0 is the women
                        match_dict_men[match][1].remove(g)#remove women from new man's list
                        match_dict_men[women[g][0]][0] = None
                        women[g][0] = match #reassign new man
                        if trace == "True":
                            print(f'{i} proposes to {g} (a matched woman); she prefers her new match, so she accepts the proposal\n')
                            print('Men Preferences (current)\n')
                            
                            
                            print(dict_as_str(match_dict_men))
                            print('unmatched men =',unmatched,'\n')
                        break
                    else:
                        if trace == "True":
                            print(f'{i} proposes to {g} (a matched woman); she prefers her current match, so she rejects the proposal\n')
                            print('Men Preferences (current)\n')
                            print(dict_as_str(match_dict_men))
                            print('unmatched men =',unmatched,'\n')
                        
            break
    
    a = extract_matches(match_dict_men)
       
    return a
                            
 # pop the girl in every man's list?
   
  


  
    
if __name__ == '__main__':
    '''m0 = {'m1': [None, ['w3', 'w2', 'w1']], 'm2': [None, ['w3', 'w1', 'w2']], 'm3': [None, ['w2', 'w1', 'w3']]}
    w0 = {'w1': [None, ['m1', 'm2', 'm3']], 'w2': [None, ['m2', 'm1', 'm3']], 'w3': [None, ['m3', 'm2', 'm1']]}
    make_match(m0,w0)
    '''
    # Write script here
    file = input("Input the file name detailing the preferences for men: ")
    men_dict = read_match_preferences(open(file))
    file = input("Input the file name detailing the preferences for women: ")
    women_dict = read_match_preferences(open(file))

    
    print('\n'+"Men Preferences (unchanging)")
    print(dict_as_str(men_dict))
    print("Women Preferences (current)")
    print(dict_as_str(women_dict))
    trace = input('Input tracing algorithm option[True]:')
    print('\nThe final matches =',make_match(men_dict, women_dict,trace))
    
        
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc2.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
