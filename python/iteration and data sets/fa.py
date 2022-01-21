# Submitter: ecsonh(Hsu, Ecson)
# Partner  : ricarddr(Reyes, Ricardo)
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming
import goody


def read_fa(file : open) -> {str:{str:str}}:
    
    ret = {}
    for line in file:
        row = line.rstrip().split(";")
        ret[row[0]] = {}
        for val in range(1, len(row), 2):
            ret[row[0]][row[val]] = row[val+1]
    return ret


def fa_as_str(fa : {str:{str:str}}) -> str:
    
    ret = ''
    for key in sorted(fa):
        ret += str("  " + key + " transitions: ")
        li = []
        for pair in fa[key]:
            li.append((pair, fa[key][pair]))
        ret += str(sorted(li, key = lambda x: x[0])) + '\n'
    return ret

    
def process(fa : {str:{str:str}}, state : str, inputs : [str]) -> [None]:
    
    ret = []
    ret.append(state)
    
    for i in inputs:
        che = 0
        for key in fa:
            if state == key:
                for tr in fa[key]:
                    if tr == i and che != 1:
                        ret.append((tr, fa[key][tr]))
                        state = fa[key][tr]
                        che = 1
                    elif i not in fa[key] and che != 1:
                        ret.append((i, None))
                        che = 1
    return ret


def interpret(fa_result : [None]) -> str:

    start = fa_result[0]
    string = f"Start state = {start}\n"
    for i in fa_result[1::]:
        if i[1] != None:
            string +=f'  Input = {i[0]}; new state = {i[1]}\n'
            stop = i[1]
        else:
            string +=f'  Input = {i[0]}; illegal input: simulation terminated\n'
            stop = i[1]
            break
    string += f'Stop state = {stop}\n'
    return string


if __name__ == '__main__':
    # Write script here
    fa = read_fa(open(input("Input the file name detailing the Finite Automaton: ")))
    
    print("\nThe details of the Finite Automaton")
    print(fa_as_str(fa))
    
    in_groups = open(input("Input the file name detailing groups of start-states and their inputs: "))
    print()
    
    for line in in_groups:
        inputs = line.rstrip().split(";")
        state = inputs[0]
        inputs.remove(state)
        
        fa_result = process(fa, state, inputs)
        print("FA: the trace from its start-state")
        print(interpret(fa_result))
        
    
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc3.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()

