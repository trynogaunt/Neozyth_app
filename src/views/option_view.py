from src.views.base_view import BaseView
import tkinter as tk

class OptionView(BaseView):
    def __init__(self, master=None, controller=None,):
        super().__init__(master)
        self.master = master
        self.controller = controller
        self.app_name = self.controller.option_service.get('Name')
        self.messagebox_type = ['error', 'info', 'warning']
        print("OptionsView: __init__ method called")

    def create_widgets(self):
        # Create widgets for the options view here
        self.label = tk.Label(self, text=f"Options for {self.app_name}")
        self.label.pack(pady=20)

    def show(self):
        # Call the base class method to pack the frame
        print("OptionsView: show method called")
        super().show()