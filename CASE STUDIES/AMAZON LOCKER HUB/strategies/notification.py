from models.core import Notification

class NotificationStrategy:
    def send_notification(self, notification: Notification):
        raise NotImplementedError("This method should be overridden by subclasses")
    
    
class  EmailNotificationStrategy(NotificationStrategy):
    def send_notification(self, notification: Notification):
        print(f"Sending email notification: {notification.notification_text}")
        
class SmsNotificationStrategy(NotificationStrategy):
    def send_notification(self, notification: Notification):
        print(f"Sending SMS notification: {notification.notification_text}")
        
        
class PushNotificationStrategy(NotificationStrategy):
    def send_notification(self, notification: Notification):
        print(f"Sending push notification: {notification.notification_text}")

