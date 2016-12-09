import os
def ext_change(fn,ext):
    return os.path.splitext(fn)[0] + ext

import markdown
import mdx_gfm
mdext = mdx_gfm.GithubFlavoredMarkdownExtension()

import codecs
import re
def md2html_file(mdfn,stylesheet):
    infile = codecs.open(mdfn, mode="r", encoding="utf-8")
    htmlfrag = markdown.markdown(
        infile.read(),
        output_format="html5",
        tab_length=2
        )
    infile.close()
    template ="""<!doctype html>
<meta charset="utf-8">
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
if __name__ == "__main__":
    if (len(sys.argv)>1):
        if (len(sys.argv)>2):
            css = sys.argv[2]
        else:
            css = None
        md2html_file(sys.argv[1], css)
        

#import glob
#mdlist = glob.glob("*.md")
