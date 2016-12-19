import os
def ext_change(fn,ext):
    return os.path.splitext(fn)[0] + ext

import markdown
import mdx_gfm
mdext = mdx_gfm.GithubFlavoredMarkdownExtension()

test = ""

import codecs
import re
def md2html_file(mdfn,stylesheet):
    infile = codecs.open(mdfn, mode="r", encoding="utf-8")
    htmlfrag = markdown.markdown(
        infile.read(),
        output_format="html5",
        tab_length=2,
        extensions=[mdext, "markdown.extensions.footnotes"]
        )
    infile.close()
    # href="*.md" -> href="*.html"
    htmlfrag = re.sub(r"(?<=href\=\")https://github\.com/(?P<usr>.+)/(?P<repo>.+)/blob/master/(?P<mdn>.+)\.md(?=\")",
                      r"https://\g<usr>.github.io/\g<repo>/\g<mdn>.html",
                      htmlfrag)
    htmlfrag = re.sub(r"(?<=href\=\")(?P<mdn>[^:]*)\.md(?=\")",
                      r"\g<mdn>.html",
                      htmlfrag)
    template ="""<!doctype html>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<!--title-->
<!--css-->\n
"""
    h1search = re.search(r"<h1>(?P<h1text>.+)</h1>",htmlfrag)
    if(h1search):
        title = "<title>"+h1search.group("h1text")+"</title>"
    else:
        title = ""
    if(stylesheet):
        link = '<link href="'+stylesheet+'" rel="stylesheet" type="text/css"/>'
    else:
        link = ""
    template_custom = template.replace("<!--title-->",title).replace("<!--css-->",link)
    outfile = codecs.open(ext_change(mdfn,".html"),mode="w",encoding="utf-8")
    outfile.write(template_custom + htmlfrag)
    outfile.close()

import sys
import glob
if __name__ == "__main__":
    if (len(sys.argv)>1):
        if (len(sys.argv)>2):
            css = sys.argv[2]
        else:
            css = None
        if (sys.argv[1].find("*")>-1):
            mdlist = glob.glob("*.md")
        else:
            mdlist = [sys.argv[1]]
        for i in mdlist:
            md2html_file(i, css)
