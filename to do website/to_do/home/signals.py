from django.db.models.signals import post_save
from .models import Project, Skills
from django.dispatch import receiver


@receiver(post_save, sender = Project)
def autoGenerateSkills(sender,instance,created,**kwargs):
    if created:
        projectdata=instance
        
        Skills.objects.create(
            name=projectdata.tech,
            description=projectdata.desc,
        )
        
    