from app import app, db
# //from models.language_data import languages_list, comments_list
# from models.user_data import user_list

with app.app_context():
    try:
        print('Recreating database..')
        db.drop_all() # Removing everything from the DB
        db.create_all() # This will create the TABLES in the database.

        print("seeding our database..")


        # db.session.add_all(user_list)
        # db.session.commit()

        # db.session.add_all(languages_list)
        # db.session.commit() # Add, commit. Like git.


        # db.session.add_all(comments_list)
        # db.session.commit()


        print("bye 👋")
    except Exception as e:
        print(e)