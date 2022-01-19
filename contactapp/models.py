from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    group = models.ForeignKey(to=Group, on_delete=models.SET_NULL, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


