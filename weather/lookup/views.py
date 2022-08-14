from django.shortcuts import render
import json
import requests


# Create your views here.
def home(request):

    if request.method == "POST":
        # TODO do post stuff
        zipcode = request.POST['zipcode']
        print(zipcode)
        api_request = requests.get(
            f"https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode={zipcode}&distance=1&API_KEY=C74D6264-C090-414A-A1A3-4D8C57DF21F4")
        # https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=1&API_KEY=C74D6264-C090-414A-A1A3-4D8C57DF21F4
        print(api_request)
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."
        print(api)
        category_description = ""
        category_color = ""
        if not api:
            api = "Error..."
        elif api[0]["Category"]["Name"] == "Good":
            category_description = "(0-50) Minimal Impact"
            category_color = "good"
        elif api[0]["Category"]["Name"] == "Moderate":
            category_description = "(51-100) May cause minor breathing discomfort to sensitive people."
            category_color = "moderate"
        elif api[0]["Category"]["Name"] == "Unhealthy for Sensitive Groups":
            category_description = "(101-150) May cause breathing discomfort to people with lung disease such as asthma, and discomfort to people with heart disease, children and older adults."
            category_color = "usg"
        elif api[0]["Category"]["Name"] == "Unhealthy":
            category_description = "(151-200) May cause breathing discomfort to people on prolonged exposure, and discomfort to people with heart disease"
            category_color = "unhealthy"
        elif api[0]["Category"]["Name"] == "Very Unhealthy":
            category_description = "(201-300) May cause respiratory illness to the people on prolonged exposure. Effect may be more pronounced in people with lung and heart diseases."
            category_color = "veryunhealthy"
        elif api[0]["Category"]["Name"] == "Hazardous":
            category_description = "(301-500) May cause respiratory impact even on healthy people, and serious health impacts on people with lung/heart disease. The health impacts may be experienced even during light physical activity"
            category_color = "hazardous"
        return render(request, 'home.html',
                  {'api': api, 'category_description': category_description, 'category_color': category_color})

    else:
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=1&API_KEY=C74D6264-C090-414A-A1A3-4D8C57DF21F4")
        # https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=1&API_KEY=C74D6264-C090-414A-A1A3-4D8C57DF21F4
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."
        print(api)
        if api[0]["Category"]["Name"] == "Good":
            category_description = "(0-50) Minimal Impact"
            category_color = "good"
        elif api[0]["Category"]["Name"] == "Moderate":
            category_description = "(51-100) May cause minor breathing discomfort to sensitive people."
            category_color = "moderate"
        elif api[0]["Category"]["Name"] == "Unhealthy for Sensitive Groups":
            category_description = "(101-150) May cause breathing discomfort to people with lung disease such as asthma, and discomfort to people with heart disease, children and older adults."
            category_color = "usg"
        elif api[0]["Category"]["Name"] == "Unhealthy":
            category_description = "(151-200) May cause breathing discomfort to people on prolonged exposure, and discomfort to people with heart disease"
            category_color = "unhealthy"
        elif api[0]["Category"]["Name"] == "Very Unhealthy":
            category_description = "(201-300) May cause respiratory illness to the people on prolonged exposure. Effect may be more pronounced in people with lung and heart diseases."
            category_color = "veryunhealthy"
        elif api[0]["Category"]["Name"] == "Hazardous":
            category_description = "(301-500) May cause respiratory impact even on healthy people, and serious health impacts on people with lung/heart disease. The health impacts may be experienced even during light physical activity"
            category_color = "hazardous"
    return render(request, 'home.html', {'api': api, 'category_description':category_description, 'category_color':category_color})


def about(request):
    return render(request, 'about.html', {})
