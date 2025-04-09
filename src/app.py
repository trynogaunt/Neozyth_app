import tkinter as tk
import os 
import importlib
from src.menu import MenuBar

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.title("RP Manager")
        self.resizable(True, True)
        self.view = None
        self.controller = None
        self.default_view = "main"
        
        callbacks = {
            "open_options": self.show_view
        }
        self.menu_bar = MenuBar(self, callbacks)
        self.config(menu=self.menu_bar)
        
    def show_view(self, view):
        
        # Check if view is already loaded and hide + unload it
        if self.view is not None:
            self.view.hide()
            self.view = None
        
        
        for c in os.listdir('src/controllers'):
            controller_name = c.split('.')[0]
            if controller_name == f"{view}_controller" and controller_name != "__init__.py":
                # Dynamically import the controller module and class
                print(controller_name)
                controller_module = importlib.import_module(f'src.controllers.{controller_name}')
                controller_class = getattr(controller_module, f"{view.capitalize()}Controller")
                self.controller = controller_class(self)
                break
        
        for v in os.listdir('src/views'):
            view_name = v.split('.')[0]
            if view_name == f"{view}_view":
                print(view_name)
                # Dynamically import the view module and class
                view_module = importlib.import_module(f'src.views.{view_name}')
                view_class = getattr(view_module, f"{view.capitalize()}View")
                if self.controller:
                    self.view = view_class(self, controller=self.controller)
                else:
                    self.view = view_class(self)
                # Call the show method of the view to display it
                self.view.show()
                break
        

    
        
    def run(self):
        self.show_view('main')
        self.mainloop()