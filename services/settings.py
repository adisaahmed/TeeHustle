# from flask import current_app as app
#
# with app.app_context():
#     from models import Job
#     db = app.db
#
#     def populate_object(obj, ignored=[], **kwargs):
#         """ populate properties on the object 'obj' based on its match in dictionary kwargs
#         """
#         for element in kwargs.keys():
#             if element in ignored:
#                 kwargs.pop(element)
#
#         for name, value in kwargs.items():
#             if hasattr(obj, name):
#                 setattr(obj, name, value)
#
#         return obj
#
#
#     def create_request(ignored_args=["id"], **kwargs):
#         """ create job request
#         """
#         request = Job()
#         request = populate_object(request, ignored_args, **kwargs)
#
#         db.session.add(request)
#         db.session.commit()
#
#         return request
#
#
#     def delete_request(request_id):
#         """ Delete job request
#         """
#         request = Job.query.get(request_id)
#
#         if not request:
#             raise Exception("Job Request not Found")
#
#         try:
#             db.session.delete(request)
#         except Exception as e:
#             db.session.rollback()
#             print e
