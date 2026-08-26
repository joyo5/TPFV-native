import sqlite3

def connexion():
    conn = sqlite3.connect('clinique.db')
    return conn

def verifier_connexion(role, mot_de_passe):
    conn = connexion()
    cursor = conn.cursor()
    
    mapping_role = {
        'Accueil / Pharmacie': 'agent',
        'Médecin / Paramed': 'support',
        'Admin': 'admin'
    }
    
    role_db = mapping_role[role]
    cursor.execute("SELECT * FROM utilisateurs WHERE role = ? AND mot_de_passe = ?", (role_db, mot_de_passe))
    utilisateur = cursor.fetchone()
    conn.close()
    
    return utilisateur is not None

def generer_code_patient(date_entree, cursor):
    date_split = date_entree.split('-')
    date = date_split[2] + date_split[1] + date_split[0]

    cursor.execute(
        "SELECT code_patient FROM Patients WHERE code_patient LIKE ? ORDER BY code_patient DESC LIMIT 1",
        (date + '%',)
    )
    dernier = cursor.fetchone()

    if dernier:
        dernier_num = int(dernier[0][-3:])
    else:
        dernier_num = 0

    nouveau_num = dernier_num + 1
    code_patient = date + str(nouveau_num).zfill(3)

    return code_patient

def ajouter_patient(donnees):
    conn = connexion()
    cursor = conn.cursor()

    date_entree = donnees.get("premiere_consultation") or "0000-00-00"
    code_patient = generer_code_patient(date_entree, cursor)

    cursor.execute("""
        INSERT INTO Patients (
            code_patient, nom_complet, date_entree, date_visite, date_naissance,
            sexe, telephone, allergies, maladies_chroniques, chirurgies,
            antecedents_familiaux, habitudes_toxiques, traitements_en_cours,
            diagnostic, prochain_rdv, besoin_controle, notes
        ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
    """, (
        code_patient,
        donnees["nom_complet"],
        date_entree,
        donnees["date_visite"],
        donnees["date_naissance"],
        donnees["sexe"],
        donnees["telephone"],
        donnees["allergies"],
        donnees["maladies_chroniques"],
        donnees["chirurgies"],
        donnees["antecedents_familiaux"],
        donnees["habitudes_toxiques"],
        donnees["traitement_en_cours"],
        donnees["diagnostic"],
        donnees["prochain_rdv"],
        donnees["besoin_controle"],
        donnees["notes"],
    ))

    conn.commit()
    conn.close()
    return code_patient

    