import re,sys,io
html_path,fragdir=sys.argv[1],sys.argv[2]; which=sys.argv[3:]
s=open(html_path,encoding='utf-8').read()
HEAD={
 'PART2':('<section id="s16"','<div class="part" id="part2">Part II — Sorting and table lookup <small>Paper §16–18, pp. 59–72. All results here assume the strict saving.</small></div>\n'),
 'PART3':(None,'<div class="part" id="part3">Part III — Concentrating arity on spheres <small>Paper §19–22, pp. 73–86.</small></div>\n'),
 'PART4':(None,'<div class="part" id="part4">Part IV — From arity to network volume <small>Paper §23–27, pp. 86–107. §27 proves Theorem 2.1.</small></div>\n'),
}
for name in which:
    frag=open(fragdir+'/'+name.lower()+'.html',encoding='utf-8').read().strip()
    anchor,head=HEAD[name]
    if anchor is None: frag=head+frag
    else:
        assert anchor in frag; frag=frag.replace(anchor,head+anchor,1)
    block='<!--'+name+'-BEGIN-->\n'+frag+'\n<!--'+name+'-END-->'
    b,e='<!--'+name+'-BEGIN-->','<!--'+name+'-END-->'
    if b in s: s=s[:s.index(b)]+block+s[s.index(e)+len(e):]
    else:
        assert '<!--'+name+'-->' in s; s=s.replace('<!--'+name+'-->',block,1)
    print(name,'spliced',len(frag))
open(html_path,'w',encoding='utf-8',newline='\n').write(s)
