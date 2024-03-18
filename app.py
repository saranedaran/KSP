from flask import Flask, request, render_template, send_from_directory
import csv
import os

app = Flask(__name__)

# Create a directory to store uploaded files
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# CSV file path
CSV_FILE = os.path.join(app.config['UPLOAD_FOLDER'], 'data.csv')

# Function to append data to CSV file
def append_to_csv(data):
    with open(CSV_FILE, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload_csv', methods=['POST'])
def upload_csv():
    # Get form data from the POST request
    district_name = request.form['districtName']
    unit_name = request.form['unitName']
    fir_no = request.form['firNo']
    ri = request.form['ri']
    year = request.form['year']
    month = request.form['month']
    offence_from_date = request.form['offenceFromDate']
    offence_to_date = request.form['offenceToDate']
    fir_reg_date_time = request.form['firRegDateTime']
    fir_date = request.form['firDate']
    victim_count = request.form['victimCount']
    accused_count = request.form['accusedCount']
    arrested_male = request.form['arrestedMale']
    arrested_female = request.form['arrestedFemale']
    arrested_count = request.form['arrestedCount']
    serial_no = request.form['serialNo']
    accused_charge_sheeted_count = request.form['accusedChargeSheetedCount']
    conviction_count = request.form['convictionCount']
    fir_id = request.form['firID']
    unit_id = request.form['unitID']
    crime_no = request.form['crimeNo']

    # Prepare the data to be saved in CSV format
    csv_data = [
        district_name, unit_name, fir_no, ri, year, month,
        offence_from_date, offence_to_date, fir_reg_date_time, fir_date,
        victim_count, accused_count, arrested_male, arrested_female,
        arrested_count, serial_no, accused_charge_sheeted_count,
        conviction_count, fir_id, unit_id, crime_no
    ]

    # Append the data to the CSV file
    append_to_csv(csv_data)

    return 'Data stored in CSV successfully'



@app.route('/uploads/<filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
