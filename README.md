https://www.youtube.com/watch?v=lllB-78pkDQ


pip install Flask-SQLAlchemy for installing flask alchemy
 
for installing requirement.txt => pip freeze > requirements.txt


for installing  pip install psycopg2

<!-- sudo -i -u postgres -->
<!-- psql -->

for venv


python -m venv venv


we have not insisde venv now, we need to activate




how to set up requirements.txt:


pip freeze > requirements.txt


more requirements.txt

# Possible Silly mistakes
- Adding extra space to conventions
- 'flask run' not happening. that was because I didn't rename my file to app.py whcih somehow I have done it in the file.



[//]: # (from sqlalchemy import create_engine)

[//]: # ()
[//]: # (from sqlalchemy.orm import sessionmaker)

[//]: # ()
[//]: # (from sqlalchemy_utils import database_exists, create_database)

[//]: # ()
[//]: # (from local_settings import postgresql)

[//]: # ()
[//]: # ()
[//]: # (def get_engine&#40;user,password,host,port,db&#41;:)

[//]: # ()
[//]: # (    url = f"postgresql://{user}:{passwd}@{host}:{port}/{db}")

[//]: # ()
[//]: # (    if not database_exists&#40;url&#41;:)

[//]: # ()
[//]: # (        create_database&#40;url&#41;)

[//]: # ()
[//]: # (    engine = create_engine&#40;url, pool_size=50,echo=False&#41;)

[//]: # ()
[//]: # (    return engine)


[//]: # (engine = get_engine&#40;settings['user'],)

[//]: # ()
[//]: # ( settings['passwd'],)

[//]: # ()
[//]: # ( settings['pghost'],)

[//]: # ()
[//]: # ( settings['pgport'],)

[//]: # ()
[//]: # ( settings['pgdb']&#41;)

[//]: # ()
[//]: # ()
[//]: # (engine.url)

[//]: # ()
[//]: # ()
[//]: # (def get_engine_from_settings&#40;&#41;:)

[//]: # ()
[//]: # (    keys = ['pgusers','pgpasswd','pghost','pgport','pgdb'])

[//]: # ()
[//]: # (    if not all&#40;ke in keysa for key in settings.keys&#40;&#41;&#41;:)

[//]: # ()
[//]: # (        raise&#40;'Bad config file'&#41;)

[//]: # ()
[//]: # ()
[//]: # (    return get_engine&#40;settings['user'],)

[//]: # ()
[//]: # ( settings['passwd'],)

[//]: # ()
[//]: # ( settings['pghost'],)

[//]: # ()
[//]: # ( settings['pgport'],)

[//]: # ()
[//]: # ( settings['pgdb']&#41;)

[//]: # ()
[//]: # ()
[//]: # (def get_session&#40;&#41;:)

[//]: # ()
[//]: # (    engine = get_engine_from_settings&#40;&#41;)

[//]: # ()
[//]: # (    session = sessionmaker&#40;bind=engine&#41;&#40;&#41;)

[//]: # ()
[//]: # (    return session)

[//]: # ()
[//]: # ()
[//]: # (session = get_session&#40;&#41;)

[//]: # ()
[//]: # (session)
