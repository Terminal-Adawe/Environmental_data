from analytics.models import Notifications
from analytics.models import NotificationViewer
import logging

# Get an instance of a logger
logger = logging.getLogger("django")


def insert_notification(moduleid,keyword,report_name,user):
	notif_save = Notifications(
                module=moduleid,
                message=keyword+" report: "+report_name,
                report=report_name,
                created_by_id=user.id
                )

	notif_save.save()


def insert_view_notification(user,reportid,module):
	notification = Notifications.objects.filter(report=reportid,module=module)
	logger.info("parameters are ")
	logger.info(reportid)
	logger.info(" and ")
	logger.info(module)
	logger.info(notification)

	notificationid = 0

	try:
		notificationid = notification[0].id
	except:
		logger.info(" no notification id in notifications table ")

	logger.info("Notification is ")
	logger.info(notificationid)
	logger.info("and User is ")
	logger.info(user)

	notification_viewed = NotificationViewer.objects.get_or_create(
				userid=user,
				notificationsId=notificationid,
				created_by=user
		)