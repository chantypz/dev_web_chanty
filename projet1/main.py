# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 21:22:35 2021

@author: etudiant
"""

from flask import Flask,render_template,request,jsonify
import sqlite3
import json

app1=Flask(__name__)




def createdb():
    conn = sqlite3.connect ('base.db')
    print ("base de donnéées ouverte avec succès")
    conn.execute("CREATE TABLE IF NOT EXISTS Patient(Numero_utilisateur INTEGER, Mot_de_passe TEXT, Nom TEXT, Prenom TEXT, Age INTEGER, Adresse TEXT, Hematies INTEGER, Hemoglobine INTEGER, Hematocrite INTEGER, VGM INTEGER, CCMH INTEGER, TCMH INTEGER,RDW INTEGER,Polynucleaires_neutrophiles INTEGER,Polynucleaires_eosinophiles INTEGER,Polynucleaires_basophiles INTEGER,Lymphocytes INTEGER, Monocytes INTEGER)")
    print ("Table créée avec succès")
    conn.close()

def ajoututilisateur(Numero_utilisateur,Mot_de_passe, Nom , Prenom, Age, Adresse, Hematies, Hemoglobine, Hematocrite, VGM, CCMH , TCMH, RDW , Polynucleaires_neutrophiles,Polynucleaires_eosinophiles,Polynucleaires_basophiles,Lymphocytes,Monocytes):
    with sqlite3.connect("base.db") as con:
        cur = con.cursor()
        cur.execute(" INSERT INTO Patient (Numero_utilisateur,Mot_de_passe, Nom , Prenom, Age, Adresse, Hematies, Hemoglobine, Hematocrite, VGM, CCMH , TCMH, RDW , Polynucleaires_neutrophiles,Polynucleaires_eosinophiles,Polynucleaires_basophiles,Lymphocytes,Monocytes) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)" , (Numero_utilisateur,Mot_de_passe, Nom , Prenom, Age, Adresse, Hematies, Hemoglobine, Hematocrite, VGM, CCMH , TCMH, RDW , Polynucleaires_neutrophiles,Polynucleaires_eosinophiles,Polynucleaires_basophiles,Lymphocytes,Monocytes))
        con.commit()
    con.close()

def Utilisateur1():
    con = sqlite3.connect('base.db')
    cursor = con.cursor()
    cursor.execute("SELECT Numero_utilisateur from Patient ;")
    a = cursor.fetchall()
    Utilisateur=""
    for i in a:
        Utilisateur = "".join(map(str, i))

    return Utilisateur


def Mdp1():
    con = sqlite3.connect('base.db')
    cursor = con.cursor()
    cursor.execute("SELECT Mot_de_passe from Patient ;")
    a = cursor.fetchall()
    Mdp=''
    for i in a:
        Mdp = "".join(map(str, i))
    return Mdp

def Nom1():
    con = sqlite3.connect('base.db')
    cursor = con.cursor()
    cursor.execute("SELECT Nom from Patient ;")
    a = cursor.fetchall()
    Nom=''
    for i in a:
        Nom = "".join(map(str, i))
    return Nom

def Prenom1():
    con = sqlite3.connect('base.db')
    cursor = con.cursor()
    cursor.execute("SELECT Prenom from Patient ;")
    a = cursor.fetchall()
    Prenom=''
    for i in a:
        Prenom = "".join(map(str, i))
    return Prenom

def Age1():
    con = sqlite3.connect('base.db')
    cursor = con.cursor()
    cursor.execute("SELECT Age from Patient ;")
    a = cursor.fetchall()
    Age=''
    for i in a:
        Age = "".join(map(str, i))
    return Age

def Adresse1():
    con = sqlite3.connect('base.db')
    cursor = con.cursor()
    cursor.execute("SELECT Adresse from Patient ;")
    a = cursor.fetchall()
    Adresse=''
    for i in a:
        Adresse = "".join(map(str, i))
    return Adresse

def Hematies1():
    con = sqlite3.connect('base.db')
    cursor = con.cursor()
    cursor.execute("SELECT Hematies from Patient ;")
    a = cursor.fetchall()
    Hematies=''
    for i in a:
        Hematies = "".join(map(str, i))
    return Hematies

def Hemoglobine1():
    con = sqlite3.connect('base.db')
    cursor = con.cursor()
    cursor.execute("SELECT Hemoglobine from Patient ;")
    a = cursor.fetchall()
    Hemoglobine=''
    for i in a:
        Hemoglobine = "".join(map(str, i))
    return Hemoglobine

def Hematocrite1():
    con = sqlite3.connect('base.db')
    cursor = con.cursor()
    cursor.execute("SELECT Hematocrite from Patient ;")
    a = cursor.fetchall()
    Hematocrite=''
    for i in a:
        Hematocrite = "".join(map(str, i))
    return Hematocrite

def VGM1():
    con = sqlite3.connect('base.db')
    cursor = con.cursor()
    cursor.execute("SELECT VGM from Patient ;")
    a = cursor.fetchall()
    VGM=''
    for i in a:
        VGM = "".join(map(str, i))
    return VGM

def CCMH1():
    con = sqlite3.connect('base.db')
    cursor = con.cursor()
    cursor.execute("SELECT CCMH from Patient ;")
    a = cursor.fetchall()
    CCMH=''
    for i in a:
        CCMH = "".join(map(str, i))
    return CCMH

def TCMH1():
    con = sqlite3.connect('base.db')
    cursor = con.cursor()
    cursor.execute("SELECT TCMH from Patient ;")
    a = cursor.fetchall()
    TCMH=''
    for i in a:
        TCMH = "".join(map(str, i))
    return TCMH

def RDW1():
    con = sqlite3.connect('base.db')
    cursor = con.cursor()
    cursor.execute("SELECT RDW from Patient ;")
    a = cursor.fetchall()
    RDW=''
    for i in a:
        RDW = "".join(map(str, i))
    return RDW

def Polynucleaires_neutrophiles1():
    con = sqlite3.connect('base.db')
    cursor = con.cursor()
    cursor.execute("SELECT Polynucleaires_neutrophiles from Patient ;")
    a = cursor.fetchall()
    Polynucleaires_neutrophiles=''
    for i in a:
        Polynucleaires_neutrophiles = "".join(map(str, i))
    return Polynucleaires_neutrophiles

def Polynucleaires_eosinophiles1():
    con = sqlite3.connect('base.db')
    cursor = con.cursor()
    cursor.execute("SELECT Polynucleaires_eosinophiles from Patient ;")
    a = cursor.fetchall()
    Polynucleaires_eosinophiles=''
    for i in a:
        Polynucleaires_eosinophiles = "".join(map(str, i))
    return Polynucleaires_eosinophiles

def Polynucleaires_basophiles1():
    con = sqlite3.connect('base.db')
    cursor = con.cursor()
    cursor.execute("SELECT Polynucleaires_basophiles from Patient ;")
    a = cursor.fetchall()
    Polynucleaires_basophiles=''
    for i in a:
        Polynucleaires_basophiles = "".join(map(str, i))
    return Polynucleaires_basophiles

def Lymphocytes1():
    con = sqlite3.connect('base.db')
    cursor = con.cursor()
    cursor.execute("SELECT Lymphocytes from Patient ;")
    a = cursor.fetchall()
    Lymphocytes=''
    for i in a:
        Lymphocytes = "".join(map(str, i))
    return Lymphocytes

def Monocytes1():
    con = sqlite3.connect('base.db')
    cursor = con.cursor()
    cursor.execute("SELECT Monocytes from Patient ;")
    a = cursor.fetchall()
    Monocytes=''
    for i in a:
        Monocytes = "".join(map(str, i))
    return Monocytes


def remplissage(data):
    for i in data:
        Numero_utilisateur = data['Numero_utilisateur']
        Adresse = data['Adresse']
        Mot_de_passe = data['Mot_de_passe']
        Nom = data['Nom']
        Prenom = data['Prenom']
        Age = data['Age']
        Hematies = data['Hematies']
        Hemoglobine = data['Hemoglobine']
        Hematocrite = data['Hematocrite']
        VGM = data['VGM']
        CCMH = data['CCMH']
        TCMH = data['TCMH']
        RDW = data['RDW']
        Polynucleaires_neutrophiles = data['Polynucleaires_neutrophiles']
        Polynucleaires_eosinophiles = data['Polynucleaires_neutrophiles']
        Polynucleaires_basophiles = data['Polynucleaires_basophiles']
        Lymphocytes = data['Lymphocytes']
        Monocytes = data['Monocytes']
    ajoututilisateur(Numero_utilisateur,Mot_de_passe, Nom , Prenom, Age, Adresse, Hematies, Hemoglobine, Hematocrite, VGM, CCMH , TCMH, RDW , Polynucleaires_neutrophiles,Polynucleaires_eosinophiles,Polynucleaires_basophiles,Lymphocytes,Monocytes)

@app1.route('/')
def index():
    return render_template('test1.html')



@app1.route("/Resultats1",methods=['POST'])

def affichage():
    createdb()
    nom = request.form.get("nom")
    fichier = nom+'.json'
    try:
        with open(fichier):pass
    except IOError:
        return 'Erreur! vérifiez le nom'
    f = open(fichier)
    data = json.load(f)
    f.close()
    remplissage(data)
    Utilisateur = Utilisateur1()

    Nom = Nom1()
    Prenom = Prenom1()
    Adresse = Adresse1()
    Mdp = Mdp1()
    Age = Age1()
    Hematies = Hematies1()
    Hemoglobine = Hemoglobine1()
    Hematocrite = Hematocrite1()
    VGM = VGM1()
    VGM = (VGM)
    CCMH = CCMH1()
    TCMH = TCMH1()
    RDW = RDW1()
    Polynucleaires_neutrophiles = Polynucleaires_neutrophiles1()
    Polynucleaires_basophiles = Polynucleaires_basophiles1()
    Polynucleaires_eosinophiles = Polynucleaires_eosinophiles1()
    Lymphocytes = Lymphocytes1()
    Monocytes = Monocytes1()
    login=request.form.get("utilisateur")
    Mdp2=request.form.get("motdepasse")
    print(login,Mdp2)
    print(Utilisateur,Mdp,Nom,Prenom,Age, Adresse, Hematies, Hemoglobine, Hematocrite, VGM, CCMH , TCMH, RDW , Polynucleaires_neutrophiles,Polynucleaires_eosinophiles,Polynucleaires_basophiles,Lymphocytes,Monocytes)
    if login == Utilisateur and Mdp2 == Mdp and nom == Nom:
        return render_template('Resultats1.html',Utilisateur = str(Utilisateur),Mdp = str(Mdp) ,Nom = str(Nom),Prenom = str(Prenom),Age = str(Age), Adresse = str(Adresse), Hematies = str(Hematies), Hemoglobine = str(Hemoglobine), Hematocrite = str(Hematocrite), VGM = str(VGM), CCMH = str(CCMH), TCMH = str(TCMH), RDW = str(RDW), Polynucleaires_neutrophiles = str(Polynucleaires_neutrophiles),Polynucleaires_eosinophiles = str(Polynucleaires_eosinophiles),Polynucleaires_basophiles = str(Polynucleaires_basophiles),Lymphocytes = str(Lymphocytes),Monocytes = str(Monocytes))
    
    else:
        return 'Vous êtes non identifie'
    
@app1.route('/formulaire1')
def espace_perso():
    return render_template('formulaire1.html')

@app1.route("/confirmation",methods=['POST'])

def recup_json():
    L=[]
    Numero_utilisateur = request.form.get('Numero_utilisateur')
    Adresse = request.form.get('Adresse')
    Mot_de_passe = request.form.get('Mot_de_passe')
    Nom = request.form.get('Nom')
    Prenom = request.form.get('Prenom')
    Age = request.form.get('Age')
    Hematies = request.form.get('Hematies')
    Hemoglobine = request.form.get('Hemoglobine')
    Hematocrite = request.form.get('Hematocrite')
    VGM = request.form.get('VGM')
    CCMH = request.form.get('CCMH')
    TCMH = request.form.get('TCMH')
    RDW = request.form.get('RDW')
    Polynucleaires_neutrophiles = request.form.get('Polynucleaires_neutrophiles')
    Polynucleaires_eosinophiles = request.form.get('Polynucleaires_neutrophiles')
    Polynucleaires_basophiles = request.form.get('Polynucleaires_basophiles')
    Lymphocytes = request.form.get('Lymphocytes')
    Monocytes = request.form.get('Monocytes')
    Numerotation_des_plaquettes = request.form.get('Numerotation_des_plaquettes')
        

    data = {
        "Numero_utilisateur":Numero_utilisateur,
        "Mot_de_passe":Mot_de_passe,
        "Nom":Nom,
        "Prenom":Prenom,
        "Age":Age,
        "Adresse":Adresse,
        "Hematies":Hematies,
        "Hemoglobine":Hemoglobine,
        "Hematocrite":Hematocrite,
        "VGM":VGM,
        "CCMH":CCMH,
        "TCMH":TCMH,
        "RDW":RDW,
        "Polynucleaires_neutrophiles":Polynucleaires_neutrophiles,
        "Polynucleaires_eosinophiles":Polynucleaires_eosinophiles,
        "Polynucleaires_basophiles":Polynucleaires_basophiles,
        "Lymphocytes":Lymphocytes,
        "Monocytes":Monocytes,
        "Numerotation_des_plaquettes":Numerotation_des_plaquettes
        }
    with open(Nom+".json", "w") as f_write:
        json.dump(data, f_write, indent=1)
       
    print(L)
    return str(L)