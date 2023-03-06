from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import information
from .forms import demographic_form, technology_form, curriculum_form, placement_form, schemes_form, sector_form
# Create your views here.
def home(request):    
    form = demographic_form()
    if request.method=="POST":
        demo_form = demographic_form(request.POST)
        if demo_form.is_valid():
            request.session['user_name'] = demo_form.cleaned_data['name']
            check_model = information.objects.filter(name__iexact=request.session['user_name'])
            for obj in check_model:
                if obj.completed == True:
                    return HttpResponse ("<h2> Your response has already been recorded.</h2>")
                else:    
                    check_model.delete()
            demo_form.save()
            tech_form = technology_form()
            return render (request, 'quiz_app/technology.html',{'form':tech_form}) 
    return render (request, 'quiz_app/index.html',{'form':form}) 

def technology(request):
    if request.method=="POST":
        model_obj = information.objects.get(name=request.session['user_name'])
        tech_form = technology_form(request.POST, instance=model_obj)
        if tech_form.is_valid():
            tech_form.save()
            curr_form = curriculum_form()
            return render (request, 'quiz_app/curriculum.html',{'form':curr_form})
    return render (request, 'quiz_app/technology.html')

def curriculum(request):
    if request.method=="POST":
        model_obj = information.objects.get(name=request.session['user_name'])
        curr_form = curriculum_form(request.POST, instance=model_obj)
        if curr_form.is_valid():
            curr_form.save()
            plac_form = placement_form()
            return render (request, 'quiz_app/placement.html',{'form':plac_form})
    return render (request, 'quiz_app/curriculum.html')

def placement(request):
    if request.method=="POST":
        model_obj = information.objects.get(name=request.session['user_name'])
        plac_form = placement_form(request.POST, instance=model_obj)
        if plac_form.is_valid():
            plac_form.save()
            sch_form = schemes_form()
            return render (request, 'quiz_app/schemes.html',{'form':sch_form})
    return render (request, 'quiz_app/placement.html')

def schemes(request):
    if request.method=="POST":
        model_obj = information.objects.get(name=request.session['user_name'])
        sch_form = schemes_form(request.POST, instance=model_obj)
        if sch_form.is_valid():
            sch_form.save()
            sec_form = sector_form()
            return render (request, 'quiz_app/sector.html',{'form':sec_form})
    return render (request, 'quiz_app/schemes.html')

def sector(request):
    if request.method=="POST":
        model_obj = information.objects.get(name=request.session['user_name'])
        sec_form = sector_form(request.POST, instance=model_obj)
        if sec_form.is_valid():
            model_obj.completed = True
            sec_form.save()
            #model_obj.completed = True
            return render (request, 'quiz_app/thanks.html')
    return render (request, 'quiz_app/sector.html')