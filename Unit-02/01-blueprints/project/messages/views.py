from flask import Blueprint, redirect, render_template, url_for, request
from project.messages.models import Message
from project.users.models import User
from project.messages.forms import MessageForm, DeleteForm
from project import db

messages_blueprint = Blueprint(
	'messages', __name__, template_folder = 'templates/messages')

@messages_blueprint.route('/users/<int:user_id>/messages', methods = ['GET', 'POST'])
def messages_index(user_id):
	delete_form = DeleteForm()
	user = User.query.get(user_id)
	if request.method == "POST":
		form = MessageForm(request.form)
		if form.validate():
			new_message = Message(request.form['text'], user_id)
			db.session.add(new_message)
			db.session.commit()
			return redirect(url_for('messages.messages_index', user_id = user_id))
		return render_template('messages_new.html', user=user, form=form)
	return render_template('messages/index.html', user=user, delete_form = delete_form)
		
@messages_blueprint.route('/users/<int:user_id>/messages/new')
def messages_new(user_id):
	found_user = User.query.get(user_id)
	form = MessageForm()
	return render_template('messages/new.html', user= found_user, form=form)

@messages_blueprint.route('/users/<int:user_id>/messages/<int:id>', methods=['PATCH', 'GET', 'DELETE'])
def messages_show(user_id, id):
	found_message = Message.query.get(id)
	if request.method == b'PATCH':
		form=MessageForm(request.form)
		if form.validate():
			found_message.text = request.form['text']
			db.session.add(found_message)
			db.session.commit()
			return redirect(url_for('messages.messages_index', user_id = user_id))
		return render_template('messages/edit.html', message=found_message,form=form)	
	if request.method == b'DELETE':
		delete_form=DeleteForm(request.form)
		if delete_form.validate():
			db.session.delete(found_message)
			db.session.commit()
		return redirect(url_for('messages.messages_index', user_id=user_id))
	return render_template('messages/show.html', message = found_message)	

@messages_blueprint.route('/users/<int:user_id>/messages/<int:id>/edit')
def messages_edit(user_id, id):
	found_message = Message.query.get(id)
	form=MessageForm(obj=found_message)
	delete_form = MessageForm()
	return render_template('messages/edit.html', message=found_message, form=form, delete_form=delete_form)