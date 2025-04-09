import tkinter as tk
from tkinter import ttk
from src.views.base_view import BaseView
from src.views.character_view import CharacterView
from src.models.character_model import CharacterModel as Ch

# MainView class that inherits from BaseView
# This class represents the main view of the application
class MainView(BaseView):
    def __init__(self, master=None , controller = None):
        # Initialize the base class with the master and controller
        super().__init__(master)
        self.master = master
        self.controller = controller
        print("MainView: __init__ method called")

    def create_widgets(self):
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        self.character_tab = CharacterView(self.master)
        self.notebook.add(self.character_tab, text="Character")
                  
    def open_add_form(self):
        self.character_tab.pack_forget()
        self.add_frame.pack(fill=tk.BOTH, expand=True)


    def cancel_add_form(self):
        self.add_frame.pack_forget()
        self.character_tab.pack(fill=tk.BOTH, expand=True)
                 
    def show(self):
        super().show() 