# spark-web
A python package for instant web applications centered around models

Creating web applications from scratch takes a lot of repetitive work. You create get, post, put, and delete
for your models (sometimes, you add some more and sometimes, you don't include some), and you expect them
to do a couple different things:

- Write to a database
- Do a search
- Send a request to another API
- Expire a cache entry
- Add a cache entry
- etc.

Because of this, Spark creates a declarative development experience which makes code readable and makes
prototyping lightning fast. Error handling is built in to give users clear feedback during validation.
