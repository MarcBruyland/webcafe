from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, IntegerField, FloatField
from wtforms.validators import DataRequired, URL


class CafeForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    map_url = StringField("Map URL", validators=[URL()])
    img_url = StringField("Image URL", validators=[URL()])
    location = StringField("Location", validators=[DataRequired()])
    has_sockets = BooleanField("Has sockets")
    has_toilet = BooleanField("Has toilet")
    has_wifi = BooleanField("Has wifi")
    can_take_calls = BooleanField("Can take calls")
    seats = StringField("Seats", validators=[DataRequired()])
    coffee_price = FloatField("Coffee price", validators=[DataRequired()])
    submit = SubmitField("Submit")
