from flask import render_template
from app import app
from app.forms import SearchForm
from flask import request
import pandas as pd

def film_info1(df, string):
	print(string)
	df=df[df['Title'].str.contains("(?i)"+string.lower())]  
	results={}
	results["title"]=df['Title'].values
	results["year"]=df['year'].values
	results["rating"]=df['rating'].values
	results["movieId"]=df['movieId'].values
	return results


@app.route('/')
@app.route('/index')
def index():	
	form=SearchForm()
	return render_template('index.html', title="NetFlask", form=form)
	


@app.route('/searchResult')
def searchResult():
	form=SearchForm()
	film = request.args.get('FilmName')
	
	df=pd.read_csv("app/static/csv/df_movies1.csv")
	df.dropna(inplace=True)
	films=film_info1(df, film)	
	
	return render_template('searchResult.html', title="search Result", form=form, search=films)

@app.route('/film')
def film():
	form=SearchForm()
	idfilm = request.args.get('id')	
	df=pd.read_csv("app/static/csv/df_movies1.csv")	
	data=df[df.movieId==int(idfilm)].to_dict('records')[0]	
	recofilm=df.loc[:5, :].to_dict('records')
	reconav=df.loc[5:10, :].to_dict('records')		
	return render_template('film.html', title="Info on {}".format(data["Title"]), form=form, data=data, recofilm=recofilm, reconav=reconav)
