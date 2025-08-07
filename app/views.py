from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from app.auth import *
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from .auth import authentication



def index(request):
    return render(request,'index.html')

def donor_register(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']
        # print(fname, contact_no, ussername)
        verify = authentication(fname, lname,  password, password1)
        if verify == "success":
            user = User.objects.create_user(username, password, password1)          #create_user
            user.first_name = fname
            user.last_name = lname
            user.save()
            messages.success(request, "Your Account has been Created.")
            return redirect("donor_log_in")
            
        else:
            messages.success(request, "Invalid Inputs!!!Try again...")
            return redirect("donor_register")
    # return HttpResponse("This is Home page")    
    return render(request, "donor_register.html", {'action' : 'donor_register'})


def donor_log_in(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Log In Successful...!")
            return redirect("donor_dashboard")
        else:
            messages.success(request, "Invalid User...!")
            return redirect("donor_log_in")
    return render(request, "donor_log_in.html", {'action': 'donor_log_in'})


@login_required(login_url="donor_log_in")
@cache_control(no_cache = True, must_revalidate = True, no_store = True)
def donor_dashboard(request):
    hospitals_data = Hospital.objects.all()
    user = request.user
    profile_icon = None  # Assuming you have a profile icon associated with each user
    if hasattr(user, 'profile'):
        profile_icon = user.profile.profile_icon.url
    return render(request, 'donor_dashboard.html', {'hospitals_data': hospitals_data})


@login_required(login_url="donor_log_in")
@cache_control(no_cache = True, must_revalidate = True, no_store = True)
def form(request):
    if request.method == "POST":
        name = request.POST['name']
        hospital_name = request.POST['hospital_name']
        organ_name = request.POST['organ_name']
        email = request.POST['email']
        phone_number = request.POST['phone']
        id_document = request.FILES['id_document']
        # healthcare_proxy = request.FILES['healthcare_proxy']
        organ_donor_card = request.FILES['organ_donor_card']
        
        # Perform input verification
        verify = input_verification(name, email)

        if verify == "success":
            # Create and save the loan application
            form = Form(
                name=name,
                hospital_name=hospital_name,
                organ_name=organ_name,
                email=email,
                # phone_number=phone_number,
                id_document=id_document,
                # healthcare_proxy=healthcare_proxy,
                organ_donor_card=organ_donor_card

            )
            form.save()
            
            # Access the generated loan_id
            generated_form_id = form.id
            print(generated_form_id)
            # You can add additional logic here, such as sending email notifications

            messages.success(request,'Form submitted successfully!')
            return redirect("donor_dashboard")
        else:
            messages.info(request,'Input verification failed. Please check your inputs.') 
            return redirect("form")

    return render(request,'form.html')



def buyer_register(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']
        # print(fname, contact_no, ussername)
        verify = authentication(fname, lname,  password, password1)
        if verify == "success":
            user = User.objects.create_user(username, password, password1)          #create_user
            user.first_name = fname
            user.last_name = lname
            user.save()
            messages.success(request, "Your Account has been Created.")
            return redirect("buyer_log_in")
            
        else:
            messages.success(request, "Invalid Inputs!!!Try again...")
            return redirect("buyer_register")
    # return HttpResponse("This is Home page")    
    return render(request, "buyer_register.html", {'action' : 'buyer_register'})


def buyer_log_in(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Log In Successful...!")
            return redirect("buyer_dashboard")
        else:
            messages.error(request, "Invalid User...!")
            return redirect("buyer_log_in")
    return render(request, "buyer_log_in.html", {'action': 'buyer_log_in'})



@login_required(login_url="buyer_log_in")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def buyer_dashboard(request):
    form_data = Form.objects.all()
    user = request.user
    profile_icon = None  # Assuming you have a profile icon associated with each user
    if hasattr(user, 'profile'):
        profile_icon = user.profile.profile_icon.url

    selected_organ = request.GET.get('organ_filter')  # Get the selected organ from the query parameters
    if selected_organ:  # If a specific organ is selected
        form_data = form_data.filter(organ_name=selected_organ)

    return render(request, 'buyer_dashboard.html', {'form_data': form_data})





def hospital_register(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        hname =  request.POST['hname']
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']
        
        # Verify input
        verify = authentication(fname, lname,  password, password1)
        if verify == "success":
            # Create user
            user = User.objects.create_user(username, password, password1)
            user.first_name = fname
            user.last_name = lname
            user.save()
            
            # Save hospital name
            Hospital.objects.create(fname=fname, lname=lname, hname=hname, email=username)
            
            messages.success(request, "Your Account has been Created.")
            return redirect("hospital_log_in")
        else:
            messages.error(request, "Invalid Inputs! Please try again.")
            return redirect("hospital_register")
    return render(request, "hospital_register.html", {'action': 'hospital_register'})



def hospital_log_in(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Log In Successful...!")
            return redirect("hospital_dashboard")
        else:
            messages.success(request, "Invalid User...!")
            return redirect("hospital_log_in")
    return render(request, "hospital_log_in.html", {'action': 'hospital_log_in'})

@login_required(login_url="hospital_log_in")
@cache_control(no_cache = True, must_revalidate = True, no_store = True)
def hospital_dashboard(request):
    show_logout = request.path == '/hospital_dashboard/'
    user = request.user
    profile_icon = None  # Assuming you have a profile icon associated with each user
    if hasattr(user, 'profile'):
        profile_icon = user.profile.profile_icon.url
    return render(request, 'hospital_dashboard.html', {'show_logout': show_logout})



# def donor_list(request):
#     form_data = Form.objects.all()
#     return render(request,'donor_list.html', {'form_data': form_data})

@login_required(login_url="hospital_log_in")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def donor_list(request):
    if request.method == 'POST':
        for key in request.POST:
            if key.startswith('accept_'):
                email = key.split('_')[1]
                Form.objects.filter(email=email).update(status='accepted')
            elif key.startswith('reject_'):
                email = key.split('_')[1]
                Form.objects.filter(email=email).update(status='rejected')
        # After updating the statuses, redirect to the same page to refresh the data
        return redirect('donor_list')  # Assuming the URL name is 'donor_list'
    else:
        form_data = Form.objects.exclude(status__in=['accepted', 'rejected'])
        context = {'form_data': form_data}
        return render(request, 'donor_list.html', context)
    

@login_required(login_url="log_in")
@cache_control(no_cache = True, must_revalidate = True, no_store = True)
def accept(request):
    donor_list = donor_list.objects.all
    donor_list.user.is_active = True
    donor_list.user.save()
    donor_list.is_approved = True
    donor_list.delete()
    messages.success(request, "Donors application accepted.")
    return redirect('donor_list')

@login_required(login_url="log_in")
@cache_control(no_cache = True, must_revalidate = True, no_store = True)
def reject(request, mess_owner_id):
    donor_list = donor_list.objects.all
    donor_list.user.is_active = False
    donor_list.user.save()
    donor_list.delete()
    messages.error(request, "Donors application rejected.")
    return redirect('donor_list')



@login_required(login_url="hospital_log_in")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def buyer_list(request):
    if request.method == 'POST':
        for key in request.POST:
            if key.startswith('accept_'):
                email = key.split('_')[1]
                Form1.objects.filter(email=email).update(status='accepted')
            elif key.startswith('reject_'):
                email = key.split('_')[1]
                Form1.objects.filter(email=email).update(status='rejected')
        # After updating the statuses, redirect to the same page to refresh the data
        return redirect('buyer_list')  # Assuming the URL name is 'buyer_list'
    else:
        form_data1 = Form1.objects.exclude(status__in=['accepted', 'rejected'])
        context = {'form_data1': form_data1}
        return render(request, 'buyer_list.html', context)
    
    
@login_required(login_url="hospital_log_in")
@cache_control(no_cache = True, must_revalidate = True, no_store = True)
def documents(request,email):
    f_form = Form.objects.get(email=email)
    print(f_form)
    context = {
        'fname': request.user.first_name,
        'f_form' : f_form,
        'email' : f_form.email,
        'id_document_url': f_form.id_document.url,
        # 'healthcare_proxy_url ': f_form.healthcare_proxy.url,
        'organ_donor_card_url': f_form.organ_donor_card.url,
        }
    return render(request, "documents.html", context)

@login_required(login_url="donor_log_in")
@cache_control(no_cache = True, must_revalidate = True, no_store = True)
def application(request):
    return render(request,'application.html')


@login_required(login_url="buyer_log_in")
@cache_control(no_cache = True, must_revalidate = True, no_store = True)
def application1(request):
    return render(request,'application1.html')


@login_required(login_url="hospital_log_in")
@cache_control(no_cache = True, must_revalidate = True, no_store = True)
def before_opt(request, email):
    if request.method == "POST":
        file = request.FILES['file']
        # Save the uploaded file along with the corresponding email
        FileDoc.objects.create(email=email, file=file)
        messages.success(request, 'File uploaded successfully!')
        return redirect("buyer_list")
    return render(request, 'before_opt.html')


@login_required(login_url="buyer_log_in")
@cache_control(no_cache = True, must_revalidate = True, no_store = True)
def view_doc(request, email):
    # Assuming FileDoc has a field named 'email' to associate it with a user
    # Get the FileDoc object associated with the provided email
    file_doc = FileDoc.objects.filter(email=email).last()

    context = {
        'file_url': file_doc.file.url if file_doc else None,  # Get the file URL or None if not found
    }

    return render(request, 'view_doc.html', context)


@login_required(login_url="buyer_log_in")
@cache_control(no_cache = True, must_revalidate = True, no_store = True)
def view_document(request, email):
    # Assuming FileDoc1 has a field named 'email' to associate it with a user
    # Get the FileDoc1 object associated with the provided email
    file_doc1 = FileDoc1.objects.filter(email=email).last()

    context = {
        'file_url': file_doc1.file.url if file_doc1 else None,  # Get the file URL or None if not found
    }

    return render(request, 'view_document.html', context)


@login_required(login_url="hospital_log_in")
@cache_control(no_cache = True, must_revalidate = True, no_store = True)
def after_opt(request, email):
    if request.method == "POST":
        file = request.FILES['file']
        # Save the uploaded file along with the corresponding email
        FileDoc1.objects.create(email=email, file=file)
        messages.success(request, 'File uploaded successfully!')
        return redirect("buyer_list")
    return render(request, 'after_opt.html')


@login_required(login_url="buyer_log_in")
@cache_control(no_cache = True, must_revalidate = True, no_store = True)
def form1(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone']
        hospital_name = request.POST['hospital_name']
        organ_name = request.POST['organ_name']
        id_document = request.FILES['id_document']
        # healthcare_proxy = request.FILES['healthcare_proxy']
        organ_donor_card = request.FILES['organ_donor_card']
        
        # Perform input verification
        verify = input_verification(name, email)

        if verify == "success":
            # Create and save the loan application
            form = Form1(
                name=name,
                email=email,
                # phone_number=phone_number,
                organ_name=organ_name,
                # hospital_name=hospital_name,
                id_document=id_document,
                # healthcare_proxy=healthcare_proxy,
                organ_donor_card=organ_donor_card

            )
            form.save()
            
            # Access the generated loan_id
            generated_form_id = form.id
            print(generated_form_id)
            # You can add additional logic here, such as sending email notifications

            messages.success(request,'Form submitted successfully!')
            return redirect("buyer_dashboard")
        else:
            messages.info(request,'Input verification failed. Please check your inputs.') 
            return redirect("form1")

    return render(request,'form1.html')


def form11(request):
    # Retrieve hospital name and organ name from URL parameters
    hospital_name = request.GET.get('hospital_name', '')
    organ_name = request.GET.get('organ_name', '')

    # Pass hospital name and organ name to the form
    return render(request, 'form1.html', {'hospital_name': hospital_name, 'organ_name': organ_name})



@login_required(login_url="hospital_log_in")
@cache_control(no_cache = True, must_revalidate = True, no_store = True)
def document1(request,email):
    f_form = Form1.objects.get(email=email)
    print(f_form)
    context = {
        'fname': request.user.first_name,
        'f_form' : f_form,
        'email' : f_form.email,
        'id_document_url': f_form.id_document.url,
        # 'healthcare_proxy_url ': f_form.healthcare_proxy.url,
        'organ_donor_card_url': f_form.organ_donor_card.url,
        }
    return render(request, "document1.html", context)


def donor(request):
    form_data = Form.objects.all()
    return render(request,'donor.html', {'form_data': form_data})


def buyer(request):
    form_data1 = Form1.objects.all()
    return render(request,'buyer.html', {'form_data1': form_data1})


def log_out(request):
    logout(request)
    messages.success(request, "Log out Successfuly...!")
    return redirect("/")

