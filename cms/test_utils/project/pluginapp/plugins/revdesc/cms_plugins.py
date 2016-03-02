# -*- coding: utf-8 -*-
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from . import models


class RevDescUnalteredP(CMSPluginBase):
    model = models.RevDescUnalteredPM
    render_template = 'cms/content.html'
plugin_pool.register_plugin(RevDescUnalteredP)


class RevDescNoRelNmeP(CMSPluginBase):
    model = models.RevDescNoRelNmePM
    render_template = 'cms/content.html'
plugin_pool.register_plugin(RevDescNoRelNmeP)


class RevDescNoRelQNmeP(CMSPluginBase):
    model = models.RevDescNoRelQNmePM
    render_template = 'cms/content.html'
plugin_pool.register_plugin(RevDescNoRelQNmeP)


class RevDescCustomRelQNmeP(CMSPluginBase):
    model = models.RevDescCustomRelQNmePM
    render_template = 'cms/content.html'
plugin_pool.register_plugin(RevDescCustomRelQNmeP)


class RevDescCustomRelNmeP(CMSPluginBase):
    model = models.RevDescCustomRelNmePM
    render_template = 'cms/content.html'
plugin_pool.register_plugin(RevDescCustomRelNmeP)


class RevDescCustomRelNmeAndRelQNmeP(CMSPluginBase):
    model = models.RevDescCustomRelNmeAndRelQNmePM
    render_template = 'cms/content.html'
plugin_pool.register_plugin(RevDescCustomRelNmeAndRelQNmeP)
