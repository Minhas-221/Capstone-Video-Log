from .models import Courses
from django.shortcuts import redirect, render
from django.views import View

# Create your views here.
def index(request):
    obj = Courses.objects.all()
    return render(request, 'index.html', {'courses': obj, 'msg': ""})

def contactus(request):
    
    return render(request, 'contactus.html')

def form(request):
    return render(request, 'form.html')

class MainFormView(View):
    def post(self,request):

# def cform(request):
        if request.method == 'POST':
            button = request.POST['b1']
            if button == "Insert":
                branch = request.POST['branch']
                name = request.POST['cname']
                cid = request.POST['cid']
                date = request.POST['date']
                credit = request.POST['cr']
                img = request.FILES['img']
                dis = request.POST['cdis']
                fac1 = request.POST['fac1']
                fac2 = request.POST['fac2']
                fac3 = request.POST['fac3']
                tt = request.POST['tt']
                cc = request.POST['cc']
                obj = Courses.objects.create(id=cid,
                                            name=name,
                                            img=img,
                                            date=date,
                                            branch=branch,
                                            credit=credit,
                                            dis=dis,
                                            fac1=fac1,
                                            fac2=fac2,
                                            fac3=fac3,
                                            ttime=tt,
                                            ctype=cc)
                msg = "Course Inserted"
                return render(request, 'index.html', {'msg': msg})
            elif button == "Delete":
                cid = request.POST['cid']
                print("cid \n\n",cid)
                obj = Courses.objects.get(id=cid)
                obj.delete()
                msg = "Course Deleted"
                return render(request, 'index.html', {'msg': msg})
            elif button == "Update":
                cid = request.POST['cid']
                print("cid \n\n",cid)
                obj = Courses.objects.get(id=cid)
                obj.branch = request.POST['branch']
                obj.name = request.POST['cname']
                obj.id = request.POST['cid']
                obj.date = request.POST['date']
                obj.credit = request.POST['cr']
                obj.img = request.FILES['img']
                obj.dis = request.POST['cdis']
                obj.fac1 = request.POST['fac1']
                obj.ttime = request.POST['tt']
                obj.ctype = request.POST['cc']
                obj.fac2 = request.POST['fac2']
                obj.fac3 = request.POST['fac3']
                obj.save()
                msg = "Course Updated"
                return render(request, 'index.html', {'msg': msg})
            elif button == "Select":
                cid = request.POST['cid']
                obj = Courses.objects.get(id=cid)
                msg = "Selected Course"
                return render(request, 'show.html', {'course': obj, 'msg': msg})
