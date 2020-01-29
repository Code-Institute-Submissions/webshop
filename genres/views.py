from django.shortcuts import render
from django.contrib import messages
from .models import Genre
from records.models import Record


""" Return all Genres and the amount of records in a Genre """
def all_genres(request ):
    genres = Genre.objects.all()
    records = Record.objects.all()
    
    for genre in genres:
        for genre_item in Genre.objects.filter(record__genres=genre.id):
            if genre_item == genre:
                genre.number += 1

    return render(request, "genres.html",  {"genres": genres})
    
""" Get a records and genre using the OneToMany relationship"""
def genres_records(request, id):
    genres = Genre.objects.all()
    genre = Genre.objects.get(id=id)
    genres_records = Record.objects.filter(genres__id=id)
    
    # for genre in genres_records:
    #     if genre:
    #         messages.success(request, "success")
    #     if not genre:
    #         messages.success(request, "fail")
        
    return render(request, "genres_records.html", {"genres": genres, "genre": genre, "genres_records": genres_records})
    
