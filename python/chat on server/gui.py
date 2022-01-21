import tkinter as tk
from tkinter import ttk, filedialog, simpledialog
from user_class import User, MessageError
import ds_messenger
from ds_messenger import DirectMessenger


"""
A subclass of tk.Frame that is responsible for drawing all of the widgets
in the body portion of the root frame.
"""
class Body(tk.Frame):
    def __init__(self, root, select_callback=None):
        tk.Frame.__init__(self, root)
        self.root = root
        self._select_callback = select_callback
        self.index = 0

        # a list of the User objects available in the active DSU file
        self._users = [User]
        
        # After all initialization is complete, call the _draw method to pack the widgets
        # into the Body instance 
        self._draw()
        
    """
    Resets all UI widgets to their default state. Useful for when clearing the UI is neccessary such
    as when a new DSU file is loaded, for example.
    """
    def reset_ui(self):
        self.set_text_entry("")
        self._users = []
        for item in self.users_tree.get_children():
            self.users_tree.delete(item)
            
    """
    Update the entry_editor with the full post entry when the corresponding node in the posts_tree
    is selected.
    """
    def node_select(self, event):
        index = int(self.users_tree.selection()[0])-1 #selections are not 0-based, so subtract one.
        self.index = index
        entry = self._users[index].entry

        self.set_text_entry(entry)
    
    """
    Returns the text that is currently displayed in the entry_editor widget.
    """
    def get_text_entry(self) -> str:
        return self.entry_editor.get('1.0', 'end').rstrip()

    """
    Sets the text to be displayed in the entry_editor widget.
    NOTE: This method is useful for clearing the widget, just pass an empty string.
    """
    def set_text_entry(self, text:str):
        self.entry_editor.delete('0.0', 'end') #delete all current text in the self.entry_editor widget
        self.entry_editor.insert('0.0', text)
        

    def set_text_box(self, text:str):
        self.text_box.delete('0.0', 'end')     #delete all current text in the self.text_box widget
        self.text_box.insert('0.0', text)
        

    def get_text_box(self) -> str:
        return self.text_box.get('1.0', 'end').rstrip()
    
    
    """
    Populates the self._posts attribute with posts from the active DSU file.
    """
    def set_users(self, users:list):
        self._users = users
        count = 0
        for user in self._users:
            count +=1
            self._insert_user_tree(count, user)  #insert the username into the tree when read all or read new

        

    """
    Inserts a single post to the post_tree widget.
    """
    def insert_user(self, user: User):
        self._users.append(user)
        self._insert_user_tree(len(self._users), user) #insert each username into the tree

   

    """
    Inserts a post entry into the posts_tree widget.
    """
    def _insert_user_tree(self, id, user: User):
        username = user.username
        # Since we don't have a title, we will use the first 24 characters of a
        # post entry as the identifier in the post_tree widget.

        if len(username) > 25:
            username = username[:24] + "..."
        self.users_tree.insert('', id, id, text=username)

                
    
    """
    Call only once upon initialization to add widgets to the frame
    """
    def _draw(self):
        users_frame = tk.Frame(master=self, width=250)
        users_frame.pack(fill=tk.BOTH, side=tk.LEFT)
        self.users_tree = ttk.Treeview(users_frame)
        self.users_tree.bind("<<TreeviewSelect>>", self.node_select)
        self.users_tree.pack(fill=tk.BOTH, side=tk.TOP, expand=True, padx=5, pady=5)
        
        entry_frame = tk.Frame(master=self, bg="")
        entry_frame.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

        text_frame = tk.Frame(master = entry_frame, bg="green")
        text_frame.pack(fill=tk.BOTH, side=tk.BOTTOM, expand = True)
        
        editor_frame = tk.Frame(master=entry_frame, bg="red")
        editor_frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
        
        scroll_frame = tk.Frame(master=entry_frame, bg="blue", width=10)
        scroll_frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=False)

        
        self.text_box = tk.Text(text_frame, height = 9, width = 0)
        self.text_box.pack(fill=tk.BOTH, side=tk.BOTTOM, expand=True, padx=0, pady=0)



        self.entry_editor = tk.Text(editor_frame, width=0)
        self.entry_editor.pack(fill=tk.BOTH, side=tk.TOP, expand=True, padx=0, pady=0)

        entry_editor_scrollbar = tk.Scrollbar(master=scroll_frame, command=self.users_tree.yview)
        self.users_tree['yscrollcommand'] = entry_editor_scrollbar.set
        entry_editor_scrollbar.pack(fill=tk.Y, side=tk.RIGHT, expand=False, padx=0, pady=0)
        """
A subclass of tk.Frame that is responsible for drawing all of the widgets
in the footer portion of the root frame.
"""
class Footer(tk.Frame):
    def __init__(self, root, send_callback=None, adduser_callback = None,refuser_callback = None):
        tk.Frame.__init__(self, root)
        self.root = root
        self._send_callback = send_callback
        self._adduser_callback = adduser_callback
        self._refuser_callback = refuser_callback
        
        
        # After all initialization is complete, call the _draw method to pack the widgets
        # into the Footer instance 
        self._draw()
    
    """
    Calls the callback function specified in the online_callback class attribute, if
    available, when the chk_button widget has been clicked.
    """
    def online_click(self):
        if self._online_callback is not None:
            self._online_callback(self.is_online.get())
        

    """
    Calls the callback function specified in the save_callback class attribute, if
    available, when the save_button has been clicked.
    """
    def send_click(self):
        if self._send_callback is not None:
            self._send_callback()


    def add_click(self):
        if self._adduser_callback is not None:
            self._adduser_callback()

    def ref_click(self):
        if self._refuser_callback is not None:
            self._refuser_callback()

    """
    Updates the text that is displayed in the footer_label widget
    """
    def set_status(self, message):
        self.footer_label.configure(text=message)
    
    """
    Call only once upon initialization to add widgets to the frame
    """
    def _draw(self):
        send_button = tk.Button(master=self, text="Send", width=10)
        send_button.configure(command=self.send_click)
        send_button.pack(fill=tk.BOTH, side=tk.RIGHT, padx=5, pady=5)
        
        add_button = tk.Button(master=self, text="Add User", width=10)
        add_button.configure(command=self.add_click)
        add_button.pack(fill=tk.BOTH, side=tk.LEFT, padx=70, pady=5)

        ref_button = tk.Button(master=self, text="Refesh", width=10)
        ref_button.configure(command=self.ref_click)
        ref_button.pack(fill=tk.BOTH, side=tk.LEFT, padx=70, pady=5)


"""
A subclass of tk.Frame that is responsible for drawing all of the widgets
in the main portion of the root frame. Also manages all method calls for
the NaClProfile class.
"""
class MainApp(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.root = root
        self._is_online = False
        self._profile_filename = None
        self.nkey = None
        self.nbio = None
        self._users = [User]

        try:
            self.dm = DirectMessenger('168.235.86.101', "Invincible Coding Squad", 'We are very lazy')
            self.dm.cnct2server()
            reall = self.dm.retrieve_all()
            renew = self.dm.retrieve_new()
            if type(reall) == None or type(renew) == None:
                reall = [] 
                renew = []
            
            direct = reall + renew
            self.listusers = []
            for item in direct:
                person = User(entry = item.message, username = item.recipient, timestamp = item.timestamp)
                self.listusers.append(person)
        except Exception as ex:
            raise MessageError(ex)
        # After all initialization is complete, call the _draw method to pack the widgets
        # into the root frame
        self._draw()

    
    """
    Closes the program when the 'Close' menu item is clicked.
    """
    def close(self):
        self.root.destroy()

    '''
    send message to the recipient being selected
    '''
    def send_msg(self):

        msg = self.body.get_text_box()
        print(msg)
        #should be the user being clicked on the post_tree
        recipient = self.listusers[self.body.index].username
        self.dm.send(msg,recipient)
        self.body.set_text_box('sent!')

    '''
    add a new user to the tree widget with user input
    '''
    def add_user(self):
        user_name = tk.simpledialog.askstring('Add a user', 'User Name:')
        self._send_user = User(username=user_name, entry = '')
        self._users.append(self._send_user)
        self.body.insert_user(self._send_user)

    def refresh_click(self):
        retrieve_again = self.dm.retrieve_new()
        for i in retrieve_again:
            user1 = User(i.message, i.recipient, i.timestamp)
            self.body.insert_user(user1)
        

    
    """
    Call only once, upon initialization to add widgets to root frame
    """
    def _draw(self):
        # Build a menu and add it to the root frame.
        menu_bar = tk.Menu(self.root)
 

        # The Body and Footer classes must be initialized and packed into the root window.
        self.body = Body(self.root, self.dm)
        self.body.set_users(self.listusers)
        self.body.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
        
  
        self.footer = Footer(self.root, send_callback=self.send_msg, adduser_callback = self.add_user, refuser_callback = self.refresh_click)
        self.footer.pack(fill=tk.BOTH, side=tk.BOTTOM)

if __name__ == "__main__":
    # All Tkinter programs start with a root window. We will name ours 'main'.
    main = tk.Tk()

    # 'title' assigns a text value to the Title Bar area of a window.
    main.title("ICS 32 Distributed Social Demo")

    # This is just an arbitrary starting point. You can change the value around to see how
    # the starting size of the window changes. I just thought this looked good for our UI.
    main.geometry("720x480")

    # adding this option removes some legacy behavior with menus that modern OSes don't support. 
    # If you're curious, feel free to comment out and see how the menu changes.
    main.option_add('*tearOff', False)

    # Initialize the MainApp class, which is the starting point for the widgets used in the program.
    # All of the classes that we use, subclass Tk.Frame, since our root frame is main, we initialize 
    # the class with it.
    MainApp(main)
    

    # When update is called, we finalize the states of all widgets that have been configured within the root frame.
    # Here, Update ensures that we get an accurate width and height reading based on the types of widgets
    # we have used.
    # minsize prevents the root window from resizing too small. Feel free to comment it out and see how
    # the resizing behavior of the window changes.
    main.update()
    main.minsize(main.winfo_width(), main.winfo_height())
    # And finally, start up the event loop for the program (more on this in lecture).
    main.mainloop()


