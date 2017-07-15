# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1500132091.388453
_enable_loop = True
_template_filename = 'themes/maupassant/templates/index.tmpl'
_template_uri = 'index.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'content_header', 'content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='index_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

    ns = runtime.TemplateNamespace('pagination', context._clean_inheritance_tokens(), templateuri='pagination_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'pagination')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        date_format = context.get('date_format', UNDEFINED)
        front_index_header = context.get('front_index_header', UNDEFINED)
        prev_next_links_reversed = context.get('prev_next_links_reversed', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        permalink = context.get('permalink', UNDEFINED)
        current_page = context.get('current_page', UNDEFINED)
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        nextlink = context.get('nextlink', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        def content():
            return render_content(context._locals(__M_locals))
        author_pages_generated = context.get('author_pages_generated', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        prevlink = context.get('prevlink', UNDEFINED)
        index_file = context.get('index_file', UNDEFINED)
        page_links = context.get('page_links', UNDEFINED)
        def content_header():
            return render_content_header(context._locals(__M_locals))
        index_teasers = context.get('index_teasers', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        pagination = _mako_get_namespace(context, 'pagination')
        pagekind = context.get('pagekind', UNDEFINED)
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
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        index_file = context.get('index_file', UNDEFINED)
        def extra_head():
            return render_extra_head(context)
        posts = context.get('posts', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    ')
        __M_writer(str(parent.extra_head()))
        __M_writer('\r\n')
        if posts and (permalink == '/' or permalink == '/' + index_file):
            __M_writer('        <link rel="prefetch" href="')
            __M_writer(str(posts[0].permalink()))
            __M_writer('" type="text/html">\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_header():
            return render_content_header(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        date_format = context.get('date_format', UNDEFINED)
        front_index_header = context.get('front_index_header', UNDEFINED)
        prev_next_links_reversed = context.get('prev_next_links_reversed', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        current_page = context.get('current_page', UNDEFINED)
        nextlink = context.get('nextlink', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        def content():
            return render_content(context)
        author_pages_generated = context.get('author_pages_generated', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        prevlink = context.get('prevlink', UNDEFINED)
        page_links = context.get('page_links', UNDEFINED)
        def content_header():
            return render_content_header(context)
        index_teasers = context.get('index_teasers', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        pagination = _mako_get_namespace(context, 'pagination')
        pagekind = context.get('pagekind', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_header'):
            context['self'].content_header(**pageargs)
        

        __M_writer('\r\n')
        if 'main_index' in pagekind:
            __M_writer('    ')
            __M_writer(str(front_index_header))
            __M_writer('\r\n')
        if page_links:
            __M_writer('    ')
            __M_writer(str(pagination.page_navigation(current_page, page_links, prevlink, nextlink, prev_next_links_reversed)))
            __M_writer('\r\n')
        for post in posts:
            __M_writer('    <div class="post">\r\n        <h2 class="post-title"><a href="')
            __M_writer(str(post.permalink()))
            __M_writer('" >')
            __M_writer(filters.html_escape(str(post.title())))
            __M_writer('</a></h2>\r\n        <div class="post-meta">\r\n            ')
            __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
            __M_writer('\r\n        </div>\r\n        <div class="post-meta">\r\n')
            if author_pages_generated:
                __M_writer('                <a href="')
                __M_writer(str(_link('author', post.author())))
                __M_writer('">')
                __M_writer(filters.html_escape(str(post.author())))
                __M_writer('</a>\r\n')
            else:
                __M_writer('                ')
                __M_writer(filters.html_escape(str(post.author())))
                __M_writer('\r\n')
            __M_writer('        </div>\r\n        <div class="post-content">\r\n')
            if index_teasers:
                __M_writer('                ')
                __M_writer(str(post.text(teaser_only=True)))
                __M_writer('\r\n')
            else:
                __M_writer('                ')
                __M_writer(str(post.text(teaser_only=False)))
                __M_writer('\r\n')
            if not post.meta('nocomments') and site_has_comments:
                __M_writer('                <p class="commentline">')
                __M_writer(str(comments.comment_link(post.permalink(), post._base_path)))
                __M_writer('\r\n')
            __M_writer('        </div>\r\n    </div>\r\n')
        __M_writer(str(helper.html_pager()))
        __M_writer('\r\n')
        __M_writer(str(comments.comment_link_script()))
        __M_writer('\r\n')
        __M_writer(str(helper.mathjax_script(posts)))
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "index.tmpl", "line_map": {"23": 2, "141": 14, "146": 15, "147": 16, "148": 17, "149": 17, "150": 17, "151": 19, "152": 20, "153": 20, "26": 3, "155": 22, "156": 23, "29": 4, "158": 24, "159": 24, "160": 24, "161": 26, "162": 26, "35": 0, "164": 30, "165": 30, "166": 30, "167": 30, "168": 30, "169": 31, "170": 32, "171": 32, "172": 32, "173": 34, "174": 36, "157": 24, "176": 37, "177": 37, "178": 38, "179": 39, "180": 39, "181": 39, "182": 41, "183": 42, "184": 42, "185": 42, "186": 44, "187": 47, "188": 47, "189": 48, "190": 48, "191": 49, "192": 49, "65": 2, "66": 3, "67": 4, "68": 5, "198": 192, "73": 12, "175": 37, "78": 50, "163": 29, "84": 7, "94": 7, "95": 8, "96": 8, "97": 9, "98": 10, "99": 10, "100": 10, "106": 15, "154": 20, "117": 14}, "source_encoding": "utf-8", "filename": "themes/maupassant/templates/index.tmpl"}
__M_END_METADATA
"""
