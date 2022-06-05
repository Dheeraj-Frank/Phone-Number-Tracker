from tkinter import *
import phonenumbers
from phonenumbers import carrier
from tkinter import ttk,messagebox
from phonenumbers import geocoder
from phonenumbers import timezone
from timezonefinder import TimezoneFinder
from geopy.geocoders import Nominatim
from datetime import datetime
import requests
import pytz

root=Tk()
root.title("Phone Number Tracker")
root.geometry("365x584")
root.resizable(False,False)

def track():
    try: 
        enter_number=entry.get()
        number=phonenumbers.parse(enter_number)
        #country
        locate=geocoder.description_for_number(number,'en')
        country.config(text=locate)

        #operator like Idea, Airtel, Jio and many other
        operator=carrier.name_for_number(number,'en')
        sim.config(text=operator)

        #phone timezone
        time=timezone.time_zones_for_number(number)
        zone.config(text=time)

        #longitude and latitude
        geolocator=Nominatim(user_agent="geoapiexercises")
        location= geolocator.geocode(locate)

        lng=location.longitude
        lat=location.latitude
        longitude.config(text=lng)
        latitude.config(text=lat)

        #time showing in phone
        obj= TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude,lat=location.latitude)

        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%I:%M:%p")
        clock.config(text=current_time)
    except Exception as e:
        messagebox.showerror("Phone Number Tracker","Invalid entry !!")    

#logo
logo=PhotoImage(file="logo image.png")
Label(root,image=logo).place(x=240,y=70)
Heading=Label(root,text="TRACK NUMBER",font=("arial",15,"bold"))
Heading.place(x=90,y=110)

#entry
Entry_back=PhotoImage(file="search png.png")
Label(root,image=Entry_back).place(x=20,y=190)

entry=StringVar()
enter_number=Entry(root,textvariable=entry,width=17,bd=0,font=("arial",20),justify="center")
enter_number.place(x=50,y=220)

#button
Search_image=PhotoImage(file="search.png")
search=Button(image=Search_image,borderwidth=0,cursor="hand2",bd=0,font=("arial",16),command=track)
search.place(x=35,y=300)

#bottom box
Box=PhotoImage(file="bottom png.png")
Label(root,image=Box).place(x=-2,y=355)

label1=Label(root,text="Country",font=("Helvetica",15,"bold"),fg="white",bg="#57adff")
label1.place(x=50,y=400)

label1=Label(root,text="SIM",font=("Helvetica",15,"bold"),fg="white",bg="#57adff")
label1.place(x=200,y=400)

label1=Label(root,text="TimeZone",font=("Helvetica",15,"bold"),fg="white",bg="#57adff")
label1.place(x=50,y=450)

label1=Label(root,text="Phone Time",font=("Helvetica",15,"bold"),fg="white",bg="#57adff")
label1.place(x=200,y=450)

label1=Label(root,text="Longitude",font=("Helvetica",15,"bold"),fg="white",bg="#57adff")
label1.place(x=50,y=500)

label1=Label(root,text="Latitude",font=("Helvetica",15,"bold"),fg="white",bg="#57adff")
label1.place(x=200,y=500)


country=Label(root,text="...",bg="#57adff",fg="black",font=("arial",10,"bold"))
country.place(x=50,y=425)

sim=Label(root,text="...",bg="#57adff",fg="black",font=("arial",10,"bold"))
sim.place(x=200,y=425)

zone=Label(root,text="...",bg="#57adff",fg="black",font=("arial",10,"bold"))
zone.place(x=50,y=475)

clock=Label(root,text="...",bg="#57adff",fg="black",font=("arial",10,"bold"))
clock.place(x=200,y=475)

longitude=Label(root,text="...",bg="#57adff",fg="black",font=("arial",10,"bold"))
longitude.place(x=50,y=525)

latitude=Label(root,text="...",bg="#57adff",fg="black",font=("arial",10,"bold"))
latitude.place(x=200,y=525)


root.mainloop()

