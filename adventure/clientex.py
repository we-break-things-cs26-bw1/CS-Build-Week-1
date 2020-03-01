from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
import requests

def get_name(request):
    response = requests.get('http://api.ipstack.com/104.32.252.209?access_key=88579c7866daa3c8c5407d91c627bdd5&format=1')
    print(response)
    geodata = response.json()
    for item in geodata:
        print(item)
    if "type" in geodata:
        print(f"yus and")
        print(geodata["type"])
    print(geodata)

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        for item in form:
            print(item)

        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            print(form.your_name)
            return render(request, 'name.html', {
                'ip': geodata['ip'],
                'country': geodata['country_name']
            })

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
    some_value ="<h1>f templates</h1>"

    final_context ={'form': form,'some_value':some_value}
    for k in geodata:
        final_context[k] =geodata[k]

    print(f" final context is {final_context}")
    return render(request, 'name.html', final_context)

class NameForm(forms.Form):
    your_name = forms.CharField(label='country', max_length=100)
