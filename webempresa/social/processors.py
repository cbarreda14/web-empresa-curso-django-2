from .models import Link
def ctx_dict(request):
    ctx = {}
    Links = Link.objects.all()
    for link in Links:
        ctx[link.key] = link.url
    return ctx