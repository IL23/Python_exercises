from datetime import datetime


class User:
    def __init__(self, name, username, e_mail):
        self.name = name
        self.username = username
        self.e_mail = e_mail
        self.reg_time = datetime.now()

    def info(self):
        return (f"""
        Full name: {self.name}
        Username: {self.username} 
        E-mail: {self.e_mail} 
        Registered at {self.reg_time}
        """)
