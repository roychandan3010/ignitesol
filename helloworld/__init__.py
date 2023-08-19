from flask import Flask, render_template, request

def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # a simple page that says hello
    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/hello', methods=['GET'])
    def hello():
        language = request.args.get("language")
        msgText = ""
        id = 0
        if language == "Hindi":
            msgText = "Namastey sansar"
            id = 1
        elif language == "English":
            msgText = "Hello world"
            id = 2
        elif language == "French":
            msgText = "Bonjour le monde"
            id = 3
        else:
            msgText = "The requested language is not supported"

            error_message = {"error_message": msgText}
            return error_message, 400

        message = {"id": id, "msgText": msgText}
        message = {"message": message}
        return message, 200

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0')
