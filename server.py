import json
from datetime import datetime
from flask import Flask, render_template, request, redirect, flash, url_for

from utils import (
	load_clubs,
	load_competitions,
	save_clubs,
	save_competitions,
	get_item
)

app = Flask(__name__)
app.secret_key = "something_special"

competitions = load_competitions()
clubs = load_clubs()

@app.route('/')
def index():
	return render_template('index.html')


@app.route('/showSummary', methods=['POST'])
def show_summary():
	# club = next((club for club in clubs if club['email'] == request.form['email']), None)
	club = get_item(clubs, lambda c: c['email'] == request.form['email'])
	if club is None:
		flash("No club with this email was found")
		return redirect(url_for('index'))
	else:
		return render_template('welcome.html', club=club, competitions=competitions, clubs=clubs)


@app.route('/book/<competition>/<club>')
def book(competition, club):
	# found_club = next((c for c in clubs if c['name'] == club), None)
	found_club = get_item(clubs, lambda c: c['name'] == club)
	# found_competition = next((c for c in competitions if c['name'] == competition), None)
	found_competition = get_item(competitions, lambda c: c['name'] == competition)

	if found_club is None or found_competition is None:
		flash("Something went wrong-please try again")
		return render_template('welcome.html', club=club, competitions=competitions)
	elif datetime.strptime(found_competition['date'], "%Y-%m-%d %H:%M:%S") < datetime.now():
		flash("This competition has already taken place")
		return render_template('welcome.html', club=club, competitions=competitions)
	else:
		return render_template('booking.html', club=found_club, competition=found_competition)


@app.route('/purchasePlaces', methods=['POST'])
def purchase_places():
	# competition = next((c for c in competitions if c['name'] == request.form['competition']), None)
	competition = get_item(competitions, c['name'] == request.form['competition'])
	club = get_item(clubs, c['name'] == request.form['club'])

	places_requested = int(request.form['places'])
	if places_requested > 12:
		flash("You can't request more than 12 places")
		return render_template("booking.html", club=club, competition=competition)
	elif places_requested > int(club['points']):
		flash("You don't have enough points to book that many places")
		return render_template("booking.html", club=club, competition=competition)
	else:
		competition['numberOfPlaces'] = int(competition['numberOfPlaces']) - places_requested
		club['points'] = int(club['points']) - places_requested
		flash("Great-booking complete!")
		return render_template('welcome.html', club=club, competitions=competitions)


# TODO: Add route for points display


@app.route('/logout')
def logout():
	return redirect(url_for('index'))