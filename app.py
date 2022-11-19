from flask import Flask, render_template
import random
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    fruits_list = ['苹果', '香蕉', '榴莲', '石榴', '柳橙', '芒果', '百香果', '葡萄']
    fruits = random.sample(fruits_list, random.randrange(5, 7))
    return render_template('index.html', fruits=fruits)


if __name__ == '__main__':
    app.run(debug=True)
