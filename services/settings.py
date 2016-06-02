from populate import *

def index(**kwargs):

    application = App()

    application = populate_object(application,**kwargs)

    db.session.add(application)

    db.session.commit()
    return application

def update_index(obj_id, **kwargs):

    application = App.query.get(obj_id)

    if application is None:
        raise Exception("Application does not exist")
        
    application = populate_object(application, **kwargs)

    db.session.add(application)

    try:
        db.session.commit()
        return application
    except:
        raise Exception("Application not updated")

def delete_index(obj_id, **kwargs):

    application = App.query.get(obj_id)
    if application is None:
        raise Exception("Application does not exist")

    db.session.delete(application)

    try:
        db.session.commit()
    except:
        raise Exception("Application not deleted")