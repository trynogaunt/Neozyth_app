import tkinter as tk

class MenuBar(tk.Menu):
    def __init__(self, master=None, callbacks=None):
        super().__init__(master)
        self.master = master
        self.callbacks = callbacks if callbacks else {}
        self.create_menu()
    
    def create_menu(self):
        self._add_menu_item(self,"Option", "open_options", "option")
    
    def _add_menu_item(self, menu, label, command , arg=None):
        """Add a menu item to the menu bar.
        """
        if command:
            if arg:
                menu.add_command(label=label, command=lambda: self._execute_callback(command, arg))
            else:
                menu.add_command(label=label, command=lambda: self._execute_callback(command))
        else:
            menu.add_command(label=label, state=tk.DISABLED)
        
    def _execute_callback(self, command , arg=None):
        '''
        Execute the callback associated with the command.
        If the command is not found, do nothing.
        '''
        if command in self.callbacks and self.callbacks[command]:
            if arg is None:
                self.callbacks[command]()
            else:
                self.callbacks[command](arg)  