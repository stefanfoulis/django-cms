# -*- coding: utf-8 -*-
from django.db import models
from cms.models import CMSPlugin


class ReverseDescUnalteredPluginModel(CMSPlugin):
    title = models.CharField(max_length=50)
    search_fields = ['title']


class ReverseDescNoRelatedNamePluginModel(CMSPlugin):
    cmsplugin_ptr = models.OneToOneField(CMSPlugin, related_name='+', parent_link=True)
    title = models.CharField(max_length=50)
    search_fields = ['title']


class ReverseDescNoRelatedQueryNamePluginModel(CMSPlugin):
    cmsplugin_ptr = models.OneToOneField(CMSPlugin, related_query_name='+', parent_link=True)
    title = models.CharField(max_length=50)
    search_fields = ['title']


class ReverseDescCustomRelatedQueryNamePluginModel(CMSPlugin):
    cmsplugin_ptr = models.OneToOneField(CMSPlugin, related_query_name='revdesc_custom_relqn', parent_link=True)
    title = models.CharField(max_length=50)
    search_fields = ['title']


class ReverseDescCustomRelatedNamePluginModel(CMSPlugin):
    cmsplugin_ptr = models.OneToOneField(CMSPlugin, related_name='revdesc_custom_reln', parent_link=True)
    title = models.CharField(max_length=50)
    search_fields = ['title']


class ReverseDescCustomRelatedNameAndRelatedQueryNamePluginModel(CMSPlugin):
    cmsplugin_ptr = models.OneToOneField(CMSPlugin, related_name='revdesc_custom_reln2', related_query_name='revdesc_custom_relqn2', parent_link=True)
    title = models.CharField(max_length=50)
    search_fields = ['title']
