from django.db import models

# Create your models here.


class SignUp(models.Model):
    name = models.CharField(max_length=255)  # may put blank=True to make it not required
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name





