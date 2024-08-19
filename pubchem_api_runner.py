import tkinter as tk
from tkinter import filedialog, ttk
import threading
import os
from PIL import Image, ImageTk
from pubchem_api import get_compound_info_list_with_progress, remove_duplicates

class PubChemApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PubChem Molecular Search")
        self.root.configure(bg="#9dd0f5")

        self.frame = tk.Frame(self.root, bg="#9dd0f5")
        self.frame.pack(padx=100, pady=20)

        self.filename = ""
        self.process_thread = None
        self.should_continue = threading.Event()
        self.should_continue.set()

        self.create_widgets()

    def create_widgets(self):
        # Add logo
        logo_path = "logo.png"
        if os.path.exists(logo_path):
            logo_image = Image.open(logo_path)
            logo_image = logo_image.resize((421, 154), Image.LANCZOS)
            logo_photo = ImageTk.PhotoImage(logo_image)
            logo_label = tk.Label(self.frame, image=logo_photo, bg="#9dd0f5")
            logo_label.image = logo_photo
            logo_label.grid(row=0, column=0, pady=10)

        self.browse_button = tk.Button(self.frame, text="Browse", command=self.browse_file, bg="#05263d", fg="white")
        self.browse_button.grid(row=1, column=0, pady=5, sticky="ew")

        self.file_label = tk.Label(self.frame, text="No file selected", bg="#9dd0f5", fg="black", wraplength=200)
        self.file_label.grid(row=2, column=0, pady=5)

        self.input_type_label = tk.Label(self.frame, text="Input Type:", bg="#9dd0f5", fg="black")
        self.input_type_label.grid(row=3, column=0, pady=5)

        self.input_type_var = tk.StringVar(self.root)
        self.input_type_var.set("Name")  # default value
        self.input_type_menu = ttk.Combobox(self.frame, textvariable=self.input_type_var, values=["Name", "CID", "SMILES"])
        self.input_type_menu.grid(row=4, column=0, pady=5)

        self.output_label = tk.Label(self.frame, text="Output Filename:", bg="#9dd0f5", fg="black")
        self.output_label.grid(row=5, column=0, pady=5)

        self.output_entry = tk.Entry(self.frame)
        self.output_entry.grid(row=6, column=0, pady=5)

        self.start_button = tk.Button(self.frame, text="Start Process", command=self.start_process, bg="#05263d", fg="white")
        self.start_button.grid(row=7, column=0, pady=5, sticky="ew")

        self.restart_button = tk.Button(self.frame, text="Restart Connection", command=self.restart_process, bg="#05263d", fg="white")
        self.restart_button.grid(row=8, column=0, pady=5, sticky="ew")

        self.progress_label = tk.Label(self.frame, text="Progress:", bg="#9dd0f5", fg="black")
        self.progress_label.grid(row=9, column=0, pady=5)

        self.progress_bar = ttk.Progressbar(self.frame, orient=tk.HORIZONTAL, length=200, mode="determinate")
        self.progress_bar.grid(row=10, column=0, pady=5)

        self.status_label = tk.Label(self.frame, text="Status:", bg="#9dd0f5", fg="black")
        self.status_label.grid(row=11, column=0, pady=5)

        self.status_var = tk.StringVar()
        self.status_var.set("Idle")
        self.status_value_label = tk.Label(self.frame, textvariable=self.status_var, bg="#9dd0f5", fg="black", wraplength=250, width=35, height=2)
        self.status_value_label.grid(row=12, column=0, pady=5)

    def browse_file(self):
        self.filename = filedialog.askopenfilename(title="Select a file", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
        self.file_label.config(text=f"Selected file: {os.path.basename(self.filename)}")

    def start_process(self):
        if not self.filename:
            return

        output_filename = self.output_entry.get()
        if not output_filename:
            self.status_var.set("Please enter an output filename")
            return

        identifiers = []
        with open(self.filename, 'r', encoding='utf-8') as file:
            for line in file:
                identifiers.append(line.strip())

        input_type = self.input_type_var.get()

        self.progress_bar["value"] = 0
        self.status_var.set("Processing...")
        self.should_continue.set()

        self.process_thread = threading.Thread(target=self.process_data, args=(identifiers, input_type, output_filename))
        self.process_thread.start()

    def process_data(self, identifiers, input_type, output_filename):
        mol_cids, full_data = get_compound_info_list_with_progress(identifiers, input_type, self.progress_bar, self.root, self.status_var, self.should_continue.is_set)
        
        with open(output_filename, "w", encoding="utf-8") as f:
            for line in full_data:
                f.write(line + "\n")
        
        remove_duplicates(output_filename)
        
        if self.should_continue.is_set():
            self.status_var.set("Process completed")
        else:
            self.status_var.set("Process interrupted")

    def restart_process(self):
        if self.process_thread and self.process_thread.is_alive():
            self.should_continue.clear()
            self.process_thread.join()
            self.status_var.set("Restarting connection...")
            self.start_process()
        else:
            self.status_var.set("No active process to restart")

if __name__ == "__main__":
    root = tk.Tk()
    app = PubChemApp(root)
    
    # Configure style for Combobox
    style = ttk.Style()
    style.theme_use('default')
    style.configure('TCombobox', fieldbackground="#9dd0f5", background="#05263d")
    
    root.mainloop()