# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models


class Categories(models.Model):
    title = models.CharField(u"Заголовок", max_length=255)
    slug = models.CharField(u"Ссылка",max_length=45, blank=True, null=True)

    class Meta:
        verbose_name = u"категория"
        verbose_name_plural = u"категории"

    def __unicode__(self):
        return "%s - %s" % (self.title, self.slug)


class Post(models.Model):
    title = models.CharField(u"Название", max_length=255)
    slug = models.CharField(u"Ссылка",max_length=45, blank=True, null=True)
    category = models.ForeignKey(Categories, blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(upload_to='post/post_picture')
    text = models.TextField(u"Текст")
    display = models.BooleanField(default=True)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)

    class Meta:
        verbose_name = u"пост"
        verbose_name_plural = u"посты"

    def __unicode__(self):
        return "%s" % (self.title)
