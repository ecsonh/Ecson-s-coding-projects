import socket
from Profile import Profile, Post, DsuFileError, DsuProfileError
from ds_protocol import post_message, post_bio
from NaClProfile import NaClProfile
import json

PORT = 2021
HOST = '168.235.86.101'
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
def join(pubkey: str,username:str, password:str) -> str:
    

    join_msg = '{"join": {"username": "'+ username +'","password": "' + password +'","token":"' + pubkey+'"}}'
    send = client.makefile('w')
    recv = client.makefile('r')

    send.write(join_msg + '\r\n')
    send.flush()

    resp = recv.readline()
    print(resp)
    try:
        obj = json.loads(resp)
        if 'ok' == obj['response']['type']:
            token = obj['response']['token']
        elif 'error'== obj['response']['type']:
            print(error)
            return ErrorResponse(obj['response']['type'],resp)
    except json.JSONDecodeError:
        print("Json cannot be decoded.")
    return token

def send(time: str,username:str, password:str, token:int, msg, bio:str=None):

    while True:
        if_bio = input('post "bio"? or y/n')
        if if_bio == 'y' or if_bio == 'Y':
            sm = post_bio(token, msg, time)
            send = client.makefile('w')
            recv = client.makefile('r')
            send.write(str(sm) + '\r\n')
            send.flush()
            resp = recv.readline()
            print(resp)
            try:
                obj = json.loads(resp)
                if 'ok' == obj['response']['type']:
                    print("bio created succesfully")
                elif 'error'== obj['response']['type']:
                    print('error')
                    return ErrorResponse(obj['response']['type'],resp)
            except json.JSONDecodeError:
                print("Json cannot be decoded.")
            break
        elif if_bio == 'n' or if_bio == 'N':
            break
        else:
            print('Error enter again')
    while True:
        if_post = input('post "decrypted message"? y/n')
        if if_post == 'y' or if_post == 'Y':
            po = post_message(token, msg, time)
            send = client.makefile('w')
            recv = client.makefile('r')

            send.write(po + '\r\n')
            send.flush()
            resp = recv.readline()
            print(resp)
            try:
                obj = json.loads(resp)
                if 'ok' == obj['response']['type']:
                    print("message posted successfully")
                elif 'error'== obj['response']['type']:
                    print('error')
                    return ErrorResponse(obj['response']['type'],resp)
            except json.JSONDecodeError:
                print("Json cannot be decoded.")
            break
        elif if_post == 'n' or if_post == 'N':
            break
        else:
            print('Error, enter again')

    

