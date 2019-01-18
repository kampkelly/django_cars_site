from django.shortcuts import render


def check_for_empty_fields(func):
    def inner(request):
        success = True
        for x in request.POST:
            if request.POST[x] or x == 'submit':
                pass
            else:
                success = False
        if success:
            return func(request)
        else:
            return render(request, 'cars/car/create.html', {'error_message': 'The input fields cannot be empty!'})
    return inner
