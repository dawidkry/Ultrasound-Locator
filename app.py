from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pytz # Standard for handling timezones in clinical apps

app = Flask(__name__)

# Database configuration - creates a file named 'tracker.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tracker.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database Model: The Audit Log
class AssetLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(100), nullable=False)
    user_identity = db.Column(db.String(100), nullable=False) # Name or Bleep
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def get_local_time(self):
        # Converts UTC to local time for the display
        return self.timestamp.strftime('%H:%M | %d %b')

# Create the database file automatically
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    # Fetch the current location (the last entry)
    current_status = AssetLog.query.order_by(AssetLog.id.desc()).first()
    # Fetch the last 10 movements for the audit trail
    history = AssetLog.query.order_by(AssetLog.id.desc()).limit(10).all()
    
    return render_template('index.html', status=current_status, history=history)

@app.route('/update', methods=['POST'])
def update():
    loc = request.form.get('location')
    user = request.form.get('user_identity')
    
    if loc and user:
        new_entry = AssetLog(location=loc, user_identity=user)
        db.session.add(new_entry)
        db.session.commit()
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Set host to 0.0.0.0 so it's accessible on your local network
    app.run(host='0.0.0.0', port=5000, debug=True)
