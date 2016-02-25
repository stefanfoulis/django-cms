# -*- coding: utf-8 -*-
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from . import models


class ReverseDescUnalteredPlugin(CMSPluginBase):
    model = models.ReverseDescUnalteredPluginModel
    render_template = 'cms/content.html'
plugin_pool.register_plugin(ReverseDescUnalteredPlugin)


class ReverseDescNoRelatedNamePlugin(CMSPluginBase):
    model = models.ReverseDescNoRelatedNamePluginModel
    render_template = 'cms/content.html'
plugin_pool.register_plugin(ReverseDescNoRelatedNamePlugin)


class ReverseDescNoRelatedQueryNamePlugin(CMSPluginBase):
    model = models.ReverseDescNoRelatedQueryNamePluginModel
    render_template = 'cms/content.html'
plugin_pool.register_plugin(ReverseDescNoRelatedQueryNamePlugin)


class ReverseDescCustomRelatedQueryNamePlugin(CMSPluginBase):
    model = models.ReverseDescCustomRelatedQueryNamePluginModel
    render_template = 'cms/content.html'
plugin_pool.register_plugin(ReverseDescCustomRelatedQueryNamePlugin)


class ReverseDescCustomRelatedNamePlugin(CMSPluginBase):
    model = models.ReverseDescCustomRelatedNamePluginModel
    render_template = 'cms/content.html'
plugin_pool.register_plugin(ReverseDescCustomRelatedNamePlugin)


class ReverseDescCustomRelatedNameAndRelatedQueryNamePlugin(CMSPluginBase):
    model = models.ReverseDescCustomRelatedNameAndRelatedQueryNamePluginModel
    render_template = 'cms/content.html'
plugin_pool.register_plugin(ReverseDescCustomRelatedNameAndRelatedQueryNamePlugin)
