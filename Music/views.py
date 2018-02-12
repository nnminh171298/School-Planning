from django.shortcuts import render, get_object_or_404
from .models import Album, Song

def index(request):
	all_albums = Album.objects.all()
	context = {'all_albums': all_albums,}
	url = 'music/index.html'
	return render(request, url, context)

def detail(request, album_id):
	album = get_object_or_404(Album, pk = album_id)
	context = {'album': album,}
	url = 'music/detail.html'
	return render(request, url, context)

def favorite(request, album_id):
	album = get_object_or_404(Album, pk = album_id)
	try:
		selected_song = album.song_set.get(pk = request.POST['song'])
	except (KeyError, Song.DoesNotExist):
		context = {
			'album': album,
			'error_message': "You did not select a valid song" 
		}
		url = 'music/detail.html'
		return render(request, url, context)
	else:
		selected_song.is_favorite = True
		selected_song.save()
		context = {'album': album,}
		url = 'music/detail.html'
		return render(request, url, context)