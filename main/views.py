from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Nabila Zainina Karina Noor',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)
