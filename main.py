from flask import Flask, render_template, jsonify

app = Flask(__name__)
JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'Bengaluru,India',
  'salary': 'Rs. 10,00,000'
}, {
  'id': 2,
  'title': 'Data Scientist',
  'location': 'Delhi,India',
  'salary': 'Rs. 12,00,000'
}, {
  'id': 3,
  'title': 'Devops Engineer',
  'location': 'Hyderabad,India',
  'salary': 'Rs. 8,00,000'
}, {
  'id': 4,
  'title': 'Forntend Analyst',
  'location': 'Kakinada,India',
  'salary': 'Rs. 20,00,000'
}, {
  'id': 5,
  'title': 'Backend Developer',
  'location': 'Newyork,USA',
  'salary': 'Rs. 17,00,000'
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS)


@app.route("/json")
def print_json():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
