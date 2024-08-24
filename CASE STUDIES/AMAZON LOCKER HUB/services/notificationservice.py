from strategies.notification import EmailNotificationStrategy, SmsNotificationStrategy, PushNotificationStrategy
from models.core import Notification

class NotificationService():
    def __init__(self):
        self._notification_strategies = {
            'email': EmailNotificationStrategy(),
            'sms': SmsNotificationStrategy(),
            'push': PushNotificationStrategy()
        }
        
    def send_notification(self, notification: 'Notification'):
        notification_strategy = self._notification_strategies.get(notification.notification_type)
        if notification_strategy:
            notification_strategy.send_notification(notification)
        else:
            raise ValueError(f"Invalid notification type: {notification.notification_type}")
        
        
    def create_notification(self, notification: 'Notification', notification_type='email'):
        notification.notification_type = notification_type
        return notification
    
    