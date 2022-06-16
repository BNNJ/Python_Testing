from flask import Flask, render_template, request, redirect, flash, url_for

from utils import (
	load_clubs,
	load_competitions,
	get_item,
	date_is_past,
	purchase_error
)

app = Flask(__name__)
app.secret_key = "something_special"

clubs_file = "clubs.json"
competitions_file = "competitions.json"

competitions = load_competitions(competitions_file)
clubs = load_clubs(clubs_file)

@app.route('/')
def index():
	return render_template('index.html')


@app.route('/showSummary', methods=['POST'])
def show_summary():
	club = get_item(clubs, lambda c: c['email'] == request.form['email'])
	if club is None:
		flash("No club with this email was found")
		return redirect(url_for('index'))
	else:
		return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/book/<competition>/<club>')
def book(competition, club):
	found_club = get_item(clubs, lambda c: c['name'] == club)
	found_competition = get_item(competitions, lambda c: c['name'] == competition)

	if found_club is None or found_competition is None:
		flash("Something went wrong-please try again")
		return render_template('welcome.html', club=club, competitions=competitions)
	elif date_is_past(found_competition['date']):
		flash("This competition has already taken place")
		return render_template('welcome.html', club=club, competitions=competitions)
	else:
		return render_template('booking.html', club=found_club, competition=found_competition)


@app.route('/purchasePlaces', methods=['POST'])
def purchase_places():
	competition = get_item(competitions, lambda c: c['name'] == request.form['competition'])
	club = get_item(clubs, lambda c: c['name'] == request.form['club'])

	places_requested = int(request.form['places'])
	if err := purchase_error(places_requested, club['points']):
		flash(err)
		return render_template("booking.html", club=club, competition=competition)
	else:
		competition['numberOfPlaces'] -= places_requested
		club['points'] -= places_requested
		# save_clubs(clubs)
		# save_competitions(competitions)
		flash("Great-booking complete!")
		return render_template('welcome.html', club=club, competitions=competitions)


# TODO: Add route for points display
@app.route('/displayBoard')
def display_board():
	return render_template('display_board.html', clubs=clubs)

@app.route('/logout')
def logout():
	return redirect(url_for('index'))
	