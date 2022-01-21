import json, socket, time
from collections import namedtuple
import user_class
from user_class import MessageError
 

class DirectMessage:
  def __init__(self):
    self.recipient = None #Recipient here is whoever is sending the message
    self.message = None
    self.timestamp = None


class DirectMessenger():
    def __init__(self, dsuserver='168.235.86.101', username=None, password=None):
        #initialize all necessary variables
        self.token = None #assigned later
        self.dsuserver = dsuserver
        self.username = username
        self.password = password
        self.port = 3021
	
    def send(self, message:str, recipient:str) -> bool:
        '''Sends a direct message to a specified recipient.'''
        #Here Recipient should be the reciever of the message
        try:
            sendit = directmessage(self.token, 'send', message, recipient)
            sent_msg = self.make_file(sendit)
            print(sent_msg.message)
            if sent_msg.type == 'ok':
                return True
            else:
                return False
            # returns true if message successfully sent, false if send failed.
        except Exception as ex: #in case there are errors with the networks
            raise MessageError(ex)

		
    def retrieve_new(self) -> list:
        """Returns a list of DirectMessage objects containing all messages."""
        try:
            new_msg = directmessage(self.token, 'new')
            new_var = self.make_file(new_msg)
            new_msglist = []
            for message in new_var.message:
                #create a DirectMessage object and collect messages
                dm = DirectMessage()
                dm.recipient = message['from']
                dm.message = message['message']
                dm.timestamp = message['timestamp']
                #add the messages to a new list that will be returned
                new_msglist.append(dm)
            return(new_msglist)
        except Exception as ex:
            raise MessageError(ex)


    def retrieve_all(self) -> list:
        """Returns a list of DirectMessage objects containing all messages."""
        try:
            all_msg = directmessage(self.token, 'all')
            all_var = self.make_file(all_msg)
            all_msglist = []
            
            for message in all_var.message:
                #create a DirectMessage object and collect messages
                dm = DirectMessage()
                dm.recipient = message['from']
                dm.message = message['message']
                dm.timestamp = message['timestamp']
                #add the messages to a new list that will be returned
                all_msglist.append(dm)
            return(all_msglist)

        except Exception as ex:
            raise MessageError(ex)


    def make_file(self, msg):
        '''
        This function was used to send a file to the server made of the json string and then
        receive a message back from the server and extract the message/messages.
        '''
        try:
            self.sendfile.write(msg + '\r\n')
            self.sendfile.flush()
            srv_msg = self.recv.readline()
            new_var = extract_json(srv_msg)
            return new_var
        except Exception as ex:
            raise MessageError(ex)


    def cnct2server(self):
        '''
        This function initially connects the user to the server and returns a usertoken that
        gets assigned to the DirectMessenger object via self.token.
        '''
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:

            try:
                #connect to the server and collect a token
                client.connect((self.dsuserver, self.port))

                self.sendfile = client.makefile('w')
                self.recv = client.makefile('r')
                joined_msg = join(self.username, self.password)
                somevar = self.make_file(joined_msg)
                print(somevar.message)
                self.token = somevar.token   #token return from the server
          
            except json.JSONDecodeError:
                print("Json cannot be decoded.") # handle error later***
    

def join(username:str, password:str) -> str:
    """Used to initially connect the user to the server."""
    try:
        tempvar = None
        tempvar = '{"join": {"username":"'+username+'", "password":"'+password+'", "token":""}}'
        return tempvar
    except TypeError as ex:
        raise MessageError(ex)


def error():
    tempvar = '{"response": {"type": "error", "message": "An error message will be contained here."}}'


def directmessage(user_token:str, request:str=None, message:str=None, recipient:str=None, stamp:str=str(time.time())):
    tempvar = None
    try:
        if request not in ['new', 'all']:
            tempvar = '{"token":"'+user_token+'", "directmessage": {"entry": "'+message+'", "recipient":"'+recipient+'", "timestamp": "'+stamp+'"}}'
        elif request in ['new', 'all']:
            tempvar = '{"token":"'+user_token+'", "directmessage": "'+request+'"}'
        return tempvar

    except TypeError as ex:
        raise MessageError(ex)


# Create a namedtuple to hold the values we expect to retrieve from json messages.
DataTuple = namedtuple('DataTuple', ['type','message', 'token'])

def extract_json(json_msg:str) -> DataTuple:
    '''
    Call the json.loads function on a json string and convert it to a namedtuple.
    '''
    typ = None
    msg = None
    token = None
    try:
        json_obj = json.loads(json_msg)
        typ = json_obj['response']['type']
        if "message" in json_obj['response'].keys():
          msg = json_obj['response']['message']
          if "token" in json_obj['response'].keys():
            token = json_obj['response']['token']
          return DataTuple(typ, msg, token)
        elif "messages" in json_obj['response'].keys():
          msg = json_obj['response']['messages']
          return DataTuple(typ, msg, token)
    except json.JSONDecodeError:
        print("Json cannot be decoded.")
    


