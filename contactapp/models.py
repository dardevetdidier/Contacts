from django.db import models


class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    group = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_created', )

    def __str__(self):
        return self.full_name


