from django.shortcuts import render, redirect, get_object_or_404
from .forms import PersonInfoForm, PersonDeleteForm
from .models import Person
from django.contrib import messages
from django.views.decorators.http import require_http_methods
# Create your views here.


def display_all_users(request):
    users = Person.objects.all()
    return render(request, 'users.html', {'users': users})


@require_http_methods(['GET', 'POST'])
def create_user(request):
    if request.method == 'POST':
        form = PersonInfoForm(request.POST)
        # validate form and CREATE user profile
        if form.is_valid():
            cd = form.cleaned_data
            new_person = Person.objects.create(first_name=cd['first_name'], last_name=cd['last_name'],
                                               email=cd['email'], bio=cd['bio'])
            new_person.save()
            messages.success(request, 'New person account successfully created!')
            return redirect('crud_app:display_all_users', 200)
        else:
            messages.error(request, 'Invalid credentials inputted!')
    else:
        #
        form = PersonInfoForm()
        return render(request, 'create_user.html', {'form': form})


@require_http_methods(['GET', 'POST'])
def display_user(request, user_id):
    user = get_object_or_404(Person, id=user_id)
    if user:
        if request.method == 'POST':
            edit_form = PersonInfoForm(request.POST, instance=user)
            delete_form = PersonDeleteForm(request.POST)

            # validate edit_form and UPDATE user profile
            if edit_form.is_valid():
                edit_form.save()
                messages.success(request, 'Profile successfully updated!')
                return redirect('crud_app:display_all_users')

            # validate delete_form and DELETE user profile
            if delete_form.is_valid():
                cd_delete = delete_form.cleaned_data
                if cd_delete['confirm_delete']:
                    Person.objects.filter(id=user.id).delete()
                    messages.success(request, 'Profile successfully deleted.')
                    return redirect('crud_app:display_all_users')
            else:
                messages.error(request, 'Something went wrong :( Confirm inputted values and try again.')
                return redirect('crud_app:display_all_users')

        else:
            # To READ profile info
            edit_form = PersonInfoForm(instance=user)
            delete_form = PersonDeleteForm()
            return render(request, 'user_detail.html', {'user': user,
                                                        'edit_form': edit_form,
                                                        'delete_form': delete_form})

    else:
        messages.error(request, 'Sorry profile does not exist!')
        return redirect('crud_app:display_all_users', {'status': 401})


# ERROR VIEWS
def handler400(request, exception):
    return render(request, 'errors/400_bad_request.html', status=400)


def handler401(request, exception):
    return render(request, 'errors/401_unauthorized.html', status=401)


def handler403(request, exception):
    return render(request, 'errors/403_forbidden.html', status=403)


def handler404(request, exception):
    return render(request, 'errors/404_not_found.html', status=404)


def handler405(request, exception):
    return render(request, 'errors/405_method_not_allowed.html', status=405)


def handler500(request):
    return render(request, 'errors/500_internal_server_error.html', status=500)


