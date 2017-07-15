# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1500132090.9353328
_enable_loop = True
_template_filename = 'themes/maupassant/templates/gallery.tmpl'
_template_uri = 'gallery.tmpl'
_source_encoding = 'utf-8'
_exports = ['sourcelink', 'extra_head', 'extra_js', 'content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

    ns = runtime.TemplateNamespace('ui', context._clean_inheritance_tokens(), templateuri='crumbs.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'ui')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'ui')._populate(_import_ns, ['bar'])
        def sourcelink():
            return render_sourcelink(context._locals(__M_locals))
        def extra_js():
            return render_extra_js(context._locals(__M_locals))
        comments = _mako_get_namespace(context, 'comments')
        ui = _mako_get_namespace(context, 'ui')
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        photo_array_json = _import_ns.get('photo_array_json', context.get('photo_array_json', UNDEFINED))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        crumbs = _import_ns.get('crumbs', context.get('crumbs', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        enable_comments = _import_ns.get('enable_comments', context.get('enable_comments', UNDEFINED))
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        folders = _import_ns.get('folders', context.get('folders', UNDEFINED))
        thumbnail_size = _import_ns.get('thumbnail_size', context.get('thumbnail_size', UNDEFINED))
        site_has_comments = _import_ns.get('site_has_comments', context.get('site_has_comments', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n')
        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'sourcelink'):
            context['self'].sourcelink(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_js'):
            context['self'].extra_js(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sourcelink(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'ui')._populate(_import_ns, ['bar'])
        def sourcelink():
            return render_sourcelink(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'ui')._populate(_import_ns, ['bar'])
        def extra_head():
            return render_extra_head(context)
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer(str(parent.extra_head()))
        __M_writer('\r\n<link rel="alternate" type="application/rss+xml" title="RSS" href="rss.xml">\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_js(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'ui')._populate(_import_ns, ['bar'])
        thumbnail_size = _import_ns.get('thumbnail_size', context.get('thumbnail_size', UNDEFINED))
        def extra_js():
            return render_extra_js(context)
        photo_array_json = _import_ns.get('photo_array_json', context.get('photo_array_json', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\r\n<script src="/assets/js/flowr.plugin.js"></script>\r\n<script>\r\njsonContent = ')
        __M_writer(str(photo_array_json))
        __M_writer(';\r\n$("#gallery_container").flowr({\r\n        data : jsonContent,\r\n        height : ')
        __M_writer(str(thumbnail_size))
        __M_writer('*.6,\r\n        padding: 5,\r\n        rows: -1,\r\n        render : function(params) {\r\n            // Just return a div, string or a dom object, anything works fine\r\n            img = $("<img />").attr({\r\n                \'src\': params.itemData.url_thumb,\r\n                \'width\' : params.width,\r\n                \'height\' : params.height\r\n            }).css(\'max-width\', \'100%\');\r\n            link = $( "<a></a>").attr({\r\n                \'href\': params.itemData.url,\r\n                \'class\': \'image-reference\'\r\n            });\r\n            div = $("<div />").addClass(\'image-block\').attr({\r\n                \'title\': params.itemData.title\r\n            });\r\n            link.append(img);\r\n            div.append(link);\r\n            return div;\r\n        },\r\n        itemWidth : function(data) { return data.size.w; },\r\n        itemHeight : function(data) { return data.size.h; },\r\n        complete : function(params) {\r\n            if( jsonContent.length > params.renderedItems ) {\r\n                nextRenderList = jsonContent.slice( params.renderedItems );\r\n            }\r\n        }\r\n    });\r\n$("a.image-reference").colorbox({rel:"gal", maxWidth:"100%",maxHeight:"100%",scalePhotos:true});\r\n$(\'a.image-reference[href="\'+window.location.hash.substring(1,1000)+\'"]\').click();\r\n</script>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'ui')._populate(_import_ns, ['bar'])
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        def content():
            return render_content(context)
        crumbs = _import_ns.get('crumbs', context.get('crumbs', UNDEFINED))
        enable_comments = _import_ns.get('enable_comments', context.get('enable_comments', UNDEFINED))
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        folders = _import_ns.get('folders', context.get('folders', UNDEFINED))
        comments = _mako_get_namespace(context, 'comments')
        ui = _mako_get_namespace(context, 'ui')
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        site_has_comments = _import_ns.get('site_has_comments', context.get('site_has_comments', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\r\n    ')
        __M_writer(str(ui.bar(crumbs)))
        __M_writer('\r\n')
        if title:
            __M_writer('    <h1>')
            __M_writer(filters.html_escape(str(title)))
            __M_writer('</h1>\r\n')
        if post:
            __M_writer('    <p>\r\n        ')
            __M_writer(str(post.text()))
            __M_writer('\r\n    </p>\r\n')
        if folders:
            __M_writer('    <ul>\r\n')
            for folder, ftitle in folders:
                __M_writer('        <li><a href="')
                __M_writer(str(folder))
                __M_writer('"><i class="glyphicon glyphicon-folder-open"></i>&nbsp;')
                __M_writer(filters.html_escape(str(ftitle)))
                __M_writer('</a></li>\r\n')
            __M_writer('    </ul>\r\n')
        __M_writer('\r\n<div id="gallery_container"></div>\r\n')
        if site_has_comments and enable_comments:
            __M_writer(str(comments.comment_form(None, permalink, title)))
            __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "gallery.tmpl", "line_map": {"128": 39, "129": 39, "130": 42, "131": 42, "137": 7, "175": 26, "23": 3, "26": 4, "155": 8, "156": 8, "154": 7, "158": 10, "159": 10, "32": 0, "161": 12, "162": 13, "163": 14, "164": 14, "165": 17, "166": 18, "167": 19, "168": 20, "169": 20, "170": 20, "171": 20, "172": 20, "173": 22, "174": 24, "157": 9, "176": 27, "177": 27, "183": 177, "59": 2, "60": 3, "61": 4, "160": 10, "66": 5, "71": 29, "76": 34, "81": 74, "87": 5, "100": 31, "109": 31, "110": 32, "111": 32, "117": 36, "127": 36}, "source_encoding": "utf-8", "filename": "themes/maupassant/templates/gallery.tmpl"}
__M_END_METADATA
"""
