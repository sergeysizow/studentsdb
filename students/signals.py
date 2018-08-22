# _*_ coding: utf-8 _*_
import logging
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from models.students import Student
from models.groups import Group
from models.exams import Exam


@receiver(post_save, sender=Student)
def log_student_updated_added_event(sender, **kwargs):
    """Writes information about newly added or updated student into log file"""
    logger = logging.getLogger(__name__)

    student = kwargs['instance']
    if kwargs['created']:
        logger.info("Student added: %s %s (ID: %d)", student.first_name, student.last_name, student.id)
    else:
        logger.info("Student updated: %s %s (ID: %d)", student.first_name, student.last_name, student.id)
    print sender


@receiver(post_delete, sender=Student)
def log_student_deleted_event(sender, **kwargs):
    """Writes information about deleted student into log file"""
    logger = logging.getLogger(__name__)

    student = kwargs['instance']
    logger.info("Student deleted: %s %s (ID: %d)", student.first_name, student.last_name, student.id)


@receiver(post_save, sender=Group)
def log_group_updated_added_event(sender, **kwargs):
    """Writes information about newly added or updated group into log file"""
    logger = logging.getLogger(__name__)

    group = kwargs['instance']
    if kwargs['created']:
        logger.info("Group added: name %s leader %s (ID: %d)", group.title, group.leader, group.id)
    else:
        logger.info("Group updated: name %s leader %s (ID: %d)", group.title, group.leader, group.id)
    print sender


@receiver(post_delete, sender=Group)
def log_group_deleted_event(sender, **kwargs):
    """Writes information about deleted group into log file"""
    logger = logging.getLogger(__name__)

    group = kwargs['instance']
    logger.info("Group deleted: name %s leader %s (ID: %d)", group.title, group.leader, group.id)


@receiver(post_save, sender=Exam)
def log_exam_updated_added_event(sender, **kwargs):
    """Writes information about newly added or updated group into log file"""
    logger = logging.getLogger(__name__)

    exam = kwargs['instance']
    if kwargs['created']:
        logger.info("Exam added: title %s teacher %s (Location: %d), group %s, date %s", exam.title, exam.teacher,
                    exam.location, exam.student_group_id, exam.date)
    else:
        logger.info("Exam updated: title %s teacher %s (Location: %d), group %s, date %s", exam.title, exam.teacher,
                    exam.location, exam.student_group_id, exam.date)
    print sender


@receiver(post_delete, sender=Exam)
def log_exam_deleted_event(sender, **kwargs):
    """Writes information about deleted exam into log file"""
    logger = logging.getLogger(__name__)

    exam = kwargs['instance']
    logger.info("Exam deleted: title %s teacher %s (Location: %d), group %s, date %s", exam.title, exam.teacher,
                exam.location, exam.student_group_id, exam.date)
