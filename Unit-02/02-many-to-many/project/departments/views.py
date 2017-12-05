from flask import redirect, render_template, request, url_for, Blueprint
from project.models import Department
from project.forms import NewEmployeeForm
from project import db

departments_blueprint = Blueprint(
    'departments',
    __name__,
    template_folder='templates'
)

