from django.db import models


# Create your models here.
class ContactMessage(models.Model):
    '''
    model to store messages from customers to the company
    '''
    email = models.EmailField(max_length=254, null=False, blank=False)
    subject = models.CharField(max_length=255, null=False, blank=False)
    message = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.subject
