# import datetime
# import pymongo
# from mongoengine import *
# # connect('my_database', host='localhost', port=27017)
# client = pymongo.MongoClient("mongodb://localhost:27017/")
# db = client.Learn
#
# student_data = [
#     {'_id': 1, 'name': 'Sameer', 'subjects': ['OOP', 'Data Mining'], 'CGPA': 3.23},
#     {'_id': 3, 'name': 'Bushra', 'subjects': ['OOP', 'DS'], 'CGPA': 3.9}
# ]
#
# # update_student =
# print(db.student.estimated_document_count())
# documents = db.student.find()
#
# for i in documents:
#     print(i)
#
# # try:
# #     update_many = db.student.update_many(
# #         {},
# #         [{'$set': {'CGPA': {'$trunc': ['$CGPA', 2]}}}]
# #     )
# #     print(update_many)
# #
# # except Exception as e:
# #     print(str(e))
#
# documents = db.student.find()
# for i in documents:
#     print(i)
# # insert_many = db.student.insert_many(student_data)
# # print(insert_many)
