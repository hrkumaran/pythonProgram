from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Your list of values
    my_list = ["apple", "banana", "cherry", "date"]
    return render_template('display_list.html', items=my_list)

if __name__ == '__main__':
    app.run(debug=True)
