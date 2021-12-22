#!/usr/bin/python3


import os
import glob
import shutil
import time
import gzip
from os import system

path = r"/chemin/de/votre/dossier pour renommer l'archive/"

#cherche dans "path" des fichiers ayant pour nom "backup" ou format zip
pattern = path + "NOM" + "*.EXTENTION"
#liste le résultat du "pattern"
result = glob.glob(pattern)


#transforme l'ancien nom en celui de votre choix 
for file_name in result:
    old_name = file_name
    new_name = path + 'NOM' + ".EXTENTION"
    os.rename(old_name, new_name)


#indique le nouveau nom de l'archive 
res = glob.glob(path + "NOM" + "*.EXTENTION" )
for name in res:
    print(name)

#J'ai sur mon bureau deux répertoire afin de décompresser chaque élément séparément pour éviter la confusion, dans un premier temps je déplace l'archive sur mon bureau.
shutil.move('/User/.../.../NOM ARCHIVE.zip','/User/Bureau/')
time.sleep(2)

#Décompression de l'archive contenant les éléments
shutil.unpack_archive('/User/.../NOM ARCHIVE.zip', '/User/Bureau/', 'zip')
time.sleep(2)

#Ici je supprime l'archive contenant les éléments puisque j'en ai plus besoin
os.remove('/User/.../.../NOM ARCHIVE.zip')

#Déplacement des archives dans leur dossier respectif 
shutil.move('/User/.../.../.../.../.../.../NOM ARCHIVE.zip', '/User/.../.../Destination')
shutil.move('/User/.../.../.../.../.../.../NOM ARCHIVE.sql.gz', '/User/.../.../Destination')
time.sleep(2)

#Décompression de mon dossier Wordpress
shutil.unpack_archive('/User/.../.../.../Nom ARCHIVE.zip', '/User/.../.../Destination', 'zip')

time.sleep(2)

#Décompression dump SQL
dir_name = '/User/.../.../Répertoire contenant votre dump/'


def gz_extract(directory):
    extension = ".gz"
    os.chdir(directory)
    for item in os.listdir(directory):  # Parcours les elements dans le dir_name
        if item.endswith(extension):  # vérif si fichier avec extension ".gz"
            gz_name = os.path.abspath(item)  # Obtenir les chemins complet
            file_name = (os.path.basename(gz_name)).rsplit('.', 1)[0]  # Obtenir le nom du fichier
            with gzip.open(gz_name, "rb") as f_in, open(file_name, "wb") as f_out:
                shutil.copyfileobj(f_in, f_out)
            os.remove(gz_name)  # supprime le fichier ".gz"


gz_extract(dir_name)
time.sleep(2)
print("Fichier décompresser dans NOM FICHIER et NOM FICHIER good job, lets go pour le final")

#Je supprime l'archive zip puisqu'elle est décompresser dans un répertoire 
os.remove('/User/.../.../.../Nom Archive.zip')

#Ici j'indique ou ce trouve les fichiers Wordpress et la destination 
source_folderwp = r"/Useer/.../.../Dosier contenant WP/"
destination_folderwp = r"/var/www/html/Votre SITE/"

# On récupère tout les fichiers 
for file_name in os.listdir(source_folderwp):
     # construct full file path
     source = source_folderwp + file_name
     destination = destination_folderwp + file_name
     # copy only files
     if os.path.isfile(source):
         shutil.copyfile(source, destination)
         print('copier', file_name)
time.sleep(2)
print("On patiente quelques instants pour faire un peu le ménage on est pas de gros dégueulasse quand même =D ")
time.sleep(2)


#ici je supprime les répertoire puisque plus besoin pour en recrée un autre prêt pour une futur utilisation sans avoir de données dedans. 

delbckpw = '/User/.../.../Dossier contenant vos fichier décompresser'
shutil.rmtree(delbckpw)
time.sleep(1)

creatbckpwp = '/User/.../.../Nom de votre dossier'
os.mkdir(creatbckpwp)

print("Minute papillon on importe la BDD pour le site ;) ")
time.sleep(5)

#Importation de la base SQL
USERNAME = ""
PASSWORD = ""
DBNAME = ""
HOST = "localhost"
FILE = "/User/.../.../.../VOTRE BASE SQL.sql"
PORT = 3306
command = """mysql -u %s -p"%s" --host %s --port %s %s < %s""" %(USERNAME, PASSWORD, HOST, PORT, DBNAME, FILE)
system(command)

delbckbdd = '/User/.../.../Dossier contenant votre BDD '
shutil.rmtree(delbckbdd)

creatbckpbdd = '/User/.../.../Nom de votre dossier'
os.mkdir(creatbckpbdd)

print("C'est fini!! Bien joué le SysAdmin!! You wanna rock! ")

