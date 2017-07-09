import logging
from os import listdir
from os.path import isfile, join
try:
	from htmlmin import minify
except:
	pass

class Plugin():
	def __init__(self, settings):
		logging.debug("[Compress_html] Init")
		try:
			from htmlmin import minify
		except Exception as e:
			logging.error("[Compress_html] To use this plugin you need to install htmlmin (example: pip install htmlmin)")
			return None
		pass

	def run(self, settings, content, fields):
		pass

	def teardown(self, settings):
		logging.debug("[Compress_html] Teardown")
		onlyfiles = [f for f in listdir(settings.get("output")) if isfile(join(settings.get("output"),f)) and (f.endswith('.html') or f.endswith('.htm'))]
		for f in onlyfiles:
			logging.debug("[Compress_html] Minify => {0}".format(f))
			f = open(settings.get("output")+f, 'r+')
			f.write(minify(f.read().decode('utf8'), remove_comments=True, remove_empty_space=True, remove_all_empty_space=True, keep_pre=True).encode('utf8'))
			f.close()