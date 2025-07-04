from django.shortcuts import render,HttpResponse
import json
import requests

# Create your views here.
def weather(request):
    data = {}
    if request.method == 'POST':
        city = request.POST.get('city')
        api_key = "de0e3ce0d060544639bd947c0780d078"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"

        response = requests.get(url)
        if response.status_code == 200:
            list_of_data = response.json()
            data = {
                "country_code": list_of_data['sys']['country'],
                "coordinates": f"{list_of_data['coord']['lon']} {list_of_data['coord']['lat']}",
                "temperature": f"{list_of_data['main']['temp']} °C",
                "humidity": f"{list_of_data['main']['humidity']}%",
                "city": city,
            }
        else:
            data['error'] = "City not found. Please try again."
            
    return render(request, 'weather.html', data)