#
# import pymongo
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
#
# mydb = myclient["mydatabase"]
# # dblist = myclient.list_database_names()
#
# # if "mydatabase" in dblist:
# #   print("The database exists.")
#
# # print(myclient.list_database_names())
#
# # This is a collection.
# posts = mydb.posts
# post_data = {
#     'title': 'Python and MongoDB',
#     'name': 'Maaz Sabahuddin',
#     'contact_no': '+923442713545',
# }
#
# result = posts.insert_one(post_data)
# print("{}".format(result.inserted_id))
#
# maaz_posts = posts.find_one({'name': 'Maaz Sabahuddin'})
# print(maaz_posts)
