from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.hashers import make_password, check_password
from misc_files.genericFunctions import generate_string, link_send
from frontpanel.models import RoleDetails, UserRole
from frontpanel.forms import RoleDetailsForm

def admin_index(request):
    return render(request,"adminindex.html")
def login(request):
    if request.method == 'POST':
        get_email = request.POST["email"]
        get_password = request.POST["password"]
        try:
            data =RoleDetails.objects.get(email=get_email)
            db_password = data.password
            db_active = data.active
            db_verify_link = data.verify_link
            role=data.role_id
            if check_password(get_password, db_password):
               if db_active == '0' and db_verify_link == "":
                   return HttpResponse("please verify your email")
               elif db_active=="1":

                   request.session['email']=get_email
                   request.session['name'] = data.name
                   request.session['image'] = data.image
                   request.session['role'] = role
                   if role==1:
                       return render(request,"update_password.html")
                   elif role==2:
                       pass
            else:
                return HttpResponse('password invalid')
        except:
            return HttpResponse('<h1>Email not found</h1>')
    return render(request, "login.html")


def verify_link(request):
    get_link=request.GET['link']#square bracket de quotes vich jera url ch link dita oh name likhna a
    session_mail=request.session['email']
    data=RoleDetails.objects.get(email=session_mail)
    db_verify=data.verify_link
    if get_link==db_verify:
        update=RoleDetails(email=session_mail, active=1, verify_link="")
        update.save(update_fields=['active', 'verify_link'])
        return redirect("/update_password/")
        #return HttpResponse("hi")


def register(request):
    data = UserRole.objects.all()
    if request.method == "POST":
        form = RoleDetailsForm(request.POST)
        # <!--this request.post is complsory to write when we crete the object of the class--

        #if form.is_valid():
        f = form.save(commit=False)
        # this the another object of class which wil take care that accidently no data will go to the database
        # f.role_id=1
        f.role_id = request.POST['role']
        f.name = request.POST['name']
        f.email = request.POST['email']
        # f.password = request.POST['password']
        # f.mobile = request.POST['mobile']
        # f.address = request.POST['address']
        f.gender = request.POST['gender']
        f.active = str(0)
        string = generate_string()
        link = make_password(string)
        link=link.replace("+", "")
        f.password = link
        f.verify_link = link

        f.save()
        f_link = "127.0.0.1:8000/verify_link/?link=" + link
        request.session['email'] = f.email
        link_send(f.email, f_link, string)
        return render(request, "re.html", {'confirm': True})
    return render(request, "re.html", {'data': data})

def update_password(request):
    if request.method == 'POST':
        get_password = request.POST["password"]
        get_confirm_password = request.POST["cpassword"]
        session_mail=request.session_mail['email']
        if get_password==get_confirm_password:
            update=RoleDetails(email=session_mail,password=make_password(get_confirm_password))
            update.save(update_fields=['password'])
            return redirect("/login/")
    return render(request,'update_password.html')
