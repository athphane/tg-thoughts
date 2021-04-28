from datetime import datetime

from pyrogram.types import User as BaseUser

from tgthoughtsbot.database import database


class UserDB:
    def __init__(self):
        self.users = database()['users']

    def all_users(self):
        users = self.users.find()
        return users

    def all_users_with_notifications(self):
        users = self.users.find({'notification': True})
        return users

    def find_user(self, from_user: BaseUser):
        query = {
            "id": from_user.id
        }
        record = self.users.find_one(query)

        return record

    def create_user(self, from_user: BaseUser):
        data = {
            "id": from_user.id,
            "f_name": from_user.first_name,
            "l_name": from_user.last_name,
            "username": from_user.username,
            'state': None,
            'location': None,
        }
        self.users.insert_one(data)
        return self.find_user(from_user)

    def update_user(self, from_user: BaseUser):
        query = {
            "id": from_user.id,
        }

        data = {
            "f_name": from_user.first_name,
            "l_name": from_user.last_name,
            "username": from_user.username,
            "last_used": datetime.now()
        }

        new_values = {"$set": data}

        self.users.update_one(query, new_values)
        return self.find_user(from_user)

    def find_or_create(self, from_user: BaseUser):
        user = self.find_user(from_user)

        if user is None:
            self.create_user(from_user)
            user = self.find_user(from_user)

        return user

    def update_state(self, from_user: BaseUser, state):
        query = {
            "id": from_user.id,
        }

        data = {
            "state": state,
        }

        new_values = {"$set": data}

        self.users.update_one(query, new_values)

    def users_with_last_used(self):
        query = {
            "last_used": {"$exists": True}
        }

        return self.users.find(query)

    def delete(self, chat_id):
        self.users.delete_many({'id': chat_id})
