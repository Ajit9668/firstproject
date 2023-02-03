from django.db import models

class ModuleInfo(models.Model):
    Module_Name=models.TextField()
    Module_Image=models.TextField()
    Module_Link=models.TextField()
    Module_SeqNo=models.PositiveIntegerField(default=1, unique=True)
    
