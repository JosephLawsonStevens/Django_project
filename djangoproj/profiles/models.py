from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    def __repr__(self):
        return f'Users(name="{self.name}",email = "{self.email}")'
