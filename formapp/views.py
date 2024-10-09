from lib2to3.fixes.fix_input import context
from .forms import StudentForm
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        "msg": "wired"
    }
    return render (request, "formapp/index.html", context, )


def bio_data_form(request):
    context = {

    }
    return render(
        request,
        "formapp/biodata.html",
        {
            "student_form": StudentForm
        }
    )
