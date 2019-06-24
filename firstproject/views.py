from django.http import HttpResponse


def profile(request):

    return HttpResponse("You are already logged in as '_ {} _'".format(request.user))
