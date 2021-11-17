from .models import Profile

def profile_pic(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(owner=request.user)
        pic = profile.profile_pic_url
        return {'picture':pic}
    return {}
