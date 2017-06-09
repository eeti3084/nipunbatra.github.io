import sys
BASIC = True

notebook_file = sys.argv[1]

from nbconvert import HTMLExporter
import nbformat

html_exporter = HTMLExporter()

if BASIC:
	html_exporter.template_file = 'basic'

nb = nbformat.reads(open(notebook_file, 'r').read(), as_version=4)

(body, resources) = html_exporter.from_notebook_node(nb)

read_navbar = open("navbar.txt", 'r').read()
read_mathjax = open("mathjax.txt", 'r').read()

read_disqus = open("disqus.txt", 'r').read()
read_css = open("bootstrap_css.txt", 'r').read()
read_ga = open("google_analytics.txt","r").read()

if BASIC:
	body = """<html>
			<head>
			<meta charset="utf-8">
		    <meta http-equiv="X-UA-Compatible" content="IE=edge">
		    <meta name="viewport" content="width=device-width, initial-scale=1">
		    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
		    <meta name="description" content="">
		    <meta name="author" content="">
		    </head>
		    <body>
		    <div class="container">"""+body+"</div></body></html>"




if read_navbar not in body:
	body = body.replace("<body>", "<body>\n" + read_navbar)

if read_ga not in body:
	body = body.replace("</body>", read_ga + "\n</body>")

if read_disqus not in body:
	body = body.replace("</body>", read_disqus + "\n</body>")

if read_mathjax not in body:
	body = body.replace("</head>", read_mathjax + "\n</head>")

if read_css not in body:
	body = body.replace("</title>", "</title>\n" + read_css)
	body = body.replace("</body>", read_css + "\n</body>")

body = body.replace("img src", "img width='100%' src")


#body = body.replace(" rendered_html", "")
body = body.replace(".rendered_html{overflow-x:auto" , ".rendered_html{overflow-x:auto;overflow-y: hidden;")
body = body.replace("#notebook{font-size:14px;line-height:20px;", "#notebook{font-size:20px;line-height:29px;")
body = body.replace("div.text_cell_render{outline:0;resize:none;width:inherit;border-style:none;padding:.5em .5em .5em .4em;color:#000;",
                    "div.text_cell_render{outline:0;resize:none;width:inherit;border-style:none;padding:.5em .5em .5em .4em;color:#777;")




html_file = notebook_file.replace(".ipynb", ".html")
html_file_writer = open(html_file, 'w')
html_file_writer.write(body)
html_file_writer.close()
