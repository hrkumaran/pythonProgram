from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Sample data (a list of dictionaries)
    data = [
        {'Name': 'Alice', 'Age': 30, 'City': 'New York'},
        {'Name': 'Bob', 'Age': 25, 'City': 'Los Angeles'},
        {'Name': 'Charlie', 'Age': 35, 'City': 'Chicago'}
    ]
    return render_template('grid.html', items=data)

if __name__ == '__main__':
    app.run(debug=True)