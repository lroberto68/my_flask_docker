from flask import Blueprint, render_template
from flask.views import MethodView

main_bp = Blueprint("main", __name__)

class HomeView(MethodView):
    def get(self):
        return render_template("home.html", title="Home")

main_bp.add_url_rule("/", view_func=HomeView.as_view("home"))
