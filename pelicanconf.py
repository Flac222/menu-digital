# pelicanconf.py
import os
import json

AUTHOR = 'Flac222'
SITENAME = 'menu-digital'
SITEURL = ""

PATH = "content"

TIMEZONE = 'America/Argentina/Buenos_Aires'

DEFAULT_LANG = 'es'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# --- 1. CONFIGURACIÓN "HEADLESS" (Evitar cosas de blog) ---
# No queremos archvios por fecha, ni autores, ni categorias en URLs
ARCHIVES_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
TAGS_SAVE_AS = ''

# Solo generaremos las páginas que definamos explícitamente
ARTICLE_PATHS = [] # No buscamos artículos de blog
PAGE_PATHS = ['.']
"""
# Blogroll esto parece opcional a revisar
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget esto parece opcional a revisar
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)
"""
# --- 2. CONFIGURACIÓN DEL TEMA ---
THEME = 'themes/simple_menu' # Crearemos este tema simple
# Definimos que no usemos CSS de syntax highlighting de código
PYGMENTS_RST_OPTIONS = {}

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# --- 3. INYECCIÓN DE DATOS (La magia) ---
# Esta función leerá el JSON que tu GitHub Action dejará en la carpeta content
def load_menu_data():
    json_path = os.path.join(os.getcwd(), 'content', 'menu_data.json')
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        # Retorna datos dummy para que no falle en local si no tienes el archivo
        return {
            "name": "Restaurante Local (Test)",
            "categories": []
        }

# Hacemos la función disponible dentro de las plantillas HTML
JINJA_GLOBALS = {
    'get_menu': load_menu_data
}