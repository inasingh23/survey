from django.db import models

# Create your models here.
class information(models.Model):
    GENDER_CHOICES = (
        (None, 'Choose an option: '),
        ('M', 'Male'),
        ('F', 'Female'),
    )
    
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age = models.CharField(max_length=1)
    educational_background = models.CharField(max_length=1, default=0)
    occupation = models.CharField(max_length=1)
    location = models.CharField(max_length=1)
    marital_status = models.CharField(max_length=1)
    individual_income = models.CharField(max_length=1)
    family_income = models.CharField(max_length=1)
    tech_q1 = models.CharField(max_length=1,default=0)
    tech_q2 = models.CharField(max_length=1,default=0)
    tech_q3 = models.CharField(max_length=1,default=0)
    tech_q4 = models.CharField(max_length=1,default=0)
    tech_q5 = models.CharField(max_length=1,default=0)
    curr_q1 = models.CharField(max_length=1,default=0)
    curr_q2 = models.CharField(max_length=1,default=0)
    curr_q3 = models.CharField(max_length=1,default=0)
    curr_q4 = models.CharField(max_length=1,default=0)
    curr_q5 = models.CharField(max_length=1,default=0)
    plac_q1 = models.CharField(max_length=1,default=0)
    plac_q2 = models.CharField(max_length=1,default=0)
    plac_q3 = models.CharField(max_length=1,default=0)
    plac_q4 = models.CharField(max_length=1,default=0)
    plac_q5 = models.CharField(max_length=1,default=0)
    sch_q1 = models.CharField(max_length=1,default=0)
    sch_q2 = models.CharField(max_length=1,default=0)
    sch_q3 = models.CharField(max_length=1,default=0)
    sch_q4 = models.CharField(max_length=1,default=0)
    sch_q5 = models.CharField(max_length=1,default=0)
    sec_q1 = models.CharField(max_length=1,default=0)
    sec_q2 = models.CharField(max_length=1,default=0)
    sec_q3 = models.CharField(max_length=1,default=0)
    sec_q4 = models.CharField(max_length=1,default=0)
    sec_q5 = models.CharField(max_length=1,default=0)
    completed = models.BooleanField(default=False)



    def __str__(self):
        return self.name
