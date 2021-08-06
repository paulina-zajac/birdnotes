from django.shortcuts import render, get_object_or_404, redirect
from .models import Observation
from .forms import ObservationForm, UserRegistrationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



@login_required
def observations_list(request):
    object_lists = Observation.objects.all()
    paginator = Paginator(object_lists, 6)
    page = request.GET.get('page')
    try:
        observations = paginator.page(page)
    except PageNotAnInteger:
        observations = paginator.page(1)
    except EmptyPage:
        observations = paginator.page(paginator.num_pages)
    return render(request, 'birdnotes/observations/list.html', {'observations': observations})


def observation_detail(request, year, month, day, observation):
    observation = get_object_or_404(Observation, slug=observation, time__year=year, time__month=month,
                                    time__day=day)
    return render(request, 'birdnotes/observations/detail.html', {'observation': observation})


def add_observation(request):
    if request.method == 'POST':
        form = ObservationForm(request.POST, request.FILES)
        if form.is_valid():
            observation = form.save(commit=False)
            observation.person = request.user
            observation.save()
            messages.success(request, 'Successfully added new bird observation!')
            return redirect(observation)
    else:
        form = ObservationForm()
    return render(request, 'birdnotes/observations/add_observation.html', {'form': form})


def edit_observation(request, id):
    if request.method == "POST":
        observation = get_object_or_404(Observation, id=id)
        edit_form = ObservationForm(request.POST, request.FILES, instance=observation)
        if edit_form.is_valid():
            edit_form.save()
            return redirect(observation)
    else:
        observation = get_object_or_404(Observation, id=id)
        edit_form = ObservationForm(instance=observation)
    return render(request, 'birdnotes/observations/edit.html', {'edit_form': edit_form, 'observation': observation})


def remove_observation(request, id):
    observation = get_object_or_404(Observation, id=id)
    if request.method == 'POST' and 'remove' in request.POST:
        messages.success(request, 'Successfully removed bird observation!')
        observation.delete()
        return redirect('birdnotes:observations_list')
    elif request.method == 'POST' and 'cancel' in request.POST:
        return redirect(observation)
    return render(request, 'birdnotes/observations/remove.html', {})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password2'])
            new_user.save()
            return render(request, 'birdnotes/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'birdnotes/register.html', {'user_form': user_form})


def landing(request):
    return render(request, 'birdnotes/landing.html', {})