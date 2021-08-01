from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import Observation
from .forms import ObservationForm
from django.contrib import messages


# Create your views here.
def observations_list(request):
    observations = Observation.objects.all()
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
    return render(request, 'birdnotes/observations/edit.html', {'edit_form': edit_form})


def remove_observation(request, id):
    observation = get_object_or_404(Observation, id=id)
    if request.method == 'POST' and 'remove' in request.POST:
        messages.success(request, 'Successfully removed bird observation!')
        observation.delete()
        return redirect('birdnotes:observations_list')
    elif request.method == 'POST' and 'cancel' in request.POST:
        return redirect(observation)
    return render(request, 'birdnotes/observations/remove.html', {})
