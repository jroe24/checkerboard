from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def checkerboard1():
    return render_template("index.html", rows = 8, columns =8)

@app.route("/<int:num_columns>")
def checkerboard2(num_columns):
    return render_template("index.html", columns = num_columns, rows = 8)

@app.route("/<int:num_rows>/<int:num_columns>")
def checkerboard3(num_rows, num_columns):
    return render_template("index.html", rows = num_rows, columns = num_columns)





if __name__ == "__main__":
    app.run(debug = True)