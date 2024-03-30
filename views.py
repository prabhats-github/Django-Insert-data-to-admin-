from django.shortcuts import render,HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from  .models import Res

# Create your views here.

def index(request):
    return render(request,'index.html',{})

def about(request):
    return render(request,'about.html',{})

def contact(request):
    return render(request,'contact.html',{})




def gallery(request):
    return render(request,'gallery.html',{})

def reservation(request):
    return render(request,'reservation.html',{})

def room(request):
    return render(request,'room.html',{})

def reservationData(request):
    Name = request.POST.get('name','default')
    print(Name)

    Mob=request.POST.get('mob','default')
    print(Mob)

    Email=request.POST.get('email','default')
    print(Email)

    Chkin=request.POST.get('chkin','default')
    print(Chkin)

    Chkout=request.POST.get('chkout','default')
    print(Chkout)

    Select_adults=request.POST.get('select_adults','default')
    print(Select_adults)

    Select_chld=request.POST.get('select_chld','default')
    print(Select_chld)

    Room_type=request.POST.get('room_type','default')
    print(Room_type)

    No_of_room=request.POST.get('no_of_rooms','default')
    print(No_of_room)

    
    subject = "Your (Skyline Hotel) Reservation Details is Here! Don't forgot to Thanks Prabhat"
    message = f'''Name : {Name}\n Mobile : {Mob}\n Email: {Email} \n Check_in:{Chkin} \n Check_out:{Chkout} \n Adults:{Select_adults} \n
     Total_childern:{Select_chld} \n Your_Room:{Room_type} \n Total_Rooms:{No_of_room} '''
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['priyachugh8439@gmail.com','prabhatsolanki099@gmail.com' ]
    send_mail( subject, message, email_from, recipient_list )
    return HttpResponse('thanks...')

def contactData(request):
     Name = request.POST.get('name','default')
     print(Name)

     Mob=request.POST.get('mob','default')
     print(Mob)

     Email=request.POST.get('email','default')
     print(Email)

     con = Res(name=Name,mob=Mob,email=Email)
     con.save()
     return HttpResponse('Thanks for Signup....')

    
