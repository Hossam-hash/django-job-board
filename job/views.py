from django.shortcuts import render
from .models import Job
# Create your views here.
from django.core.paginator import Paginator
from  .form import ApplyForm





#model querey set

def job_list(request):
    job_list=Job.objects.all()
    #print(job_list)
    paginator = Paginator(job_list, 1)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context={'jobs':page_obj} #template name
    return render(request,'job/job_list.html',context)

def job_details(request,slug):#id to filter and get the wanted job
    job_detail=Job.objects.get(slug=slug)

    if request.method=="POST":#means that i click at apply
        form=ApplyForm(request.POST,request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.job=job_detail
            myform.save()
    else:#the page form is empty and dont click at apply
        form=ApplyForm()

    context={'job':job_detail,'form1':form}
    return render(request,'job/job_details.html',context)
