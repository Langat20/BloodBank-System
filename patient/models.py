from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

class Patient(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key= True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient')
    image = models.ImageField(upload_to='images/', blank=True)
    age=models.PositiveIntegerField()
    bloodgroup=models.CharField(max_length=10)
    disease=models.CharField(max_length=100)
    doctorname=models.CharField(max_length=50)
<<<<<<< HEAD
<<<<<<< HEAD
    emailaddress = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
=======
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)

>>>>>>> 968e2f3ede6ecbc90af6a613fca2991231ab086a
=======
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)

>>>>>>> 5acda11030eb4a47ec19200d275f46345ce53468
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_instance(self):
        return self
    def __str__(self):
        return self.user.username
