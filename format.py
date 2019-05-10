# ====================================================================== IMPORTS ========================================================================
import sys
import os

# ====================================================================== CONSTANTE ======================================================================
listeFormat = ["png","PNG","jpeg","JPEG","jpg","JPG"]


# ====================================================================== FONCTIONS ======================================================================

def cleanImage(path):
	'''
		Objectif : 
			Supprimer tout les fichiers du dossier donnée en paramètre n'ayant pas l'une des extensions suivante
			png, jpeg, jpg
		Entree : 
			- le path du dossier
		Sortie : 
	'''
	[os.system("rm " + path + "/" + fichier) for fichier in os.listdir(path) if not fichier.endswith(tuple(listeFormat))]
	


def renameAllFile(path, newName) :
	'''
		Objectif : 
			Renome toute les images se trouvant dans le dossier en suivant le partern donné suivant newMane (donné en paramètre)  + indice
		Entree : 
			- le path du dossier
			- le nouveau nom pour les images
		Sortie : 
	'''

	for root, dirs, files in os.walk(path):
		i = 0
		for file in files:
			os.rename(path + "/" + file, path + "/" + newName + str(i) + "." + file.split(".")[-1])
			i+=1


def convertImage(path, newExtension):
	'''
		Objectif : 
			Converti toute les images en fonction de l'extension donné en paramètre
		Entree : 
			- le path du dossier
			- la nouvelle extension
		Sortie : 
	'''
	
	listeResult = [fichier.split(".")[-1] for fichier in os.listdir(path) if not fichier.endswith(newExtension)]
	[os.system("mogrify -format " + newExtension + " " + path +"/*." + extension) for extension in set(listeResult)]
	[os.system("rm " + path + "/" + fichier) for fichier in os.listdir(path) if not fichier.endswith(newExtension)]



# TODO a ameliore ou faire dans javascript
def creeEmptyLabel(path):

	for fichier in os.listdir(path) :
	
		if not fichier.endswith("txt") :
			if fichier.split(".")[0] + ".txt" not in os.listdir(path) :
				print(fichier)
				#os.system("touch " + fichier.split(".")[0] + ".txt")
		
		
		

# ====================================================================== EXECUTION ======================================================================


if __name__ == "__main__":

	creeEmptyLabel(".")

	if len(sys.argv) < 3 :
		print("Un argument est manquant !\n Veuillez saisir :\n -le nom du fichier python \n -le path du dossier ou se trouve les fichiers \n -le nouveau nom")
		exit(0)

		
	path = sys.argv[1]
	newName = sys.argv[2]

	#cleanImage(path)
	#renameAllFile(path,newName)
	#convertImage(path, "jpg")

