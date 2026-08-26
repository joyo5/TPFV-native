# Ecran de connexion

from database import verifier_connexion
import tkinter as tk
from tkinter import ttk, messagebox

class Connexion(tk.Frame):
    def __init__(self, parent, controleur):
        super().__init__(parent, bg="white")
        self.controleur = controleur
        
        tk.Label(self, text="TPFV", font=("Arial", 24), bg="white").pack(pady=20)
        
        tk.Label(self, text="Veuillez vous identifier", font=("Arial", 24), bg="white").pack(pady=20)
        
        tk.Label(self, text="Votre rôle", font=("Arial", 14), bg="white").pack(pady=10)
        
        options = ["Accueil / Pharmacie", "Médecin / Paramed", "Admin"]
        self.combobox = ttk.Combobox(self, values=options, state="readonly")
        self.combobox.set(options[0])
        self.combobox.pack(pady=10)
        
        tk.Label(self, text="Mot de passe", font=("Arial", 14), bg="white").pack(pady=10)
        
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack(pady=10)
        
        tk.Button(self, text="Accéder", command=self._valider).pack(pady=20)
        
    
    def _valider(self):
        role = self.combobox.get()
        password = self.password_entry.get()
        
        if verifier_connexion(role, password):
            self.controleur.role = role
            self.controleur.password = password
            self.controleur.afficher_page("Principale")
            
        else:
            messagebox.showerror("Erreur", "Rôle ou mot de passe incorrect.")
