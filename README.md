In this project, we created a Django application to extract data from the Top 250 Movies list on the IMDB website, store it in a database, and display it to the user.

To achieve this, we followed these steps:

    
  1. Firstly, we created a Django project using PyCharm.
2. Then, we added an application called 'read_data' using the command 'python
[manage.py](https://github.com/shahrzad-gdr/web_scraping/blob/master/manage.py)
startapp read_data'.
3.  We added the 'read_data' application to the 'INSTALLED_APPS' list in
'[settings.py](https://github.com/shahrzad-gdr/web_scraping/blob/master/web_scraping/settings.py)'.
4.  Next, we added a path for the 'read_data' application: 'path('', include('read_data.[urls](https://github.com/shahrzad-gdr/web_scraping/blob/master/read_data/urls.py)'))'.
5.  And then, we created a Python file called 'urls' in the 'read_data' directory.
6.  We created a model called 'movie' to store movie data such as title, director, rating, poster, and IMDB link.
7.  We registered the 'movie' model in '[admin.py](https://github.com/shahrzad-gdr/web_scraping/blob/master/read_data/admin.py)'.
8.  We ran the 'makemigrations' and 'migrate' commands.
9.  After that, we added a directory called 'templates' in the 'read_data' directory, and a subdirectory called
'[read_data](https://github.com/shahrzad-gdr/web_scraping/tree/master/read_data/templates/read_data)'
within that to add HTML files: 'web_scraping -> read_data ->
templates -> read_data'.
10.  To use Bootstrap5 and Django syntax such as {% block %} and {% include %}, we created an HTML file called '__temp' which includes a
title block, content block, and Bootstrap CSS link: 'web_scraping ->
read_data -> templates -> read_data ->
[__temp.html](https://github.com/shahrzad-gdr/web_scraping/blob/master/read_data/templates/read_data/__temp.html)'.
11.  We created another HTML file called 'index' in the path explained in item 9.
12.  Then, we created a function called 'home' to render '[index.html](https://github.com/shahrzad-gdr/web_scraping/blob/master/read_data/templates/read_data/index.html)'.
13.  We added a path to 'urlpatterns' in '[urls.py](https://github.com/shahrzad-gdr/web_scraping/blob/master/read_data/urls.py)'
to call the 'home' view.
14.  We added three links on the homepage for extracting data from the website, inserting data into the database, and displaying the
stored data using a query.
15.  We created a new function in '[views.py](https://github.com/shahrzad-gdr/web_scraping/blob/master/read_data/views.py)'
called 'extract_data' to extract data from
'[https://www.imdb.com/chart/top/](https://www.imdb.com/chart/top/)'
using the Beautiful Soup library.
16.  In this function, we wrote the data to a CSV file called '[data.csv](https://github.com/shahrzad-gdr/web_scraping/blob/master/data.csv)'
using the CSV library.
17.  We created an 'extract_data' function, using the Django built-in library 'messages' to show success or failure messages.
18.  We added a new path to 'urlpatterns' in '[urls.py](https://github.com/shahrzad-gdr/web_scraping/blob/master/read_data/urls.py)'
to call the 'extract_data' view.
19.  We created a 'read_movies' function in 'views.py' to read data from
'[data.csv](https://github.com/shahrzad-gdr/web_scraping/blob/master/data.csv)'
and insert it into the database, also showing a suitable message to
the user.
20.  We added a new path to 'urlpatterns' in ['urls.py](https://github.com/shahrzad-gdr/web_scraping/blob/master/read_data/urls.py)'
to call the 'read_movies' view.
21.  We created a 'movies' function to list the movies using a query, and the results were rendered in an HTML file called
'[all_movies.html](https://github.com/shahrzad-gdr/web_scraping/blob/master/read_data/templates/read_data/all_movies.html)'.
22.  To avoid displaying 250 records of data in a single page, we used the Django built-in library 'Paginator' to show 20 records on
each page.
23.  We added a new path to 'urlpatterns' in '[urls.py](https://github.com/shahrzad-gdr/web_scraping/blob/master/read_data/urls.py)'
to call the 'movies' view.
24.  We added a table to '[all_movies.html](https://github.com/shahrzad-gdr/web_scraping/blob/master/read_data/templates/read_data/all_movies.html)'
using Django syntax such as {% for item in list %} loop and {{
item.title }}.
25.  Finally, by clicking on each movie's poster, the user is redirected to the detailed information of that specific movie on the
IMDB website."



