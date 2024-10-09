from django.db import models


class Student(models.Model):
    # Student Information
    surname = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    student_class = models.CharField(max_length=50)
    squadron = models.CharField(max_length=50)
    svc_no = models.CharField(max_length=50)
    admission_date = models.CharField(max_length=50)
    blood_group = models.CharField(max_length=5)
    tribe = models.CharField(max_length=50)
    state_of_origin = models.CharField(max_length=50)
    lga = models.CharField(max_length=50)
    date_of_birth = models.CharField(max_length=50)
    place_of_birth = models.CharField(max_length=100)
    religion = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    hobbies = models.CharField(max_length=200)

    # Guardian/Parent Information
    guardian_parent_name = models.CharField(max_length=100)
    relationship = models.CharField(max_length=50)
    occupation = models.CharField(max_length=100)
    guardian_address = models.CharField(max_length=200)
    guardian_state_of_origin = models.CharField(max_length=50)
    telephone_no = models.CharField(max_length=15)
    next_of_kin = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"