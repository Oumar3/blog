# from django.db import models
# from django.contrib.contenttypes.models import ContentType
# from django.utils.translation import gettext_lazy as _

# class Permission(models.Model):
#     """
#     Modèle personnalisé pour les permissions.
#     Chaque permission est liée à un type de contenu (modèle spécifique) et possède un nom unique.
#     """
#     name = models.CharField(_("name"), max_length=255)
#     content_type = models.ForeignKey(
#         ContentType,
#         on_delete=models.CASCADE,
#         verbose_name=_("content type"),
#     )
#     codename = models.CharField(_("codename"), max_length=100)

#     class Meta:
#         verbose_name = _("permission")
#         verbose_name_plural = _("permissions")
#         unique_together = [["content_type", "codename"]]
#         ordering = ["content_type__app_label", "content_type__model", "codename"]

#     def __str__(self):
#         return f"{self.content_type} | {self.name}"

#     @staticmethod
#     def get_by_codename(codename):
#         """
#         Méthode utilitaire pour récupérer une permission par son nom de code.
#         """
#         return Permission.objects.get(codename=codename)

#     def has_permission(self, user):
#         """
#         Vérifie si un utilisateur donné possède cette permission.
#         """
#         return user.has_perm(f"{self.content_type.app_label}.{self.codename}")


# class Group(models.Model):
#     """
#     Modèle personnalisé pour les groupes.
#     Chaque groupe peut avoir plusieurs permissions associées, et chaque utilisateur peut appartenir à un ou plusieurs groupes.
#     """
#     name = models.CharField(_("name"), max_length=150, unique=True)
#     permissions = models.ManyToManyField(
#         Permission,
#         verbose_name=_("permissions"),
#         blank=True,
#     )

#     class Meta:
#         verbose_name = _("group")
#         verbose_name_plural = _("groups")

#     def __str__(self):
#         return self.name

#     def add_permission(self, permission):
#         """
#         Méthode pour ajouter une permission à ce groupe.
#         """
#         if isinstance(permission, Permission):
#             self.permissions.add(permission)

#     def remove_permission(self, permission):
#         """
#         Méthode pour retirer une permission de ce groupe.
#         """
#         if isinstance(permission, Permission):
#             self.permissions.remove(permission)

#     def has_permission(self, permission):
#         """
#         Vérifie si ce groupe possède une permission donnée.
#         """
#         return self.permissions.filter(id=permission.id).exists()

#     def get_permissions(self):
#         """
#         Retourne toutes les permissions associées à ce groupe.
#         """
#         return self.permissions.all()
