from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from week6.day1.profile.profiles.profileApp.models import Profile


@receiver(post_save, sender=Profile)
def notify_new_profile(sender, instance, created, **kwargs):
    if created:
        print(f"New Profile Created: Name = {instance.name}, Email = {instance.email}")


@receiver(pre_delete, sender=Profile)
def warn_before_deleting(sender, instance, **kwargs):
    if instance.is_active:
        print(f"Warning: You are about to delete an active profile: Name = {instance.name}, Email = {instance.email}")