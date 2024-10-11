from flask import Flask, render_template
import csv

app = Flask(__name__)

# This data could be fetched from a database, API, or CSV file.
# Here is an example of how it might look:
def read_csv():
    participants = []
    with open('participants.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            participants.append({
                'name': row['Name'],
                'redemption_status': row['Redemption Status'],
                'profile_url': row['Cloud Skill Boost Profile'],
                'completion': row['Completion of Chapter and Arcade'],
                'chapters_completed': int(row['No. of Chapter Completed']),
                'arcades_completed': int(row['No. of Arcade Completed']),
                'arcade_completion': row['Arcade Game Completion']
            })
    return participants


@app.route('/')
def index():
    participants = read_csv()
    for participant in participants:
        if participant['chapters_completed']==15 and participant['arcades_completed']==1:
            participant['completion']='Yes'
        else:
            participant['completion']='No'
        
    # Pass the participants list to the template
    return render_template('index.html', participants=participants)

if __name__ == '__main__':
    app.run(debug=True)
