:page: index.html
:path: settings/
:template: page.html

Plugin {{site_title}}
=====================
.. raw:: html

	<ul>
		{% for pl in plugins %}
			<li>{{pl}}</li>
		{% endfor %}
	</ul>

Paramétrage
===========
* Thème : {{theme}}
* Build différentiel : {% if diff_build %}Oui{% else %}Non{% endif %}

Paramétrage plugin blog
=======================
.. raw:: html

	<ul>
		{% for k in blog_settings %}
			<li>{{k}} : {{blog_settings[k]}}</li>
		{% endfor %}
	</ul>

Paramétrage plugin pyscss
=========================
.. raw:: html

	<ul>
		{% for k in scss_settings %}
			{% if k == "files" %}
				<li> Fichiers :
						<ul>
							{% for css,scss in scss_settings[k] %}
								<li>{{scss}} ==> {{css}}</li>
							{% endfor %}
						</ul>
				</li>
			{% else %}
				<li>{{k}} : {{scss_settings[k]}}</li>
			{% endif %}
		{% endfor %}
	</ul>	