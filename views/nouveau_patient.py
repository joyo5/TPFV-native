import tkinter as tk
from tkinter import ttk

class NouveauPatient(tk.Frame):
    def __init__(self, parent, controleur):
        super().__init__(parent)
        self.controleur = controleur

        # 1. CRÉATION D'UNE BARRE DE DÉFILEMENT (SCROLLBAR)
        canvas = tk.Canvas(self, borderwidth=0, highlightthickness=0)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True, padx=10, pady=10)
        scrollbar.pack(side="right", fill="y")

        # TITRE PRINCIPAL
        label_titre = tk.Label(scrollable_frame, text="Nouveau Dossier Patient", font=("Arial", 16, "bold"))
        label_titre.pack(pady=10)

        # 2. SECTION 1 INFORMATIONS PERSONNELLES (Grille à 2 colonnes)
        sec_perso = tk.LabelFrame(scrollable_frame, text="Informations Personnelles", font=("Arial", 11, "bold"), padx=15, pady=15)
        sec_perso.pack(fill="x", expand=True, padx=10, pady=5)

        tk.Label(sec_perso, text="Nom et Prénom").grid(row=0, column=0, sticky="w", pady=5)
        self.code_patient_entry = tk.Entry(sec_perso, width=25)
        self.code_patient_entry.grid(row=0, column=1, pady=5, padx=(0, 20))

        tk.Label(sec_perso, text="Téléphone").grid(row=0, column=2, sticky="w", pady=5)
        self.nom_complet_entry = tk.Entry(sec_perso, width=25)
        self.nom_complet_entry.grid(row=0, column=3, pady=5)

        tk.Label(sec_perso, text="Date de naissance").grid(row=1, column=0, sticky="w", pady=5)
        self.date_naissance_entry = tk.Entry(sec_perso, width=25)
        self.date_naissance_entry.grid(row=1, column=1, pady=5, padx=(0, 20))

        tk.Label(sec_perso, text="Sexe").grid(row=1, column=2, sticky="w", pady=5)
        self.sexe_entry = ttk.Combobox(sec_perso, values=["Homme", "Femme"], state="readonly", width=23)
        self.sexe_entry.grid(row=1, column=3, pady=5)

        tk.Label(sec_perso, text="1ère consultation").grid(row=2, column=0, sticky="w", pady=5)
        self.telephone_entry = tk.Entry(sec_perso, width=25)
        self.telephone_entry.grid(row=2, column=1, pady=5, padx=(0, 20))

        tk.Label(sec_perso, text="Date de visite").grid(row=2, column=2, sticky="w", pady=5)
        self.contact_urgence_entry = tk.Entry(sec_perso, width=25)
        self.contact_urgence_entry.grid(row=2, column=3, pady=5)

        # 3. SECTION 2 ANTECEDENTS MEDICAUX
        sec_medical = tk.LabelFrame(scrollable_frame, text="ANTECEDENTS", font=("Arial", 11, "bold"), padx=15, pady=15)
        sec_medical.pack(fill="x", expand=True, padx=10, pady=5)

        tk.Label(sec_medical, text="Allergies connues").grid(row=0, column=0, sticky="w", pady=5)
        self.allergies_entry = tk.Entry(sec_medical, width=25)
        self.allergies_entry.grid(row=0, column=1, pady=5, padx=(0, 20))

        tk.Label(sec_medical, text="Antécedents médicaux").grid(row=0, column=2, sticky="w", pady=5)
        self.maladies_chroniques_entry = tk.Entry(sec_medical, width=25)
        self.maladies_chroniques_entry.grid(row=0, column=3, pady=5)

        tk.Label(sec_medical, text="Antécedents chirurgicaux").grid(row=1, column=0, sticky="w", pady=5)
        self.chirurgies_entry = tk.Entry(sec_medical, width=25)
        self.chirurgies_entry.grid(row=1, column=1, pady=5, padx=(0, 20))

        tk.Label(sec_medical, text="Antécedents familiaux").grid(row=1, column=2, sticky="w", pady=5)
        self.traitement_en_cours_entry = tk.Entry(sec_medical, width=25)
        self.traitement_en_cours_entry.grid(row=1, column=3, pady=5)
        
        tk.Label(sec_medical, text="Habitudes toxiques").grid(row=2, column=0, sticky="w", pady=5)
        self.habitudes_toxiques_entry = tk.Entry(sec_medical, width=25)
        self.habitudes_toxiques_entry.grid(row=2, column=1, pady=5, padx=(0, 20))
        
        tk.Label(sec_medical, text="Traitement en cours").grid(row=2, column=2, sticky="w", pady=5)
        self.traitement_en_cours_entry = tk.Entry(sec_medical, width=25)
        self.traitement_en_cours_entry.grid(row=2, column=3, pady=5)
        
        # SUIVI & VITAUX
        sec_suivi = tk.LabelFrame(scrollable_frame, text="Suivi & Signes Vitaux", font=("Arial", 11, "bold"), padx=15, pady=15)
        sec_suivi.pack(fill="x", expand=True, padx=10, pady=5)
        
        tk.Label(sec_suivi, text="Temp").grid(row=0, column=0, sticky="w", pady=5)
        self.temp_entry = tk.Entry(sec_suivi, width=25)
        self.temp_entry.grid(row=1, column=0, pady=5, padx=(0, 20))
        
        tk.Label(sec_suivi, text="Poids").grid(row=0, column=1, sticky="w", pady=5)
        self.poids_entry = tk.Entry(sec_suivi, width=25)
        self.poids_entry.grid(row=1, column=1, pady=5, padx=(0, 20))
        
        tk.Label(sec_suivi, text="Pouls").grid(row=0, column=2, sticky="w", pady=5)
        self.pouls_entry = tk.Entry(sec_suivi, width=25)
        self.pouls_entry.grid(row=1, column=2, pady=5, padx=(0, 20))
        
        tk.Label(sec_suivi, text="Sys").grid(row=0, column=3, sticky="w", pady=5)
        self.sys_entry = tk.Entry(sec_suivi, width=25)
        self.sys_entry.grid(row=1, column=3, pady=5, padx=(0, 20))
        
        tk.Label(sec_suivi, text="Dia").grid(row=0, column=4, sticky="w", pady=5)
        self.dia_entry = tk.Entry(sec_suivi, width=25)
        self.dia_entry.grid(row=1, column=4, pady=5, padx=(0, 20))
        
        tk.Label(sec_suivi, text="Sat O2").grid(row=0, column=5, sticky="w", pady=5)
        self.sat_o2_entry = tk.Entry(sec_suivi, width=25)
        self.sat_o2_entry.grid(row=1, column=5, pady=5, padx=(0, 20))
        
        tk.Label(sec_suivi, text="Prescription").grid(row=2, column=0, sticky="w", pady=5)
        self.prescription_entry = tk.Entry(sec_suivi, width=25)
        self.prescription_entry.grid(row=3, column=0, pady=5, padx=(0, 20))
        
        tk.Label(sec_suivi, text="Diagnostic / avis médical").grid(row=4, column=0, sticky="w", pady=5)
        self.diagnostic_entry = tk.Entry(sec_suivi, width=25)
        self.diagnostic_entry.grid(row=5, column=0, pady=5, padx=(0, 20))

        # 4. SECTION 3 ANALYSES MEDICALES
        sec_analyse = tk.LabelFrame(scrollable_frame, text="Analyses médicales", font=("Arial", 11, "bold"), padx=15, pady=15)
        sec_analyse.pack(fill="x", expand=True, padx=10, pady=5)
        
        tk.Label(sec_analyse, text="Sélectionner une catégorie d'analyse").grid(row=1, column=2, sticky="w", pady=5)
        self.analyse_entry = ttk.Combobox(sec_analyse, values=["Hématologie & Hémostase", "Biochimie Médicale", "Immunologie & Sérologie", "Hormonologie", "Marqueurs Tumoraux", "Bactériologie", "Parasitologie", "Analyses d'Urines", "Liquides Biologiques"], state="readonly", width=23)
        self.analyse_entry.grid(row=1, column=3, pady=5)
        
        # 4. SECTION 4 HOSPITALISATION
        sec_hospitalisation = tk.LabelFrame(scrollable_frame, text="Hospitalisation", font=("Arial", 11, "bold"), padx=15, pady=15)
        sec_hospitalisation.pack(fill="x", expand=True, padx=10, pady=5)
        
        ttk.Checkbutton(sec_hospitalisation, text="Oui", variable=tk.IntVar()).grid(row=0, column=0, sticky="w", pady=5)
        ttk.Checkbutton(sec_hospitalisation, text="Non", variable=tk.IntVar()).grid(row=0, column=1, sticky="w", pady=5)
        ttk.Checkbutton(sec_hospitalisation, text="Transfert externe", variable=tk.IntVar()).grid(row=0, column=2, sticky="w", pady=5)
        
        tk.Label(sec_hospitalisation, text="Duréé, motif ou détails d'hospitalisation...").grid(row=1, column=0, sticky="w", pady=5)
        self.service_entry = tk.Entry(sec_hospitalisation, width=25)
        self.service_entry.grid(row=1, column=1, pady=5, padx=(0, 20))
        
        
        # 4. SECTION 4 CONSULTATION ACTUELLE
        
        sec_consultation = tk.LabelFrame(scrollable_frame, text="", font=("Arial", 11, "bold"), padx=15, pady=15)
        sec_consultation.pack(fill="x", expand=True, padx=10, pady=5)
        
        tk.Label(sec_consultation, text="Contrôle Requis").grid(row=0, column=0, sticky="w", pady=5)
        self.requis_entry = ttk.Combobox(sec_consultation, values=["Oui", "Non"], state="readonly", width=23)
        self.requis_entry.grid(row=0, column=1, pady=5)

        tk.Label(sec_consultation, text="Prochain RDV").grid(row=0, column=2, sticky="w", pady=5)
        self.prochain_rdv_entry = tk.Entry(sec_consultation, width=25)
        self.prochain_rdv_entry.grid(row=0, column=3, pady=5)

        tk.Label(sec_consultation, text="Notes").grid(row=1, column=0, sticky="w", pady=5)
        self.notes_entry = tk.Entry(sec_consultation, width=25)
        self.notes_entry.grid(row=1, column=1, pady=5, padx=(0, 20))

        # 5. BOUTONS D'ACTION
        frame_boutons = tk.Frame(scrollable_frame)
        frame_boutons.pack(pady=20)

        bouton_sauvegarder = tk.Button(
            frame_boutons, text="Sauvegarder", command=self.sauvegarder_patient,
            bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), padx=15, pady=5
        )
        bouton_sauvegarder.pack(side="left", padx=10)

        bouton_retour = tk.Button(
            frame_boutons, text="Retour à l'accueil", 
            command=lambda: self.controleur.afficher_page("Principale"),
            bg="#f44336", fg="white", font=("Arial", 10, "bold"), padx=15, pady=5
        )
        bouton_retour.pack(side="left", padx=10)

    def sauvegarder_patient(self):
        # Attention pour lire une zone Text, on utilise .get("1.0", tk.END) à la place de .get()
        donnees = {
            "code": self.code_patient_entry.get(),
            "nom": self.nom_complet_entry.get(),
            "parametres": self.parametres_entry.get("1.0", tk.END).strip(),
            "notes": self.notes_entry.get("1.0", tk.END).strip()
        }
        print("Sauvegarde", donnees)