# -*- coding: utf-8 -*-
# @Time    : 2022/8/17 19:12
# @Author  : Walter
# @File    : mytags.py
# @License : (C)Copyright Walter
# @Desc    :
from django import template

register = template.Library()

class ReversalNode(template.Node):
    def __init__(self, value):
        self.value = str(value)

    def render(self, context):
        return self.value[::-1]

@register.tag(name='reversal')
def do_reversal(parse, token):
    try:
        tag_name, value = token.split_contents()

    except:
        raise template.TemplateSyntaxError('syntax')

    return ReversalNode(value)

