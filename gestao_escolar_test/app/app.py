import os
from .views.aluno_view import aluno_blueprint
from .views.docente_view import docentes_blueprint
from .views.turma_view import turmas_blueprint
from .config import app,db


app.register_blueprint(aluno_blueprint)
app.register_blueprint(docentes_blueprint)
app.register_blueprint(turmas_blueprint)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)