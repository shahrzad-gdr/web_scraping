import csv

from django.contrib import messages
from django.shortcuts import render, redirect
import requests
from django.http import HttpResponse
from bs4 import BeautifulSoup

from read_data.models import Movie


def data(url):
    # url = 'https://www.imdb.com/chart/top/'


    page_data = requests.get(url)


    page_soup = BeautifulSoup(page_data.text, 'html.parser')

    movie_titles = []
    movie_years = []
    movie_rates = []
    movie_posters = []
    movie_links = []
    movie_directors = []


    for item in page_soup.find_all('td', attrs={'class': 'posterColumn'}):
        # extract poster
        img = (item.a).img
        img_src = img['src']
        movie_posters.append(img_src)

        # extract link
        link = item.a['href']
        movie_links.append('https://www.imdb.com'+link)


    for item in page_soup.find_all('td', attrs={'class': 'titleColumn'}):
        link = item.a

        # extract title
        title = link.string
        movie_titles.append(title)

        # extract director
        director = item.a['title']
        movie_directors.append(director[:director.index('(')])

        # extract year
        year = (item.span.string).replace('(', '').replace(')', '')
        movie_years.append(int(year))


    for item in page_soup.find_all('td', attrs={'class': 'ratingColumn imdbRating'}):
        # extract rate
        rate = float(item.strong.string)
        movie_rates.append(rate)


    # merge all info to one list
    zipped_list = list(zip(movie_titles, movie_years, movie_rates, movie_directors, movie_posters, movie_links))

    # write in a csv file
    with open('data.csv', 'w', newline='') as output_file:
        writer = csv.writer(output_file, delimiter='\t')
        for item in zipped_list:
            writer.writerow([item[0], item[1], item[2], item[3], item[4], item[5]])

    return True



def home(request):
    return render(request, 'read_data/index.html')




def extract_data(request):
    try :
        data('https://www.imdb.com/chart/top/')
        messages.success(request, 'extract data successfully', 'success')

    except:
        messages.error(request, 'extract failed! please try again', 'danger')

    return redirect('index')




def read_movies(request):
    try:
        with open('data.csv') as f:
            reader = csv.reader(f, delimiter='\t')

            for item in reader:
                Movie.objects.create(
                    title=item[0],
                    year=item[1],
                    rank=item[2],
                    director=item[3],
                    poster=item[4],
                    link=item[5],
                )
            messages.success(request, 'insert data successfully', 'success')
    except:
        messages.error(request, 'insert data failed! please try again', 'danger')

        return redirect('index')
