from django.shortcuts import render

anime_list = [
    {'id': 1, 'name': "One Piece"},
    {'id': 2, 'name': "Your Name"},
    {'id': 3, 'name': "Garden of words"},
    {'id': 4, 'name': "Violate Evergarden"},
    {'id': 5, 'name': "To The Moon for You"},
    {'id': 6, 'name': "One Punch Man"},
]


# Create your views here.
def home(request):
    context = {'anime_list': anime_list}
    return render(request, 'NFT_Api/home.html', context)

def room(request, pk):
    room_data = None
    for anime in anime_list:
        if anime['id'] == int(pk):
            room_data = anime

    return render(request, 'NFT_Api/room.html', room_data)
