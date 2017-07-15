# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1500132089.2327423
_enable_loop = True
_template_filename = 'themes/maupassant/templates/post.tmpl'
_template_uri = 'post.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='post_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

    ns = runtime.TemplateNamespace('pheader', context._clean_inheritance_tokens(), templateuri='post_header.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'pheader')] = ns

    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        helper = _mako_get_namespace(context, 'helper')
        def content():
            return render_content(context._locals(__M_locals))
        parent = context.get('parent', UNDEFINED)
        pheader = _mako_get_namespace(context, 'pheader')
        post = context.get('post', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n')
        __M_writer('\r\n')
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def extra_head():
            return render_extra_head(context)
        helper = _mako_get_namespace(context, 'helper')
        post = context.get('post', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    ')
        __M_writer(str(parent.extra_head()))
        __M_writer('\r\n')
        if post.meta('keywords'):
            __M_writer('    <meta name="keywords" content="')
            __M_writer(filters.html_escape(str(post.meta('keywords'))))
            __M_writer('">\r\n')
        __M_writer('    <meta name="author" content="')
        __M_writer(filters.html_escape(str(post.author())))
        __M_writer('">\r\n')
        if post.prev_post:
            __M_writer('        <link rel="prev" href="')
            __M_writer(str(post.prev_post.permalink()))
            __M_writer('" title="')
            __M_writer(filters.html_escape(str(post.prev_post.title())))
            __M_writer('" type="text/html">\r\n')
        if post.next_post:
            __M_writer('        <link rel="next" href="')
            __M_writer(str(post.next_post.permalink()))
            __M_writer('" title="')
            __M_writer(filters.html_escape(str(post.next_post.title())))
            __M_writer('" type="text/html">\r\n')
        if post.is_draft:
            __M_writer('        <meta name="robots" content="noindex">\r\n')
        __M_writer('    ')
        __M_writer(str(helper.open_graph_metadata(post)))
        __M_writer('\r\n    ')
        __M_writer(str(helper.twitter_card_information(post)))
        __M_writer('\r\n    ')
        __M_writer(str(helper.meta_translations(post)))
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        helper = _mako_get_namespace(context, 'helper')
        pheader = _mako_get_namespace(context, 'pheader')
        messages = context.get('messages', UNDEFINED)
        def content():
            return render_content(context)
        post = context.get('post', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<div class="post post-page">\r\n    ')
        __M_writer(str(pheader.html_post_header()))
        __M_writer('\r\n    <div class="post-content">\r\n        ')
        __M_writer(str(post.text()))
        __M_writer('\r\n    </div>\r\n    <div class="postpromonav">\r\n        <nav>\r\n            ')
        __M_writer(str(helper.html_tags(post)))
        __M_writer('\r\n            ')
        __M_writer(str(helper.html_pager(post)))
        __M_writer('\r\n        </nav>\r\n    </div>\r\n')
        if not post.meta('nocomments') and site_has_comments:
            __M_writer('    <section class="comments hidden-print">\r\n        <h2>')
            __M_writer(str(messages("Comments")))
            __M_writer('</h2>\r\n        ')
            __M_writer(str(comments.comment_form(post.permalink(absolute=True), post.title(), post._base_path)))
            __M_writer('\r\n    </section>\r\n')
        __M_writer('    ')
        __M_writer(str(helper.mathjax_script(post)))
        __M_writer('\r\n    ')
        __M_writer(str(comments.comment_link_script()))
        __M_writer('\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "post.tmpl", "line_map": {"128": 29, "129": 31, "130": 31, "131": 35, "132": 35, "133": 36, "134": 36, "135": 39, "136": 40, "137": 41, "138": 41, "139": 42, "140": 42, "141": 45, "142": 45, "143": 45, "144": 46, "145": 46, "23": 2, "26": 3, "29": 4, "35": 0, "51": 2, "52": 3, "53": 4, "54": 5, "59": 25, "151": 145, "69": 7, "78": 7, "79": 8, "80": 8, "81": 9, "82": 10, "83": 10, "84": 10, "85": 12, "86": 12, "87": 12, "88": 13, "89": 14, "90": 14, "91": 14, "92": 14, "93": 14, "94": 16, "95": 17, "96": 17, "97": 17, "98": 17, "99": 17, "100": 19, "101": 20, "102": 22, "103": 22, "104": 22, "105": 23, "106": 23, "107": 24, "108": 24, "114": 27, "126": 27, "127": 29}, "source_encoding": "utf-8", "filename": "themes/maupassant/templates/post.tmpl"}
__M_END_METADATA
"""
