import NaClDSEncoder
from NaClProfile import NaClProfile
from pathlib import Path
from Profile import Profile, Post, DsuFileError, DsuProfileError
from ds_client import send, join
from ds_protocol import post_message, post_bio
while True:
    command = input()
    if 'Q' in command:
        break
    elif len(command) == 1:
        print('ERROR')
    else:
        path = command.split()[1].strip()
        p = Path(path)
        if command.split()[0].strip() == 'Q':
            break
        if command.split()[0].strip() == 'L':
            if len(command.split()) == 2:
                for o in p.iterdir():
                    print(o)
                
            elif len(command.split()) == 3:
                if command.split()[2].strip() == '-r':
                    for o in p.iterdir():
                        print(o)
                        if o.is_dir() == True:
                            for i in o.iterdir():
                                print(i)
                if command.split()[2].strip() == '-f':
                    for o in p.iterdir():
                        if o.is_file() == True:
                            print(o)
            elif '-f' in command and '-r' in command:
                for o in p.iterdir():
                    if o.is_file() == True:
                        print(o)
                    if o.is_dir() == True:
                        for i in o.iterdir():
                            print(i)
            if '-s' in command:
                file = len(command.split())
                if command.split()[2].strip() == '-r':
                    for o in p.iterdir():
                        if command.split()[file-1].strip() in str(o):
                            print(o)
                        if o.is_dir() == True:
                            for i in o.iterdir():
                                if command.split()[file-1].strip() in str(i):
                                    print(i)
                elif command.split()[2].strip() == '-f':
                    for o in p.iterdir():
                        if o.is_file() == True:
                            if command.split()[file-1].strip() in str(i):
                                print(i)
                elif len(command.split()) == 4:
                    for i in p.iterdir():
                        if command.split()[file-1].strip() in str(i):
                            print(i)
                            
            if '-e' in command:
                extension = command.split()[len(command.split())-1].strip()
                if len(command.split()) == 4:
                    for o in p.iterdir():
                        if o.suffix.strip('.') == extension:
                            print(o)
                elif '-f' in command:
                    for o in p.iterdir():
                        if o.is_file() == True:
                            if o.suffix.strip('.') == extension:
                                print(o)
                elif '-r' in command:
                    for o in p.iterdir():
                        if o.suffix.strip('.') == extension:
                            print(o)
                        if o.is_dir() == True:
                            for i in o.iterdir():
                                if i.suffix.strip('.') == extension:
                                    print(i)
        if command.split()[0].strip() == 'R':
            if p.suffix.strip('.') == 'dsu':
                if '-l' in command:
                    npr = NaClProfile()
                    npr.load_profile(ifile) #load profile
                if p.stat().st_size ==0:
                    print('EMPTY')
                else:
                    with open(p) as f:
                        thefile = f.read()
                        newfile = str(thefile).strip('\n')
                        print(newfile)
            else:
                print('ERROR')
        if command.split()[0].strip() == 'C': #send post through here and create file

            if '-n' in command:
                path = str(p) + "/" + command.split()[3].strip()
                np = Path(path)
                ifile = str(np) + '.dsu'

            elif len(command) == 3:
                ifile = str(p) + '.dsu'
            f = open(ifile, "w")
            print('Your dsu file:', ifile)
            npr = NaClProfile()
            npr.dsuserver = input('dsuserver')
            npr.username = input('username')
            npr.password = input('password')
            npr.bio = input('bio')
            print("send encryped post")
            
            npr.generate_keypair()
            pub_k = npr.pub_key() #get my own public key
            token = join(pub_k, npr.username, npr.password)#join with my public key
            ds_pubkey = token
            entry_msg = input('Enter your entry Message')
            post = Post(entry_msg)
            en_msg = npr.encrypt_entry(entry_msg, ds_pubkey) #encrypt message with ds server's public key
            a =en_msg.decode("utf-8") 
            print('Your encrypted message:', a)
            time = str(post).split(" ")[-1].strip('}')
            if len(npr.bio) == 0: #if the user doesn't enter bio
                send(time, npr.username, npr.password, pub_k, a)
            else:
                send(time, npr.username, npr.password, pub_k, a, npr.bio)

            #encrypt post
            count = 0
            while True:
                apst = input('Do you want to add a new post or add another post T/F?')
                if apst == 'T' or apst == 't':
                    count =1
                    whatpst = input('Enter your Post')
                    eepost = npr.add_post(Post(whatpst))
                    print('Your encrypted post:',eepost)
                elif apst == 'F' or apst == 'f':
                    break
                else:
                    print('try again')
                
            if count ==1:
                p_list = npr.get_posts()
                print(p_list)
                print('See decypted posts:') #decrpyt post
                for i in range(len(p_list)):
                    print(p_list[i].get_entry())
            print('profile saved. use command R to load profile')
            f.close()
            npr.save_profile(ifile) #save profile
            



        if command.split()[0].strip() == 'D':
            if p.suffix.strip('.') == 'dsu':
                print(p, 'DELETED')
                p.unlink()
            else:
                print('ERROR')
