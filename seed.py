from app import app, db
from models.artist_data import artist_list , artist_comments_list
from models.venue_data import venue_list, venue_comments_list


with app.app_context():
    try:
        print('Recreating database..')
        db.drop_all() # Removing everything from the DB
        db.create_all() # This will create the TABLES in the database.

        print("seeding our database..")


        db.session.add_all(artist_list)
        db.session.commit()

        db.session.add_all(venue_list)
        db.session.commit() # Add, commit. Like git.


        db.session.add_all(artist_comments_list)
        db.session.commit()

        db.session.add_all(venue_comments_list)
        db.session.commit()

        print("bye 👋")
    except Exception as e:
        print(e)