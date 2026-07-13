from django.db import models


class Employee(models.Model):

    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    last_name = models.CharField(max_length=100)

    date_of_birth = models.DateField()

    mobile_number = models.CharField(max_length=15)
    alternate_mobile_number = models.CharField(
        max_length=15,
        blank=True,
        null=True
    )

    email = models.EmailField(max_length=100)

    MARITAL_STATUS_CHOICES = [
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Divorced', 'Divorced'),
        ('Widowed', 'Widowed'),
    ]

    marital_status = models.CharField(
        max_length=20,
        choices=MARITAL_STATUS_CHOICES
    )

    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]

    blood_group = models.CharField(
        max_length=3,
        choices=BLOOD_GROUP_CHOICES,
        blank=True,
        null=True
    )

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"