from abc import ABC, abstractmethod

# Abstract class
class NotificationSender(ABC):

    @abstractmethod
    def send(self, message, recipient):
        pass

    @abstractmethod
    def validate_recipient(self, recipient):
        pass


# Email Notification
class EmailSender(NotificationSender):

    def validate_recipient(self, recipient):
        return "@" in recipient

    def send(self, message, recipient):
        if self.validate_recipient(recipient):
            print(f"Email sent to {recipient}: {message}")
        else:
            print("Invalid Email Address")


# SMS Notification
class SMSSender(NotificationSender):

    def validate_recipient(self, recipient):
        return recipient.isdigit()

    def send(self, message, recipient):
        if self.validate_recipient(recipient):
            print(f"SMS sent to {recipient}: {message}")
        else:
            print("Invalid Phone Number")


# Push Notification
class PushNotificationSender(NotificationSender):

    def validate_recipient(self, recipient):
        return True  # Always valid (for demo)

    def send(self, message, recipient):
        print(f"Push Notification: {message}")


# Factory Class
class NotificationFactory:

    @staticmethod
    def get_sender(notification_type):
        if notification_type == "email":
            return EmailSender()
        elif notification_type == "sms":
            return SMSSender()
        elif notification_type == "push":
            return PushNotificationSender()
        else:
            raise ValueError("Invalid Notification Type")


# Main Program
type1 = input("Enter notification type (email/sms/push): ").lower()
recipient = input("Enter recipient: ")
message = input("Enter message: ")

sender = NotificationFactory.get_sender(type1)
sender.send(message, recipient)