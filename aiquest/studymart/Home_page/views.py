from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    offering = {
       
        'slider' : {
             'slider_title': 'Welcome to StudyMart',
            'slider_subtitle': 'Your Gateway to Quality Education',
            'slider_image': 'https://images.unsplash.com/photo-1522202176988-66273c2fd55f?w=600',
            'slider_button_text': 'Explore Courses',
            'slider_button_text_one' : 'Watch Demo',
            'slider_cars' : ['car 1', 'car 2', 'car 3'],
        }
    }
    # print(offering)
    return render(request, 'Home_page/index.html', offering)