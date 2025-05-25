# models/__init__.py

# Import your models here to make them accessible when the 'models' package is imported.
# This also helps in ensuring SQLAlchemy registers them.
from .user import User

# If you add more models in the future, like Post, Comment, etc., import them here too:
# from .post import Post
# from .comment import Comment

# You can define an __all__ variable if you want to control what `from models import *` imports,
# though it's not strictly necessary for SQLAlchemy registration.
__all__ = ["User"]
