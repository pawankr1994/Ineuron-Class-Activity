from flask import Flask, request
import mysql.connector as conn

app = Flask(__name__)

@app.route('/testrun')
def test():
    get_name = request.args.get('get_name')
    mobile_number = request.args.get('mobile')
    mail_id = request.args.get('mail_id')

    return 'this is my first function for get {} {} {}'.format(get_name,mobile_number,mail_id)


;/


if __name__=='__main__':
    app.run(port = 5002)