from django.db import models

# Create your models here.

class user(models.Model):
    user_name = models.CharField(max_length = 20)
    contact_no = models.CharField(max_length = 10)
    email_id = models.EmailField(max_length = 40)
    vaccine_name = models.CharField(max_length = 20, blank = True, null = True)
    dose_no = models.CharField(max_length = 20, blank = True, null = True)
    date_of_birth = models.DateField()
    date_of_vaccianatio = models.DateField(blank = True, null = True)

    def __str__(self):return self.user_name +"\t" + self.email_id