import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from src.views.base_view import BaseView
from src.controllers.character_controller import CharacterController
from src.models.character_model import CharacterModel
import os
import shutil

class CharacterView(BaseView):
    PICTURE_DIRECTORY = os.path.join(os.path.dirname(__file__), "..", "datas", "pictures")
    def __init__(self, master=None, controller=None):
        super().__init__(master, controller)

        self.character_list = []
        self.controller = CharacterController()
        self.create_widgets()
        print("CharacterView: __init__ method called")
    
    def create_widgets(self):
        self.frame = ttk.Frame(self)
        self.frame.pack(fill=tk.BOTH, expand=True)
    
        # Create a Listbox to display the character list
        self.character_listbox = tk.Listbox(self.frame)
        self.character_listbox.pack(expand=True, fill=tk.BOTH)
        self.character_list = self.controller.get_all()
        for character in self.character_list:
            self.character_listbox.insert(tk.END, f"{character.full_name}")
        if not self.character_listbox.size():   
            self.character_listbox.insert(tk.END, "No characters found.")
        
        # Bind double-click event to open character details
        self.character_listbox.bind("<Double-Button-1>", lambda event: self.open_character_details())
        self.character_add_button = tk.Button(self.frame, text="Add Character", command=lambda:self.add_character())
        self.character_add_button.pack(pady=10)
    
    def add_character(self):
        print("Adding character...")
        # Create a new window for adding a character
        self.character_add_window = tk.Toplevel(self)
        self.character_add_window.title("Add Character")
        self.character_add_window.geometry("400x300")
        
        # Create labels and entry fields for character details
        tk.Label(self.character_add_window, text="First Name:").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(self.character_add_window, text="Last Name:").grid(row=1, column=0, padx=10, pady=5)
        tk.Label(self.character_add_window, text="Age:").grid(row=2, column=0, padx=10, pady=5)
        tk.Label(self.character_add_window, text="Lineage:").grid(row=3, column=0, padx=10, pady=5)
        tk.Label(self.character_add_window, text="Job:").grid(row=4, column=0, padx=10, pady=5)
        
        self.first_name_entry = tk.Entry(self.character_add_window)
        self.first_name_entry.grid(row=0, column=1, padx=10, pady=5)
        
        self.last_name_entry = tk.Entry(self.character_add_window)
        self.last_name_entry.grid(row=1, column=1, padx=10, pady=5)
        
        self.age_entry = tk.Entry(self.character_add_window)
        self.age_entry.grid(row=2, column=1, padx=10, pady=5)
        
        self.lineage_entry = tk.Entry(self.character_add_window)
        self.lineage_entry.grid(row=3, column=1, padx=10, pady=5)
        
        self.job_entry = tk.Entry(self.character_add_window)
        self.job_entry.grid(row=4, column=1, padx=10, pady=5)

        
        

        
        # Create buttons for saving and canceling the addition
        self.save_button = tk.Button(self.character_add_window, text="Save", command=lambda:self.save_character())
        self.save_button.grid(row=5, columnspan=2,pady=(20))
        
    def open_character_details(self):
        print("Opening character details...")
        character_index = self.character_listbox.curselection()[0]
        self.character = self.character_list[character_index]
        
        # Create a new window for character details
        self.character_detail_window = tk.Toplevel(self)
        self.character_detail_window.title(f"Character Details - {self.character.full_name}")
        self.character_detail_window.geometry("400x300")
        self.character_detail_frame = ttk.Frame(self.character_detail_window)
        self.character_detail_frame.pack(fill=tk.BOTH, expand=True)
        
        
        # Create labels fields for character details
        tk.Label(self.character_detail_frame, text="First Name:", justify="left").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        tk.Label(self.character_detail_frame, text="Last Name:", justify="left").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        tk.Label(self.character_detail_frame, text="Age:", justify="left").grid(row=2, column=0, padx=10, pady=5 , sticky="w")
        tk.Label(self.character_detail_frame, text="Lineage:", justify="left").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        tk.Label(self.character_detail_frame, text="Job:", justify="left").grid(row=4, column=0, padx=10, pady=5, sticky="w")
        tk.Label(self.character_detail_frame, text="Image:", justify="left").grid(row=5, column=0, padx=10, pady=5, sticky="w")
        
        # Create entry fields for character details
        self.character_detail_firstname_entry = tk.Entry(self.character_detail_frame)
        self.character_detail_firstname_entry.grid(row=0, column=1, padx=10, pady=5)
        self.character_detail_firstname_entry.insert(0, self.character.first_name)
        
        self.character_detail_lastname_entry = tk.Entry(self.character_detail_frame)
        self.character_detail_lastname_entry.grid(row=1, column=1, padx=10, pady=5)
        self.character_detail_lastname_entry.insert(0, self.character.last_name)
        
        self.character_detail_age_entry = tk.Entry(self.character_detail_frame)
        self.character_detail_age_entry.grid(row=2, column=1, padx=10, pady=5)
        self.character_detail_age_entry.insert(0, self.character.age)
        
        self.character_detail_lineage_entry = tk.Entry(self.character_detail_frame)
        self.character_detail_lineage_entry.grid(row=3, column=1, padx=10, pady=5)
        self.character_detail_lineage_entry.insert(0, self.character.lineage)
        
        self.character_detail_job_entry = tk.Entry(self.character_detail_frame)
        self.character_detail_job_entry.grid(row=4, column=1, padx=10, pady=5)
        self.character_detail_job_entry.insert(0, self.character.job)
        
        self.character_detail_image_entry = tk.Entry(self.character_detail_frame)
        self.character_detail_image_entry.grid(row=5, column=1, padx=10, pady=5)
        self.character_detail_image_entry.insert(0, self.character.image)

        self.character_detail_import_image_button = tk.Button(self.character_detail_frame, text="Import Image", command=lambda: self.import_image())
        self.character_detail_import_image_button.grid(row=5, column=2, padx=10, pady=5)

        

        
        # Create buttons for saving and deleting the character
        self.character_save_button = tk.Button(self.character_detail_window, text="Save Changes")
        self.character_save_button.pack(pady=10)
        self.character_delete_button = tk.Button(self.character_detail_window, text="Delete Character")
        self.character_delete_button.pack(pady=10)
        self.character_save_button.bind("<Button-1>", lambda event: self.save_character(index = character_index))
        self.character_delete_button.bind("<Button-1>", lambda event: self.delete_character())


    def import_image(self):
        file_path = filedialog.askopenfilename(title="Select an image file", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            # Assuming you want to set the selected image path to the entry field
            self.character_detail_image_entry.delete(0, tk.END)
            self.character_detail_image_entry.insert(0, file_path)

    def save_character(self, index):
        print("Saving character...")
        # Get the updated character details from the entry fields
        first_name = self.character_detail_firstname_entry.get()
        last_name = self.character_detail_lastname_entry.get()
        age = self.character_detail_age_entry.get()
        lineage = self.character_detail_lineage_entry.get()
        job = self.character_detail_job_entry.get()
        image = self.character_detail_image_entry.get()
        os.makedirs(self.PICTURE_DIRECTORY, exist_ok=True)
        # Copy the image to the PICTURE_DIRECTORY if it exists
        file_name = os.path.basename(image)
        destination = os.path.join(self.PICTURE_DIRECTORY, file_name)
        if os.path.isfile(image):
            shutil.copy(image, destination)
            image = destination
        else:
            print(f"Image file {image} does not exist.")  


        
        # Update the character object with the new details
        self.character.first_name = first_name
        self.character.last_name = last_name
        self.character.age = age
        self.character.lineage = lineage
        self.character.job = job
        self.character.image = image
        self.character.full_name = f"{self.character.first_name} {self.character.last_name}"
        
        # Save the updated character to the database
        updated_character = CharacterModel(
            id=self.character.id,
            first_name=self.character.first_name,
            last_name=self.character.last_name,
            age=self.character.age,
            lineage=self.character.lineage,
            job=self.character.job,
            image=self.character.image
        )
        self.controller.update(updated_character)
        # Update the character listbox with the new details
        self.character_listbox.delete(index)
        self.character_listbox.insert(index, f"{self.character.full_name}")
        # Close the character detail window
        self.character_detail_window.destroy()
    
    def delete_character(self):
        print("Deleting character...")

    
        
