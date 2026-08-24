# Classe principale

import tkinter as tk
from views.connexion import Connexion
from views.principale import Principale

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("TPFV")
        self.geometry("500x400")
        
        conteneur = tk.Frame(self)
        conteneur.pack(side="top", fill="both", expand=True)
        conteneur.grid_rowconfigure(0, weight=1)
        conteneur.grid_columnconfigure(0, weight=1)
        
        self.pages = {}
        
        for P in (Connexion, Principale):
            nom_page = P.__name__
            frame = P(parent=conteneur, controleur=self)
            self.pages[nom_page] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            
        self.afficher_page("Connexion")
        
    def afficher_page(self, nom_page: str):
        page = self.pages[nom_page]
        if hasattr(page, "actualiser"):
            page.actualiser()
        page.tkraise()