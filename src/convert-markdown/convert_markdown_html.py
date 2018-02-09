# coding: UTF-8
# convert markdown to html
# in order to get module attributes(argv)
import sys
# markdown
#import markdown
import gfm

# get command line args
args = sys.argv

file_name = args[1]
print("file_name : "+file_name)

# markdown file の読み込み
f = open(file_name, 'r', encoding='utf-8')
text_md = f.read()
f.close()

print("************ markdown **************")
print(text_md)

# markdown file -> html file
#md = markdown.Markdown()
#html = md.convert(text_md)
html = gfm.markdown(text_md)

print("************ html **************")
print(html)
