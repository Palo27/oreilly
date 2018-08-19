
import pandas as pd
unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
mnames = ['movie_id', 'title', 'genres']

prefix = "E:/code/pydata-book/ch02/movielens/"
path_users = prefix + 'users.dat'
path_ratings = prefix + 'ratings.dat'
path_movies = prefix + 'movies.dat'

users = pd.read_table(path_users, sep='::', header=None, names=unames)
ratings = pd.read_table(path_ratings, sep='::', header=None, names=rnames)
movies = pd.read_table(path_movies, sep='::', header=None, names=mnames)


data = pd.merge(pd.merge(ratings, users), movies)

ratings_by_title = data.groupby('title').size()

active_titles = ratings_by_title.index[ratings_by_title >= 250]

mean_ratings = data.pivot_table('rating', rows='title', cols='gender', aggfunc='mean')
list(data)






