import tkinter as tk
from tkinter import messagebox
class BaseView(tk.Frame):
    def __init__(self, master=None, controller = None, **kwargs):
        super().__init__(master)
        self.master = master
        self.messagebox_type = ['error', 'info', 'warning']
        self.controller = controller

    def create_widgets(self):
        '''
        This method should be overridden in subclasses to create widgets.
        It should not be called directly from outside the class.
        Instead, subclasses should implement their own version of this method.
        For example:
        class MyView(BaseView):
            def create_widgets(self):
                self.label = tk.Label(self, text="Hello, World!")
                self.label.pack()
        '''
        pass  # This method should be overridden in subclasses

    def show(self):
        '''
        This method should be called to display the view.
        It will call the create_widgets method to create the widgets,'''
        # and then pack the frame to make it visible.
        self.create_widgets()
        self.pack(fill=tk.BOTH, expand=True)

    def hide(self):
        self.pack_forget()
    
    def open_messagebox(self, message , type):
        if type not in self.messagebox_type:
            raise ValueError(f"Invalid messagebox type: {type}. Valid types are: {self.messagebox_type}")
        
        # Display the messagebox based on the type
        if type == "error":
            messagebox.showerror("Error", message)
        elif type == "warning":
            messagebox.showwarning("Warning", message)
        else:
            messagebox.showinfo("Message", message)