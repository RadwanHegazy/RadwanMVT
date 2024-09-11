from RadwanORM.orm import RadwanORM

# connect with db
db = RadwanORM().connect(
    dbtype='sqlite3',
    config={
        'NAME' : 'default.sqlite3'
    }
)

# creating and managing your tables here
# db.create_table(<Your-Model>)
# model_manager = db.manage(<Your-Model>)
