# -*- coding: utf-8 -*-
#
# aws-cli documentation build configuration file, created by
# sphinx-quickstart on Fri Feb  1 12:57:38 2013.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath('.'))

import bootstrapdocs

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['notfound.extension',]
notfound_context = {
    'title': 'Page not found',
    'body': '<h1>Page not found</h1>\n\n'
            'Sorry, the page you requested could not be found.'
}
notfound_pagename = '_404'
# notfound.extension changes all the relative links to links like
# "/en/latest/_static/**" and we use "notfound_default_language" key
# to change “en” to our path prefix
notfound_default_language = os.environ.get(
    'DOCS_STATIC_PATH',
    'v2/documentation/api'
)

# For local 404.html testing uncomment lines below and put in local path
# to the build folder on your disk

# notfound_default_language = '<local path to build folder>/build'
# notfound_default_version = 'html'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'AWS CLI Command Reference'
copyright = u'2018, Amazon Web Services'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '2.0'
# The full version, including alpha/beta/rc tags.
release = '2.17.56'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:

# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['examples']

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'guzzle_sphinx_theme.GuzzleStyle'
#pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#html_theme = 'pyramid'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
# html_theme_options = {
#     'bodyfont': '"Andale Mono", Courier, monospace;'
#     }

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = ['.']

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = "AWS CLI %s Command Reference" % release

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
html_sidebars = {
  '**': ['sidebarlogo.html',
         'localtoc.html',
         'searchbox.html',
         'feedback.html',
         'userguide.html']
}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'aws-clidoc'

# Adds an HTML table visitor to apply Bootstrap table classes
html_translator_class = 'guzzle_sphinx_theme.HTMLTranslator'
p = os.path.abspath('.')
p = os.path.join(p, 'guzzle_sphinx_theme')
html_theme_path = [p]
html_theme = 'guzzle_sphinx_theme'
# Register the theme as an extension to generate a sitemap.xml
extensions.append("guzzle_sphinx_theme")

html_theme_options = {
    # Set the name of the project to appear in the nav menu
    "project_nav_name": "AWS CLI Command Reference",
    # Set your GitHub user and repo to enable GitHub stars links
    "github_user": "aws",
    "github_repo": "aws-cli",
    # Set to true to bind left and right key events to turn the page
    "bind_key_events": False,
    # Specify a base_url used to generate sitemap.xml links. If not
    # specified, then no sitemap will be built.
    "base_url": "http://docs.aws.amazon.com/cli/latest/",
}



# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('index', 'aws-cli.tex', u'AWS CLI Documentation',
   u'Amazon Web Services', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).

man_pages = [('reference/index', 'aws', 'The main command', '', 1),
             ('reference/autoscaling/index', 'aws-autoscaling',
              'The autoscaling service', '', 1),
             ('reference/cloudformation/index', 'aws-cloudformation',
              'AWS CloudFormation', '', 1),
             ('reference/cloudwatch/index', 'aws-cloudwatch',
              'Amazon CloudWatch', '', 1),
             ('reference/datapipeline/index', 'aws-datapipeline',
              'AWS Data Pipeline', '', 1),
             ('reference/directconnect/index', 'aws-directconnect',
              'AWS Direct Connect', '', 1),
             ('reference/dynamodb/index', 'aws-dynamodb',
              'Amazon DynamoDB', '', 1),
             ('reference/ec2/index', 'aws-ec2',
              'Amazon Elastic Compute Cloud', '', 1),
             ('reference/elasticache/index', 'aws-elasticache',
              'Amazon ElastiCache', '', 1),
             ('reference/elasticbeanstalk/index', 'aws-elasticbeanstalk',
              'AWS Elastic Beanstalk', '', 1),
             ('reference/elastictranscoder/index', 'aws-elastictranscoder',
              'Amazon Elastic Transcoder', '', 1),
             ('reference/elb/index', 'aws-elb',
              'Elastic Load Balancing', '', 1),
             ('reference/emr/index', 'aws-emr',
              'Amazon Elastic MapReduce', '', 1),
             ('reference/iam/index', 'aws-iam',
              'AWS Identity and Access Management', '', 1),
             ('reference/importexport/index', 'aws-importexport',
              'AWS Import/Export', '', 1),
             ('reference/opsworks/index', 'aws-opsworks',
              'AWS OpsWorks', '', 1),
             ('reference/rds/index', 'aws-rds',
              'Amazon Relational Database Service', '', 1),
             ('reference/redshift/index', 'aws-redshift',
              'Amazon Redshift', '', 1),
             ('reference/route53/index', 'aws-route53',
              'Amazon Route 53', '', 1),
             ('reference/s3/index', 'aws-s3',
              'Amazon Simple Storage Service', '', 1),
             ('reference/ses/index', 'aws-ses',
              'Amazon Simple Email Service', '', 1),
             ('reference/sns/index', 'aws-sns',
              'Amazon Simple Notification Service', '', 1),
             ('reference/sqs/index', 'aws-sqs',
              'Amazon Simple Queue Service', '', 1),
             ('reference/storagegateway/index', 'aws-storagegateway',
              'AWS Storage Gateway', '', 1),
             ('reference/sts/index', 'aws-sts',
              'AWS Security Token Service', '', 1),
             ('reference/support/index', 'aws-support',
              'AWS Support', '', 1),
             ('reference/swf/index', 'aws-swf',
              'Amazon Simple Workflow Service', '', 1),
             ]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output ------------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = []


# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'
