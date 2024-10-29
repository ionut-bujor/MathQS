from django.db import models

class user():
    usernameforwritten: str

class authentication():
    username_found: bool
    passwords_match : bool 
    user_loggedin: bool
