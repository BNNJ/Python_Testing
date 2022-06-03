import json
from flask import Flask, render_template, request, redirect, flash, url_for


def load_clubs():
	with open('clubs.json') as c:
		 list_of_clubs = json.load(c)['clubs']
		 return list_of_clubs


def load_competitions():
	with open('competitions.json') as comps:
		 list_of_competitions = json.load(comps)['competitions']
		 return list_of_competitions


app = Flask(__name__)
app.secret_key = "something_special"

competitions = load_competitions()
clubs = load_clubs()

@app.route('/')
def index():
	return render_template('index.html')


@app.route('/showSummary', methods=['POST'])
def show_summary():
	club = next((club for club in clubs if club['email'] == request.form['email']), None)
	if club is None:
		flash("No club with this email was found")
		return redirect(url_for('index'))
	else:
		return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/book/<competition>/<club>')
def book(competition, club):
	found_club = [c for c in clubs if c['name'] == club][0]
	found_competition = [c for c in competitions if c['name'] == competition][0]
	if found_club and found_competition:
		return render_template('booking.html', club=found_club, competition=found_competition)
	else:
		flash("Something went wrong-please try again")
		return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/purchasePlaces', methods=['POST'])
def purchase_places():
	competition = next((c for c in competitions if c['name'] == request.form['competition']), None)
	club = next((c for c in clubs if c['name'] == request.form['club']), None)
	places_requested = int(request.form['places'])
	if places_requested > 12:
		flash("You can't request more than 12 places")
		return render_template("booking.html", club=club, competition=competition)
	elif places_requested > int(club['points']):
		flash("You don't have enough points to book that many places")
		return render_template("booking.html", club=club, competition=competition)
	else:
		competition['numberOfPlaces'] = int(competition['numberOfPlaces']) - places_requested
		flash("Great-booking complete!")
		return render_template('welcome.html', club=club, competitions=competitions)


# TODO: Add route for points display


@app.route('/logout')
def logout():
	return redirect(url_for('index'))