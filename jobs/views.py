from django.shortcuts import render

#importing the class from the models file
from .models import Job

def joblist (request):
    #this pulls all the instances of the Job class and saves to a variable jobs
    jobs = Job.objects
    # pass the variable into the return statement. It has to be a dictionary element with a string key to work in html
    return render(request, 'jobs/joblist.html', {'jobs': jobs})
