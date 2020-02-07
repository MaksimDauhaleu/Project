from django.db import models
import re
import bcrypt

class LoginManager(models.Manager):
    def reg_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        user = User.objects.filter(email = postData['email'])

        if len(postData['first_name']) < 5:
            errors['first_name'] = "First name should be at least 5 characters"
            
        if len(postData['last_name']) < 5:
            errors['last_name'] = "Last name should be at least 5 characters"

        if len(postData['location']) < 5:
            errors['location'] = "Location name should be at least 5 characters"

        if len(user)>0:
            errors["email"] = "Email exist"

        if len(postData['email']) < 5:
            errors['email'] = "Email should be at least 5 characters"

        if not EMAIL_REGEX.match(postData['email']):         
            errors['email'] = "Invalid email address!"

        if len(postData["password"]) < 8:
            errors["password"] = "The password must be at least 8 characters."
        
        if postData["password_conf"] != postData["password"]:
            errors["password_conf"] = "Passwords does not match"

        return errors

    def login_validator(self, postData):
        errors = {}
        user = User.objects.filter(email = postData['email'])
        if not user:
            errors['email'] = 'User does not exist'
        else:
            if bcrypt.checkpw(postData['password'].encode('utf-8'), user[0].password.encode()):
                pass
            else:
                errors['password'] = "Wrong Password"
        
        return errors











class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=65)
    phone_number = models.CharField(max_length=12)
    password = models.CharField(max_length=65)
    location = models.CharField(max_length=65)
    on_call = models.BooleanField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = LoginManager()

