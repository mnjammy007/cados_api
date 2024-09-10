from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=250, null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class Advocate(models.Model):
    username = models.CharField(max_length=255)
    bio = models.TextField(max_length=250, null=True, blank=True)
    company = models.ForeignKey(
        Company, on_delete=models.SET_NULL, null=True, blank=True, default=None
    )

    def __str__(self) -> str:
        return self.username
