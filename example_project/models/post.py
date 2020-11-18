from example_project.components import DATABASE
from spark import models
from spark.links import all_methods


@all_methods(src=DATABASE, dst=DATABASE)
class Post(models.Model):
    pass
