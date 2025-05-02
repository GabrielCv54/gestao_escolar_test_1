from flask_restx import Resource,Namespace,fields

turma_ns = Namespace('Turmas',description='Operação relacionada as turmas')

turma_model = turma_ns.model('Turma',{
   'descricao':fields.String(required=True,description='Descrições sobre a turma '),
   'professor_id':fields.Integer(required=True,description='Id do Professor responsável pela turma'),
   'ativo':fields.Boolean(required=True,description='Situação da turma(ativa ou não)')
})

turma_output_model = turma_ns.model('TurmaOutput',{
  'id':fields.Integer(description='Id da turma'),
  'descrição':fields.String(description='Descrição sobre a turma'),
  'professor_id':fields.Integer(description='Id do professor responsável pela turma'),
  'ativo':fields.Boolean(description='Situação da turma')
})

