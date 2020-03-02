from django.http import HttpResponse
from django.shortcuts import render

# # Create your views here.
def home_view(request, *args, **kwargs):
    print(request.user)
    my_context = {
        "my_text": "This is about us",
        "my_number": 123,
        "my_list": [123, 5123, 5555, "ADWA"]
    }
    # return HttpResponse("<h1>Hello World</h1>") # String of HTML code
    return render(request, "home.html", my_context)