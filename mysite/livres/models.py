from django.db import models

class Livre(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')  # assurez-vous d'avoir installé Pillow pour gérer les images
    pdf = models.FileField(upload_to='pdfs/')  # le fichier PDF
