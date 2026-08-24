import tkinter as tk

class Principale(tk.Frame):
    def __init__(self, parent, controleur):
        super().__init__(parent)
        self.controleur = controleur
        
        label = tk.Label(self, text="Bienvenue dans l'application TPFV", font=("Arial", 18))
        label.pack(pady=20)
        
        self.label_role = tk.Label(self, text="", font=("Arial", 14))
        self.label_role.pack(pady=10)
        
        self.label_password = tk.Label(self, text="", font=("Arial", 14))
        self.label_password.pack(pady=10)
        
        bouton_retour = tk.Button(
            self, 
            text="Retour à la connexion", 
            command=lambda: self.controleur.afficher_page("Connexion")
        )
        bouton_retour.pack(pady=20)
        
    def actualiser(self):

        self.label_role.config(text=f"Rôle sélectionné: {self.controleur.role}")
        self.label_password.config(text=f"Mot de passe: {self.controleur.password}")