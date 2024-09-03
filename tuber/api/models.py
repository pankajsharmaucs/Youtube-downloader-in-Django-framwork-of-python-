from django.db import models

class Posts(models.Model):
    title=models.CharField(max_length=130)
    create_date=models.DateTimeField()
    image=models.ImageField()
    details=models.TextField()


