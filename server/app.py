from flask import Flask

app = Flask(__name__,
            static_url_path='',
            template_folder='../client/build',
            static_folder='../client/build')


@app.route('/api/hello')
def hello():
    return {'message': 'Hello, from Flask!'}


if __name__ == '__main__':
    app.run(debug=True, port=5555)
