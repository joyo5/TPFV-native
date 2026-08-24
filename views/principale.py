# Application principale

import tkinter as tk

class Principale(tk.Frame):
    def __init__(self, parent, controleur):
        super().__init__(parent)
        self.controleur = controleur
        
        label = tk.Label(self, text="Bienvenue dans l'application TPFV", font=("Arial", 18))
        label.pack(pady=20)
        
        self.label_role = tk.Label(self, text="", font=("Arial", 14))
        self.label_role.pack(pady=10)
        
        bouton_nouveau_patient = tk.Button(
            self, 
            text="Créer un nouveau patient", 
            command=lambda: self.controleur.afficher_page("NouveauPatient")
        )
        bouton_nouveau_patient.pack(pady=10)
        
        bouton_retour = tk.Button(
            self, 
            text="Retour à la connexion", 
            command=lambda: self.controleur.afficher_page("Connexion")
        )
        bouton_retour.pack(pady=20)
        
    def actualiser(self):
        self.label_role.config(text=f"Rôle sélectionné: {self.controleur.role}")