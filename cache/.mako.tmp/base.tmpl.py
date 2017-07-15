# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1500132088.1030984
_enable_loop = True
_template_filename = 'themes/maupassant/templates/base.tmpl'
_template_uri = 'base.tmpl'
_source_encoding = 'utf-8'
_exports = ['sourcelink', 'extra_head', 'extra_js', 'content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('base', context._clean_inheritance_tokens(), templateuri='base_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'base')] = ns

    ns = runtime.TemplateNamespace('notes', context._clean_inheritance_tokens(), templateuri='annotation_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'notes')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        def sourcelink():
            return render_sourcelink(context._locals(__M_locals))
        base = _mako_get_namespace(context, 'base')
        def extra_js():
            return render_extra_js(context._locals(__M_locals))
        notes = _mako_get_namespace(context, 'notes')
        logo_url = _import_ns.get('logo_url', context.get('logo_url', UNDEFINED))
        blog_title = _import_ns.get('blog_title', context.get('blog_title', UNDEFINED))
        set_locale = _import_ns.get('set_locale', context.get('set_locale', UNDEFINED))
        search_form = _import_ns.get('search_form', context.get('search_form', UNDEFINED))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        blog_url = _import_ns.get('blog_url', context.get('blog_url', UNDEFINED))
        def content():
            return render_content(context._locals(__M_locals))
        date_fanciness = _import_ns.get('date_fanciness', context.get('date_fanciness', UNDEFINED))
        annotations = _import_ns.get('annotations', context.get('annotations', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        js_date_format = _import_ns.get('js_date_format', context.get('js_date_format', UNDEFINED))
        momentjs_locales = _import_ns.get('momentjs_locales', context.get('momentjs_locales', UNDEFINED))
        body_end = _import_ns.get('body_end', context.get('body_end', UNDEFINED))
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        content_footer = _import_ns.get('content_footer', context.get('content_footer', UNDEFINED))
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n')
        __M_writer(str(set_locale(lang)))
        __M_writer('\r\n')
        __M_writer(str(base.html_headstart()))
        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\r\n')
        __M_writer(str(template_hooks['extra_head']()))
        __M_writer('\r\n</head>\r\n<body>\r\n<div class="body_container">\r\n    <div id="header">\r\n        <div class="site-name">\r\n')
        if logo_url:
            __M_writer('            <a id="logo" href="')
            __M_writer(str(blog_url))
            __M_writer('"><img src="')
            __M_writer(str(logo_url))
            __M_writer('" alt="')
            __M_writer(filters.html_escape(str(blog_title)))
            __M_writer('"></a>\r\n')
        else:
            __M_writer('                <a id="logo" href="')
            __M_writer(str(blog_url))
            __M_writer('"><h1>')
            __M_writer(filters.html_escape(str(blog_title)))
            __M_writer('</h1></a>\r\n')
        __M_writer('        </div>\r\n\r\n        <div id="nav-menu">\r\n            <div class="bitcron_nav_container">\r\n                <div class="bitcron_nav">\r\n                    <div class="site_nav_wrap">\r\n                        <ul class="site_nav sm sm-base">\r\n                            ')
        __M_writer(str(base.html_navigation_links()))
        __M_writer('\r\n                            ')
        __M_writer(str(template_hooks['menu']()))
        __M_writer('\r\n                        </ul>\r\n                        <div class="clear clear_nav_inline_end"></div>\r\n                    </div>\r\n                </div>\r\n                <div class="clear clear_nav_end"></div>\r\n            </div>\r\n        </div>\r\n    </div>\r\n    <div id="layout">\r\n        <div class="pure-g">\r\n            <div class=" pure-u-24-24 pure-u-sm-24-24 pure-u-md-18-24 pure_cell">\r\n                <div class="content_container">\r\n                    <!--Body content-->\r\n                    <div class="row">\r\n                        ')
        __M_writer(str(template_hooks['page_header']()))
        __M_writer('\r\n                        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n                </div>\r\n                <!--End of body content-->\r\n                <div style="clear:both;height:0;"></div>\r\n            </div>\r\n        </div>\r\n\r\n        <!-- Sidebar -->\r\n\r\n        <div class=" pure-u-6-24 pure_cell">\r\n            <div id="sidebar">\r\n                <div class="widget">\r\n                    <div id="search_bar">\r\n')
        if search_form:
            __M_writer('                        ')
            __M_writer(str(search_form))
            __M_writer('\r\n')
        __M_writer('                    </div>\r\n                </div>\r\n            </div>\r\n        </div>\r\n    </div>\r\n    <div id="footer">\r\n        ')
        __M_writer(str(content_footer))
        __M_writer('\r\n        ')
        __M_writer(str(template_hooks['page_footer']()))
        __M_writer('\r\n    </div>\r\n\r\n    <!--FIXME: put these somewhere                            -->\r\n    <!--%if len(translations) > 1:-->\r\n    <!--<li>')
        __M_writer(str(base.html_translations()))
        __M_writer('</li>-->\r\n    <!--%endif-->\r\n    <!--% if show_sourcelink:-->\r\n    <!--')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'sourcelink'):
            context['self'].sourcelink(**pageargs)
        

        __M_writer('-->\r\n    <!--%endif-->\r\n    <link href="/assets/css/duoshuo.css" type="text/css" rel="stylesheet"/>\r\n    ')
        __M_writer(str(base.late_load_js()))
        __M_writer('\r\n    <script>$(\'a.image-reference:not(.islink) img:not(.islink)\').parent().colorbox({rel:"gal",maxWidth:"100%",maxHeight:"100%",scalePhotos:true});</script>\r\n    <!-- fancy dates -->\r\n    <script>\r\n    moment.locale("')
        __M_writer(str(momentjs_locales[lang]))
        __M_writer('");\r\n    fancydates(')
        __M_writer(str(date_fanciness))
        __M_writer(', ')
        __M_writer(str(js_date_format))
        __M_writer(');\r\n    </script>\r\n    <!-- end fancy dates -->\r\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_js'):
            context['self'].extra_js(**pageargs)
        

        __M_writer('\r\n')
        if annotations and post and not post.meta('noannotations'):
            __M_writer(str(notes.code()))
            __M_writer('\r\n')
        elif not annotations and post and post.meta('annotations'):
            __M_writer(str(notes.code()))
            __M_writer('\r\n')
        __M_writer(str(body_end))
        __M_writer('\r\n')
        __M_writer(str(template_hooks['body_end']()))
        __M_writer('\r\n</body>\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sourcelink(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
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
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        def extra_head():
            return render_extra_head(context)
        __M_writer = context.writer()
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_js(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        def extra_js():
            return render_extra_js(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        def content():
            return render_content(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "base.tmpl", "line_map": {"128": 86, "129": 87, "130": 88, "131": 88, "132": 89, "133": 90, "134": 90, "135": 92, "136": 92, "137": 93, "138": 93, "144": 75, "23": 2, "26": 3, "29": 0, "158": 6, "167": 6, "173": 86, "201": 187, "187": 44, "61": 2, "62": 3, "63": 4, "64": 4, "65": 5, "66": 5, "71": 8, "72": 9, "73": 9, "74": 15, "75": 16, "76": 16, "77": 16, "78": 16, "79": 16, "80": 16, "81": 16, "82": 17, "83": 18, "84": 18, "85": 18, "86": 18, "87": 18, "88": 20, "89": 27, "90": 27, "91": 28, "92": 28, "93": 43, "94": 43, "99": 44, "100": 57, "101": 58, "102": 58, "103": 58, "104": 60, "105": 66, "106": 66, "107": 67, "108": 67, "109": 72, "110": 72, "115": 75, "116": 78, "117": 78, "118": 82, "119": 82, "120": 83, "121": 83, "122": 83, "123": 83}, "source_encoding": "utf-8", "filename": "themes/maupassant/templates/base.tmpl"}
__M_END_METADATA
"""
