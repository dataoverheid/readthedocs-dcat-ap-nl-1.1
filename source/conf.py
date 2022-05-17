# encoding: utf-8

project = u'DCAT-NL.info'
copyright = u'2018, Kennis- en Exploitatiecentrum Officiële Overheidspublicaties'
author = u'Willem ter Berg, Textinfo B.V.'
version = u''
release = u''
extensions = []
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
language = u'nl'
exclude_patterns = []
pygments_style = 'sphinx'

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'navigation_depth': 4,
    'display_version': False,
    'collapse_navigation': False
}
html_show_sourcelink = False
html_context = {
    'commit': False
}
html_static_path = ['_static']
htmlhelp_basename = 'DCAT-NLdoc'

latex_elements = {}
latex_documents = [
    (master_doc, 'DCAT-NL.tex', u'DCAT-NL Documentation', u'Kennis- en Exploitatiecentrum Officiële Overheidspublicaties', 'manual'),
]
latex_show_urls = 'footnote'

man_pages = [
    (master_doc, 'dcat-nl', u'DCAT-NL Documentation', [author], 1)
]

texinfo_documents = [
    (master_doc, 'DCAT-NL', u'DCAT-NL Documentation', author, 'DCAT-NL', 'One line description of project.', 'Miscellaneous'),
]

def setup(app):
    app.add_stylesheet('theme_override.css')
