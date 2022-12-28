from django.db import models

# Create your models here.
class  Client(models.Model):
    identite=models.CharField(max_length=20)  
    nom = models.CharField(max_length=50)
    prenom= models.CharField(max_length=50)
    contact= models.CharField(max_length=50)
    
    def __str__(self):
        return self.nom 
    
    
class Livre(models.Model):
    numeroserie=models.ForeignKey(Client, on_delete=models.CASCADE)
    titre_livre=models.CharField(max_length=50)
    
    def __str__(self):
        return self.titre_livre
    
        

    

   