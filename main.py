from flask import Flask
from flask import render_template
from game_of_life import GameOfLife


app = Flask(__name__)


@app.route("/")
def index():
    GameOfLife(25, 25)
    return render_template("index.html")

@app.route("/live")
def life():
    life = GameOfLife()
    life.form_new_generation()
    return render_template("live.html", life = life.world, old_life = life.old_world, generation = life.generation)


if __name__ == '__main__':
    app.run(debug=True)