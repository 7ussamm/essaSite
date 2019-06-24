from django.contrib import admin
from .models import SignUp
from .forms import SignUpForm

# Register your models here.


class SignUpAdmin(admin.ModelAdmin):
    class Meta:
        model = SignUp

    form = SignUpForm
    list_display = [
        '__str__',
        'email',
        'timestamp',
        'updated'
    ]


admin.site.register(SignUp, SignUpAdmin)
