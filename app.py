from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # This data could be fetched from a database, API, or CSV file.
    # Here is an example of how it might look:
    participants = [
        {
            'name': 'VIVEK JETANI',
            'redemption_status': 'Done',
            'profile_url': 'https://cloud.google.com/profile/vivek',
            'completion': 'No!',
            'chapters_completed': 5,
            'arcades_completed': 1,
            'arcade_completion': 'Completed'
        },
        {
            'name': 'JANE DOE',
            'redemption_status': 'Pending',
            'profile_url': 'https://cloud.google.com/profile/jane',
            'completion': 'Yes!',
            'chapters_completed': 3,
            'arcades_completed': 2,
            'arcade_completion': 'Pending'
        },
        # Add more participants dynamically here
    ]

    # Pass the participants list to the template
    return render_template('index.html', participants=participants)

if __name__ == '__main__':
    app.run(debug=True)
