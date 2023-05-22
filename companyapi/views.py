from django.http import HttpResponse,JsonResponse

def home_page(request):
    print("home page requested")
    thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
  }
    return JsonResponse(thisdict, safe=False)