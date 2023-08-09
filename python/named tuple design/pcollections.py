# Submitter: ecsonh(Hsu, Ecson)
# Partner  : wanghs(Wang, Henry)
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming
import re, traceback, keyword

def pnamedtuple(type_name, field_names, mutable = False,  defaults =  {}):
    def show_listing(s):
        for ln_number, text_of_ln in enumerate(s.split('\n'),1):     
            print(f' {ln_number: >3} {text_of_ln.rstrip()}')

    # put your code here
    # bind class_definition (used below) to the string constructed for the class
    def unique(iterable):
        iterated = set()
        for i in iterable:
            if i not in iterated:
                iterated.add(i)
                yield i
    
    def legal_test(inputstring):
        if not isinstance(inputstring, str):
            return False
        elif not re.match(r'^[a-zA-Z][\w]*$', inputstring):
            return False
        elif inputstring in keyword.kwlist:
            return False
        return True
    
    if not legal_test(type_name):
        raise SyntaxError('Type name not legal')
    
    
    if isinstance(field_names, str):
        field_names = field_names.replace(',', ' ')
        field_names = field_names.split()
        
    if not isinstance(field_names, list):
        raise SyntaxError('Not List')
    
    for name in field_names:
        if not legal_test(name):
            raise SyntaxError('Field Name not Legal')
    
    field_names = [name for name in unique(field_names)]
    
    if len(defaults) != 0:
        for i in defaults:
            if i not in field_names:
                raise SyntaxError('Name not in field name')  
            
    def gen_init(field_names):
        res = f" def __init__(self, {', '.join(field_names)}):\n"
        for name in field_names:
            new_line = f"self.{name} = {name}"
            res += f"         {new_line}\n"  
        return res
    
    def gen_repr(type_name, field_names):
        final = ' def __repr__(self):\n'
        final += f"         return f'{type_name}("
        
        for name in field_names:
            new_line = f'{name}={{self.{name}}},'
            final += new_line
        final = final.rstrip(',')
        final += ")'\n"
        return final
    
    def gen_get(field_names):
        res = ''
        for i in field_names:
            res += f' def get_{i}(self):\n'
            res += f'         return self.{i}\n' 
            res +='\n    '
        return res
        

        
    class_definition = f'''\
class {type_name}:
     _fields = {field_names}
     _mutable = {mutable}
    {gen_init(field_names)}
    {gen_repr(type_name, field_names)}
    {gen_get(field_names)}
     def __getitem__(self,index):
        if isinstance(index, int) and index >= 0 and index < len(self._fields):
            return eval('self.get_' + self._fields[index] + '()')
        if isinstance(index, str) and index in self._fields:
            return self.__dict__[index]
        else:
            raise IndexError
     def __eq__(self,right):
        if type(right) is {type_name}:
            for i in self._fields:
                if i in right._fields and self.__getitem__(i) != right.__getitem__(i):
                    return False
        else:
            return False
        return True
        
     def _asdict(self):
        d = dict()
        for i in self._fields:
            d[i] = self.__getitem__(i)
        return d
    
     def _make(iterable):
        return {type_name}(*iterable)
        
     def _replace(self, **kargs):
        for karg in kargs:
            if karg not in self._fields:
                raise TypeError('Name not field_names')
        if self._mutable:
            for k,v in kargs.items():
                self.__dict__[k] = v
            return None
        else:
            for key,value in self.__dict__.items():
                if key not in kargs:
                    kargs[key] = value
                    
            return {type_name}(**kargs)
                
     def __setattr__(self, name, value):
        if self._mutable or name not in self.__dict__:
            self.__dict__[name] = value
        elif self._mutable == False:
            raise AttributeError('Mutable is false, names cannot be changed')
        
    '''



    # Debugging aid: uncomment show_listing here so always display source code
    # show_listing(class_definition)
    
    # Execute class_definition's str inside name_space; followed by binding the
    #   attribute source_code to the class_definition; after the try/except then
    #   return the created class object; if any syntax errors occur, show the
    #   listing of the class and also show the error in the except clause
    name_space = dict( __name__ = f'pnamedtuple_{type_name}' )              
    try:
        exec(class_definition,name_space)
        name_space[type_name].source_code = class_definition
    except (TypeError,SyntaxError):                  
        show_listing(class_definition)
        traceback.print_exc()
    return name_space[type_name]


    
if __name__ == '__main__':

    # Test simple pnamedtuple below in script: Point=pnamedtuple('Point','x,y')

    #driver tests
    import driver  
    driver.default_file_name = 'bscp3S21.txt'
#     driver.default_show_exception_message= True
#     driver.default_show_traceback= True
    driver.driver()
