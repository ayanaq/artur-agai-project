from django.db import models
import uuid
class Medicine(models.Model):
    image = models.ImageField(upload_to="media/")
    name = models.CharField(max_length=250)
    recept = models.CharField(max_length=500)
    usage = models.CharField(max_length=500)
    amount = models.IntegerField(default=0)
    price = models.IntegerField()
    type_of_med = models.ForeignKey("Type_of_med", on_delete=models.PROTECT)
    last_update = models.DateField(auto_now=True)
    link = models.CharField(max_length=255, unique=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.link:
            self.link = str(uuid.uuid4())
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Type_of_med(models.Model):
    name = models.CharField(max_length=250)
    link = models.CharField(max_length=255, unique=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.link:
            self.link = str(uuid.uuid4())
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name