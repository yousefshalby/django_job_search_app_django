from django.shortcuts import render, redirect
from .models import Job
from django.core.paginator import Paginator
from .forms import ApplyForm, JobForm, CategoryForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .filters import JobFilter
from django.contrib import messages


# Create your views here.
def job_list(request):
    job_list = Job.objects.all()
    myfilter = JobFilter(request.GET,queryset=job_list)
    job_list = myfilter.qs


    paginator = Paginator(job_list, 3) 
    page_number = request.GET.get('page') 
    page_obj = paginator.get_page(page_number) 

    return render(request,'job/job_list.html', {'page_obj' :page_obj , 'myfilter' : myfilter})



def job_detail(request , slug):
    job_detail = Job.objects.get(slug=slug)

    if request.method=='POST':
        form = ApplyForm(request.POST , request.FILES) 
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job_detail 
            myform.save()

    else:
        form = ApplyForm()

    return render(request,'job/job_detail.html', {'job' : job_detail , 'form1':form})

@login_required
def add_job(request):
    if request.method=='POST':
        form = JobForm(request.POST , request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            messages.success(request , 'your job has been added successfully')
            return redirect(reverse('jobs:job_list'))

    else:
        form = JobForm()

    return render(request,'job/add_job.html',{'form':form})


@login_required
def job_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save() 
            messages.success(request , 'your category has been added successfully')
            return redirect ('jobs:job_list')    

    else:
        form = CategoryForm()   

    return render(request,'job/category.html',{'form':form})
