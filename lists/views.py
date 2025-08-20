from django.shortcuts import redirect, render
from .models import Item

# Create your views here.
def home_page(request):
    if request.method == "POST":
        print(request.POST["item_text"], "request.POST['item_text']!")
        Item.objects.create(text=request.POST["item_text"])
        return redirect("/")
    items = Item.objects.all()
    return render(
        request,
        "home.html",
        {"items": items}
        )