from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

insert_data = True

app = Flask(__name__)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/pintu'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    time_stamp = db.Column(db.String(200),  nullable=False)
    end_point = db.Column(db.String(200),  nullable=False)
    ip = db.Column(db.String(200),  nullable=False)

    def __init__(self, time_stamp, end_point, ip):
        self.time_stamp = time_stamp
        self.end_point = end_point
        self.ip = ip

    def __repr__(self):
        return f'<Data {self.time_stamp}, {self.end_point},{self.ip}>'


migrate = Migrate(app, db)


def add_data_object(time_stamp, end_point, ip):
    with app.app_context():
        data_object = Data(
            time_stamp=time_stamp,
            end_point=end_point,
            ip=ip
        )
        db.session.add(data_object)
        db.session.commit()


def render_file():
    file_path = 'C:\\Users\\kushw\\Desktop\\main\\error.txt'
    data = []

    # Open the file for reading
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.split(' ')
            if len(parts) > 8 and int(parts[8]) == 200:
                data.append("secure")
            else:
                data.append("error")
                if insert_data:
                    add_data_object(parts[3]+parts[4], parts[6], parts[0])

    return data


@app.route("/")
def web_api():
    # Call the render_file function to get the data
    data = render_file()
    global insert_data
    if insert_data:

        insert_data = False
    # Render an HTML template with the data
    return render_template('index.html', data=data)


if __name__ == "__main__":
    app.run(debug=True, port=80)
