import phonenumbers as ph
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone

number = input("Enter the number :  ") #use country code while writing the number 
number = ph.parse(number)
print(timezone.time_zones_for_number(number))
print(carrier.name_for_number(number , "end"))
print(geocoder.description_for_number(number , "en"))
