from flask import render_template
from app import app, mail
from app.models.form import EmailForm
from flask_mail import  Message


@app.route('/', methods=['POST', 'GET'])

def hello_world():
    form = EmailForm()
    if form.validate_on_submit():

        msg = Message(
            "Novo Contato",
            sender='caioagoncalves@gmail.com',
            recipients=['caioagoncalves@gmail.com'],
            body="%s, %s, %s" %(form.email.data, form.nome.data, form.telefone.data)
        )
        mail.send(msg)
    else:
        print(form.errors)
    return render_template('index.html', form=form)
