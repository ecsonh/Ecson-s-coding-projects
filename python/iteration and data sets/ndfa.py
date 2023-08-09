# Submitter: ecsonh(Hsu, Ecson)
# Partner  : ricarddr(Reyes, Ricardo)
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming

import goody


def read_ndfa(file : open) -> {str:{str:{str}}}:
    
    ret = {}
    for line in file:
        row = line.rstrip().split(";")
        ret[row[0]] = {}
        for val in range(1, len(row), 2):
            if row[val] not in ret[row[0]]:
                ret[row[0]][row[val]] = {row[val+1]}
            else:
                ret[row[0]][row[val]].add(row[val+1])
    return ret


def ndfa_as_str(ndfa : {str:{str:{str}}}) -> str:
    
    ret = ''
    for key in sorted(ndfa):
        ret += str("  " + key + " transitions: ")
        li = []
        for pair in ndfa[key]:
            li.append((pair, sorted([i for i in ndfa[key][pair]])))
        ret += str(sorted(li, key = lambda x: x[0])) + '\n'
    return ret

       
def process(ndfa : {str:{str:{str}}}, state : str, inputs : [str]) -> [None]:
    
    ret = [state]
    hu = {state}
    
    #print(ndfa)
    
    '''for i in inputs:
        che = 0
        sta = {}
        for o in hu:
            for key in ndfa:
                if key == o:
                    for pair in ndfa[key]:
                        if i == pair and che == 0:
                                sta = {g for g in ndfa[key][pair]}
                                ret.append((i, {g for g in ndfa[key][pair]}))
                                che = 1
                        elif i == pair and che == 1:
                                for t in ndfa[key][pair]:
                                    sta.add(t)
                                    ret[len(ret)-1][1].add(t)
                        print(i, o, key, ndfa[key], ndfa[key][pair], hu, ret)
                    if che != 1 and (o not in ndfa[key]):
                        print("Stop", i, hu)
                        ret.append((i, set()))
        hu = sta'''
    
    stop = 0
    
    for i in inputs:
        che = 0
        for key in ndfa:
            for o in hu:
                if key == o:
                    for pair in ndfa[key]:
                        if i == pair and che == 0 and stop == 0:
                                sta = {g for g in ndfa[key][pair]}
                                ret.append((i, {g for g in ndfa[key][pair]}))
                                che = 1
                        elif i == pair and che == 1 and stop == 0:
                                for t in ndfa[key][pair]:
                                    sta.add(t)
                                    ret[len(ret)-1][1].add(t)
                    if o not in ndfa[key] and stop == 0:
                        up = 0
                        for p in hu:
                            if i in ndfa[p]:
                                up = 1
                        if up == 0:
                            ret.append((i, set()))
                            stop = 1
        hu = sta
    return ret


def interpret(result : [None]) -> str:
    
    start = result[0]
    string = f"Start state = {start}\n"
    for i in result[1::]:
        y = sorted([j for j in i[1]])
        string +=f'  Input = {i[0]}; new possible states = {y}\n'

        stop = y
            
    string += f'Stop state(s) = {stop}\n'
    return string


if __name__ == '__main__':
    # Write script here
    
    ndfa = read_ndfa(open(input('Input the file name detailing the Non-Deterministic Finite Automaton: ')))
    
    print("The details of the Non-Deterministic Finite Automaton ")
    print(ndfa_as_str(ndfa))
    
    in_groups = open(input('Input the file name detailing groups of start-states and their inputs: '))
    print()
    
    for line in in_groups:
        inputs = line.rstrip().split(";")
        state = inputs[0]
        inputs.remove(state)
        
        fa_result = process(ndfa, state, inputs)
        print("NDFA: the trace from its start-state")
        print(interpret(fa_result))
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc4.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
    
    
