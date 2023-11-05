from django.http import HttpResponse


def index(request):
        return HttpResponse("Hello. Youa re in the dashboard index")
