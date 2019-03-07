from django.db import models

class Email(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=50, null=True)
    content = models.TextField()
    send_from = models.EmailField(null=True)
    email_name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name