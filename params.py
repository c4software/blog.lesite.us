settings = {"site_title":"Un peu de tout, un peu de rien...", 
			"author":"Valentin Brosseau",
			"url":"http://blog.lesite.us",
			"input":"./source/",
			"output":"./output/",

			"title_as_name":True,

			"plugins":['sitemap','blog',"theme","static"],
			#"plugins":['sitemap','blog','pyscss',"theme","static"],
			
			"static_settings":"./static/",
			"theme":"./theme/valentin_new/",
			"blog_settings":{"index_page":"index","nbchar_resume":100,"nb_per_page":7},
			"scss_settings":{"files":[('main.scss','main.css'),('pygments.scss','pygments.css')],"path":"./theme/valentin/static/styles/"},

			"diff_build":True,
			"lastbuild_file":"./output/.lastbuild",
			"diff_build_db":"./output/.diff_build_db",

			"links":(
					    ('Archives', '/archives.html'),
					    ('Moi', 'http://valentinbrosseau.lesite.us/'),
					    ('Twitter', 'http://twitter.com/c4software'),
					    ('Google+', 'https://plus.google.com/104883394321573041618/about'),
					    ('Flux RSS', 'feeds/all.atom.xml')
			        )
			}