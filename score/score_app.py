"""This is docstring"""

from flask import *
from score.score import *
APP = Flask(__name__)
import cProfile

@APP.route('/')
def score_teams():
    """This is docstring"""
    return render_template('index.html', new_score=new_score)

if __name__ == '__main__':
    cProfile.run('APP.run(debug=True)', sort='time')
