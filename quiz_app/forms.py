from django import forms
from .models import information

class demographic_form(forms.ModelForm):
    class Meta:
        model = information
        fields = ['name','gender','age','educational_background','occupation','location','marital_status','individual_income','family_income']
        labels = {
            "individual_income": "Individual income (Monthly)",
            "family_income": "Family income (Monthly)"
        }
        AGE_CHOICES = [('A','A. 15-20 years'),
                       ('B','B. 20-25 years'),
                       ('C','C. 25-30 years'),
                       ('D','D. Over 30 years'),]
        EDU_CHOICES = [('A','A. Not attended school'),
                       ('B','B. Completed schooling'),
                       ('C','C. Graduate'),
                       ('D','D. Post - graduate'),
                       ('E','E. Doctorate'),]
        OCCU_CHOICES = [('A','A. Student'),
                       ('B','B. Working - Full time'),
                       ('C','C. Working - Part time'),
                       ('D','D. Freelancers'),
                       ('E','E. Self employed'),
                       ('F','F. Unemployed'),]
        LOC_CHOICES = [('A','A. Metropolitan - Eg. New Delhi, Mumbai, Bangalore'),
                       ('B','B. City - Tier 2, Tier 3 - Eg. Agra, Nagpur, Mysore'),
                       ('C','C. Town - Eg. Kottayam, Gudur, Ratnagiri'),
                       ('D','D. Village - Eg. Achala, Mattur, Gahmar'),
                       ('E','E. Others'),]
        MAR_CHOICES = [('A','A. Married'),
                       ('B','B. Unmarried'),
                       ('C','C. Divorced'),
                       ('D','D. Widowed'),
                       ('E','E. Others'),]
        IND_INC_CHOICES = [('A','A. Unemployed'),
                       ('B','B. Less than 10,000 INR'),
                       ('C','C. Between 10,000 - 50,000 INR'),
                       ('D','D. Between 50,000 - 1,00,000 INR'),
                       ('E','E. Between 1,00,000 - 1,50,000 INR'),
                       ('F','F. More than 1,50,000 INR'),]
        FAM_INC_CHOICES = [('A','A. Less than 10,000 INR'),
                       ('B','B. Between 10,000 - 50,000 INR'),
                       ('C','C. Between 50,000 - 1,00,000 INR'),
                       ('D','D. Between 1,00,000 - 1,50,000 INR'),
                       ('E','E. More than 1,50,000 INR'),]

        #age=forms.CharField(widget=forms.RadioSelect(choices=AGE_CHOICES))
        widgets={
        #    'age':forms.RadioSelect(attrs={'choices':'AGE_CHOICES'}),
             'age':forms.RadioSelect(choices=AGE_CHOICES),
             'educational_background': forms.RadioSelect(choices=EDU_CHOICES),
             'occupation':forms.RadioSelect(choices=OCCU_CHOICES),
             'location':forms.RadioSelect(choices=LOC_CHOICES),
             'marital_status':forms.RadioSelect(choices=MAR_CHOICES),
             'individual_income':forms.RadioSelect(choices=IND_INC_CHOICES),
             'family_income':forms.RadioSelect(choices=FAM_INC_CHOICES),
             }

class technology_form(forms.ModelForm):
    class Meta:
        model = information
        fields = ['tech_q1','tech_q2','tech_q3','tech_q4','tech_q5']
        labels = {
            "tech_q1": "A. Technology enabled me learning my modules better",
            "tech_q2": "B. Technology was necessary to learn my job role",
            "tech_q3": "C. Knowing technology was a pre-requisite to my job role",
            "tech_q4": "D. Technology related training was given during my course",
            "tech_q5": "E. My courses included technology related modules",
        }
        TECH_CHOICES = [('A','A. Strongly Disagree'),
                    ('B','B. Disagree'),
                    ('C','C. Neither Agree Nor Disagree'),
                    ('D','D. Agree'),
                    ('E','E. Strongly Agree'),]
        widgets={
             'tech_q1':forms.RadioSelect(choices=TECH_CHOICES),
             'tech_q2':forms.RadioSelect(choices=TECH_CHOICES),
             'tech_q3':forms.RadioSelect(choices=TECH_CHOICES),
             'tech_q4':forms.RadioSelect(choices=TECH_CHOICES),
             'tech_q5':forms.RadioSelect(choices=TECH_CHOICES),
             }
        
class curriculum_form(forms.ModelForm):
    class Meta:
        model = information
        fields = ['curr_q1','curr_q2','curr_q3','curr_q4','curr_q5']
        labels = {
            "curr_q1": "A. Curriculum related information was provided to me",
            "curr_q2": "B. Curriculum was designed suitably for my job role",
            "curr_q3": "C. The instructor followed the curriculum throughout the training",
            "curr_q4": "D. The instructor/trainers/faculty had good knowledge of the curriculum",
            "curr_q5": "E. Curriculum/courses were completely covered before exams",
        }
        CURR_CHOICES = [('A','A. Strongly Disagree'),
                    ('B','B. Disagree'),
                    ('C','C. Neither Agree Nor Disagree'),
                    ('D','D. Agree'),
                    ('E','E. Strongly Agree'),]
        widgets={
             'curr_q1':forms.RadioSelect(choices=CURR_CHOICES),
             'curr_q2':forms.RadioSelect(choices=CURR_CHOICES),
             'curr_q3':forms.RadioSelect(choices=CURR_CHOICES),
             'curr_q4':forms.RadioSelect(choices=CURR_CHOICES),
             'curr_q5':forms.RadioSelect(choices=CURR_CHOICES),
        }

class placement_form(forms.ModelForm):
    class Meta:
        model = information
        fields = ['plac_q1','plac_q2','plac_q3','plac_q4','plac_q5']
        labels = {
            "plac_q1": "A. Placement related information was told to me before appearing for Interviews",
            "plac_q2": "B. Placement related training was provided",
            "plac_q3": "C. Placement opportunities were provided to me",
            "plac_q4": "D. The instructor/faculty prepared me for placement opportunities during my job role training",
            "plac_q5": "E. Placement related infrastructure was available in my training centre",
        }
        PLAC_CHOICES = [('A','A. Strongly Disagree'),
                    ('B','B. Disagree'),
                    ('C','C. Neither Agree Nor Disagree'),
                    ('D','D. Agree'),
                    ('E','E. Strongly Agree'),]
        widgets={
             'plac_q1':forms.RadioSelect(choices=PLAC_CHOICES),
             'plac_q2':forms.RadioSelect(choices=PLAC_CHOICES),
             'plac_q3':forms.RadioSelect(choices=PLAC_CHOICES),
             'plac_q4':forms.RadioSelect(choices=PLAC_CHOICES),           
             'plac_q5':forms.RadioSelect(choices=PLAC_CHOICES),
        }

class schemes_form(forms.ModelForm):
    class Meta:
        model = information
        fields = ['sch_q1','sch_q2','sch_q3','sch_q4','sch_q5']
        labels = {
            "sch_q1": "A. I had counselling on the state government schemes",
            "sch_q2": "B. State government schemes was useful to me",
            "sch_q3": "C. State government schemes helped me improved my livelihood",
            "sch_q4": "D. State government schemes had any condition to fulfil before availing",
            "sch_q5": "E. State government schemes were utilized by me",
        }
        SCH_CHOICES = [('A','A. Strongly Disagree'),
                    ('B','B. Disagree'),
                    ('C','C. Neither Agree Nor Disagree'),
                    ('D','D. Agree'),
                    ('E','E. Strongly Agree'),]
        widgets={
             'sch_q1':forms.RadioSelect(choices=SCH_CHOICES),
             'sch_q2':forms.RadioSelect(choices=SCH_CHOICES),
             'sch_q3':forms.RadioSelect(choices=SCH_CHOICES),
             'sch_q4':forms.RadioSelect(choices=SCH_CHOICES),
             'sch_q5':forms.RadioSelect(choices=SCH_CHOICES),             
        }

class sector_form(forms.ModelForm):
    class Meta:
        model = information
        fields = ['sec_q1','sec_q2','sec_q3','sec_q4','sec_q5']
        labels = {
            "sec_q1": "A. I know about various Job sectors in India",
            "sec_q2": "B. Selecting relevant courses across various sectors / fields is important for placements",
            "sec_q3": "C. Emerging technologies are very important for any sector to find Jobs",
            "sec_q4": "D. Startup India movement is helping India in various sectors create Jobs",
            "sec_q5": "E. Soft skills are important in any sector to find Jobs",
        }
        SEC_CHOICES = [('A','A. Strongly Disagree'),
                    ('B','B. Disagree'),
                    ('C','C. Neither Agree Nor Disagree'),
                    ('D','D. Agree'),
                    ('E','E. Strongly Agree'),]
        widgets={
             'sec_q1':forms.RadioSelect(choices=SEC_CHOICES),
             'sec_q2':forms.RadioSelect(choices=SEC_CHOICES),
             'sec_q3':forms.RadioSelect(choices=SEC_CHOICES),
             'sec_q4':forms.RadioSelect(choices=SEC_CHOICES),
             'sec_q5':forms.RadioSelect(choices=SEC_CHOICES),             
        }