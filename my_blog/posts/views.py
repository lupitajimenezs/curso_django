from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse

class HelloWord(View):

    def get(self, request):
        data = {
            'name': 'MARIA GUADALUPE JIMENEZ SANCHEZ',
            'years': 28,
            'codes': ['python', 'Django', 'React']
        }
        return render(
            request, 'hello_word.html',
            context=data
        )
