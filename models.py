from django.db import models

class Curiosity(models.Model):
    # Define o campo 'title' como uma cadeia de caracteres com no máximo 100 caracteres
    title = models.CharField(max_length=100)
    # Define o campo 'info_1' como um texto longo
    info_1 = models.TextField()
    # Define o campo 'info_2' como um texto longo
    info_2 = models.TextField()
    # Define o campo 'info_3' como um texto longo
    info_3 = models.TextField()

class TopScorer(models.Model):
    # Define o campo 'title' como uma cadeia de caracteres com no máximo 100 caracteres
    title = models.CharField(max_length=100)
    # Define o campo 'info_1' como um texto longo
    info_1 = models.TextField()
    # Define o campo 'info_2' como um texto longo
    info_2 = models.TextField()
    # Define o campo 'info_3' como um texto longo
    info_3 = models.TextField()
