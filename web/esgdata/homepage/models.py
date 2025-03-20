from django.db import models

# Create your models here.

class Entity(models.Model):
    id = models.IntegerField(primary_key=True) 
    name = models.CharField(max_length=100)
    descr = models.TextField()
    class Meta:
        db_table = 'entity' 

class ESGStandard(models.Model):
    iso_standard = models.CharField(max_length=100)
    release_date = models.CharField(max_length=4)
    sector = models.CharField(max_length=100)
    esg_component = models.CharField(max_length=100)
    
    class Meta:
        db_table = '[esg].[iso_standards]' 
    def __str__(self):
        return f"{self.iso_standard} - {self.release_date} - {self.sector} - {self.esg_component}"

class Attributes(models.Model):
    attribute_name = models.CharField(max_length=1000)
    measuring_unit = models.CharField(max_length=50)
    GWP_factor = models.IntegerField()
    scope = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    
    class Meta:
        db_table = '[esg].[attributes]' 
    def __str__(self):
        return f"{self.attribute_name} - {self.measuring_unit} - {self.GWP_factor} - {self.scope} - {self.category}"
