# Scrapy settings for blackwidow project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

import os


# BOT_NAME = 'BlackWidow'
# WEBSITE = 'heelsfetishism.com'
# USER_AGENT = '%s/2.0 (%s)' % (BOT_NAME, WEBSITE)

SPIDER_MODULES = ['blackwidow.spiders', ]
NEWSPIDER_MODULE = 'blackwidow.spiders'

DEFAULT_ITEM_CLASS = 'blackwidow.items.HeelsItem'

# set False to print to stdout
LOG_STDOUT = False

ITEM_PIPELINES = [
    'blackwidow.pipelines.DefaultValuePipeline',
    'blackwidow.pipelines.DuplicatePipeline',
    'blackwidow.pipelines.NormalizationPipeline',
    'blackwidow.pipelines.SubmitItemPipeline',
    # 'scrapy.contrib.pipeline.images.ImagesPipeline',
]

# http://doc.scrapy.org/en/latest/topics/images.html
if 'scrapy.contrib.pipeline.images.ImagesPipeline' in ITEM_PIPELINES:
    PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    IMAGES_STORE = os.path.join(PROJECT_PATH, 'images')
    IMAGES_MIN_WIDTH = 450

try:
    from settings_prod import *
except ImportError:
    pass
