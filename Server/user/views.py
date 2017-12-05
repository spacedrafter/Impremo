from django.contrib.auth.decorators import login_required
from django.core.checks import messages
from django.db import transaction
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from post.models import Post
from user.forms import UserForm, ProfileForm
from user.models import Profile


@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile = profile_form.instance
            profile.user = request.user
            profile.save()
            return redirect('/')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'post/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

@login_required
def profile_view(request):
    profile = get_object_or_404(Profile, pk=request.user.pk)
    posts = Post.objects.filter(user=request.user)
    count_post = posts.count()
    return render(request, 'post/profile.html', {'profile':profile, 'posts': posts, 'count_post': count_post})