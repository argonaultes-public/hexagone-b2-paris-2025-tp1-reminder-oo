from abc import ABC, abstractmethod


class Contact:

    def __init__(self, email, phone):
        self.__email = email
        self.__phone = phone

    @property
    def email(self):
        return self.__email

    @property
    def phone(self):
        return self.__phone

class NotificationManager:

    def __init__(self, contact, notification = None):
        self.__contact = contact
        self.__notification = notification    

    @property
    def notification(self):
        return self.__notification

    @notification.setter
    def notification(self, value):
        self.__notification = value

    def send_message(self, message):
        self.__notification.notify(message, self.__contact)

class Notification(ABC):
    @abstractmethod
    def notify(self, message, contact):
        pass


class Email(Notification):
    def notify(self, message, contact):
        print(f'Send {message} to {contact.email}')


class SMS(Notification):
    def notify(self, message, contact):
        print(f'Send {message} to {contact.phone}')


if __name__ == '__main__':
    batman = Contact(email='batman@gotham.city', phone='010101')
    notification_manager = NotificationManager(batman)
    notification_manager.notification = SMS()

    notification_manager.send_message('Hello')
    notification_manager.notification = Email()
    notification_manager.send_message('Hello')
