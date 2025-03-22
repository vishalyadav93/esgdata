from django.db import models
import datetime
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
    user_id = models.IntegerField(default=1)
    attribute_name = models.CharField(primary_key=True,max_length=900)
    linked_indicator_name = models.CharField(max_length=900)
    measuring_unit = models.CharField(max_length=50)
    GWP_factor = models.IntegerField()
    scope = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    
    class Meta:
        db_table = '[esg].[indicator_attributes]' 
    def __str__(self):
        return f"{self.attribute_name} -{self.linked_indicator_name}  -{self.measuring_unit} - {self.GWP_factor} - {self.scope} - {self.category}"
        
class SelectedMateriality(models.Model):
    user_id = models.IntegerField(default=1)
    linked_indicator_name = models.CharField(max_length=900)
    material_name = models.CharField(max_length=1000)
    effective_date = models.CharField(default=datetime.datetime.now(),max_length=4)
    
    class Meta:
        db_table = '[esg].[material_assesment]' 
    def __str__(self):
        return f"{self.user_id} - {self.material_name} - {self.linked_indicator_name}"
