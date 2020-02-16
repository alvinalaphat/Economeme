from app import app
from flask_mongoengine.wtf import model_form

class User(db.Document):
    username = db.StringField(max_length=50)
    password = db.StringField(max_length=50)

# class Meme(db.Document):
#     text = db.StringField()
#     lang = db.StringField(max_length=3)
#     tags = db.ListField(db.StringField(max_length=30))
#     content = db.EmbeddedDocumentField(Content)

# PostForm = model_form(Post)

# def add_post(request):
#     form = PostForm(request.POST)
#     if request.method == 'POST' and form.validate():
#         # do something
#         redirect('done')
#     return render_template('add_post.html', form=form)