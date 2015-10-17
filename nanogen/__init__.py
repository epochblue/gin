import os

__version__ = '0.6.0'
__author__ = 'Bill Israel <bill.israel@gmail.com>'

PATHS = {
    'cwd': os.getcwd(),
    'site': os.path.join(os.getcwd(), '_site'),
    'posts': os.path.join(os.getcwd(), '_posts'),
    'layouts': os.path.join(os.getcwd(), '_layouts'),
}