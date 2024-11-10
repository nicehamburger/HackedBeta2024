from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    events = [
        {"name": "HACKED BETA 2024", "date": "November 9-10", "time": "Not Specified", "location": "DICE 8TH FLOOR", "food": "Not Specified", "registration": "Unknown"},
        {"name": "CHEME COMPE MECE PRESENTS CHOMPE BAKE SALE", "date": "October 15th & 16th", "time": "10AM-2PM", "location": "ETLC Atrium", "food": "Yes", "registration": "Not Specified"},
        {"name": "FALL SGM!", "date": "September 25th", "time": "5 PM", "location": "DICE 8-207", "food": "Yes", "registration": "Free"},
        {"name": "Nursing + Engineering BOARD GAME MIXER", "date": "November 6th", "time": "4:30-8", "location": "SUB: Cascade Room", "food": "Yes", "registration": "Free"},
        {"name": "NURSING + ENGINEERING BOARD GAME MIXER", "date": "November 6th", "time": "4:30-8", "location": "Cascade Room (lower level of SUB)", "food": "Yes", "registration": "Pre-registration recommended, drop-ins welcome"},
        {"name": "Canadian Engineering Leadership Conference (CELC)", "date": "January 1st-7th, 2025", "time": "Not Specified", "location": "University of New Brunswick, Fredericton", "food": "Not Specified", "registration": "Not Specified"},
        {"name": "2024-2025 ANNUAL GENERAL SURVEY", "date": "Not Specified", "time": "Not Specified", "location": "Not Specified", "food": "Not Specified", "registration": "Not Specified"},
        {"name": "LIMITED EDITION ENGINEERING PAPER", "date": "Not Specified", "time": "Not Specified", "location": "GEER Store", "food": "Not Specified", "registration": "Not Specified"},
        {"name": "ESS Halloween DUCK Scavenger Hunt", "date": "Oct. 28 - Oct. 31", "time": "Not Specified", "location": "5 Engineering Buildings and Engg Quad", "food": "Not Specified", "registration": "Not Specified"},
        {"name": "Y2Q2 GAME NIGHT", "date": "November 7th, 2024", "time": "5:00-7:30PM", "location": "GEER LOUNGE MEC E STH FLOOR", "food": "Yes", "registration": "Drop-in"},
    ]
    return render_template('index.html', events=events)

if __name__ == '__main__':
    app.run(debug=True)
