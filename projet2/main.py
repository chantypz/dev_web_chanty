# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 01:12:35 2021

@author: etudiant
"""

from flask import Flask,render_template,request,jsonify
import sqlite3
import json

app1=Flask(__name__)




def createdb():
    conn = sqlite3.connect ('base.db')
    print ("base de donnéées ouverte avec succès")
    conn.execute("CREATE TABLE IF NOT EXISTS Patient(Numero_utilisateur INTEGER, Mot_de_passe TEXT, Nom TEXT, Prenom TEXT, code postal INTEGER, Adresse TEXT,email TEXT)")
    print ("Table créée avec succès")
    conn.close()

def ajoututilisateur(Numero_utilisateur,Mot_de_passe, Nom , Prenom, email, Adresse,codepostal):
    with sqlite3.connect("base.db") as con:
        cur = con.cursor()
        cur.execute(" INSERT INTO Patient (Numero_utilisateur,Mot_de_passe, Nom , Prenom, email, Adresse,code postal) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)" , (Numero_utilisateur,Mot_de_passe, Nom , Prenom, Age, Adresse))
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





def remplissage(data):
    for i in data:
        Numero_utilisateur = data['Numero_utilisateur']
        Adresse = data['Adresse']
        Mot_de_passe = data['Mot_de_passe']
        Nom = data['Nom']
        Prenom = data['Prenom']
        Age = data['Age']
        email = data['email']
        code postal = ['code_postal']
    ajoututilisateur(Numero_utilisateur,Mot_de_passe, Nom , Prenom, email, Adresse,code postal)

@app1.route('/')
def index():
    return render_template('test.html')



@app1.route("/Resultats",methods=['POST'])

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
    
    login=request.form.get("utilisateur")
    Mdp2=request.form.get("motdepasse")
    print(login,Mdp2)
    print(Utilisateur,Mdp,Nom,Prenom,email, Adresse,code postal)
    if login == Utilisateur and Mdp2 == Mdp and nom == Nom:
        return render_template('Resultats.html',Utilisateur = str(Utilisateur),Mdp = str(Mdp) ,Nom = str(Nom),Prenom = str(Prenom),Age = str(Age), Adresse = str(Adresse), Hematies = str(Hematies), Hemoglobine = str(Hemoglobine), Hematocrite = str(Hematocrite), VGM = str(VGM), CCMH = str(CCMH), TCMH = str(TCMH), RDW = str(RDW), Polynucleaires_neutrophiles = str(Polynucleaires_neutrophiles),Polynucleaires_eosinophiles = str(Polynucleaires_eosinophiles),Polynucleaires_basophiles = str(Polynucleaires_basophiles),Lymphocytes = str(Lymphocytes),Monocytes = str(Monocytes))
    
    else:
        return 'Vous êtes non identifie'
    
@app1.route('/formulaire')
def espace_perso():
    return render_template('formulaire.html')

@app1.route("/confirmation",methods=['POST'])

def recup_json():
    L=[]
    Numero_utilisateur = request.form.get('Numero_utilisateur')
    Adresse = request.form.get('Adresse')
    Mot_de_passe = request.form.get('Mot_de_passe')
    Nom = request.form.get('Nom')
    Prenom = request.form.get('Prenom')
    email = request.form.get('email')
    code postal = request.form.get('code_postal')
    
        

    data = {
        "Numero_utilisateur":Numero_utilisateur,
        "Mot_de_passe":Mot_de_passe,
        "Nom":Nom,
        "Prenom":Prenom,
        "email":email,
        "Adresse":Adresse,
        "code postal":code_postal,
        }
    with open(Nom+".json", "w") as f_write:
        json.dump(data, f_write, indent=1)
       
    print(L)
    return str(L)