import re,sys,collections
html=open(sys.argv[1],encoding='utf-8').read()
idx=open(sys.argv[2],encoding='utf-8').read().splitlines()
paper=open(sys.argv[3],encoding='utf-8').read()
pages=collections.defaultdict(set); order=[]
for ln in idx:
    m=re.match(r'p(\d+)\t(Theorem|Lemma|Proposition|Corollary) (\d+\.\d+)',ln)
    if m:
        key=(m.group(2),m.group(3)); pages[key].add(int(m.group(1)))
        if key not in order: order.append(key)
# statement boxes in html
box=re.findall(r'<div class="(thm|lem|prop|cor)"[^>]*>\s*<b>(Theorem|Lemma|Proposition|Corollary) (\d+\.\d+)[^<]*</b>\s*<span class="pg">pp?\. (\d+)',html)
seen=set(); bad=0
for cls,kind,num,pg in box:
    key=(kind,num); seen.add(key)
    if key not in pages: print('NOT IN INDEX',key,pg); bad+=1
    elif int(pg) not in pages[key]: print('PAGE MISMATCH',key,'html',pg,'index',sorted(pages[key])); bad+=1
print('statement boxes:',len(box),'problems:',bad)
ext={('Theorem','4.3'),('Lemma','2.2')}  # citations of [42] caught by the index regex
miss=[k for k in order if k not in seen and k not in ext]
print('statements in index without a box:',miss)
# equation tags
tags=sorted(set(re.findall(r'[\x5c]tag\{(\d+\.\d+)\}',html)),key=lambda s:tuple(map(int,s.split('.'))))
nt=[t for t in tags if '('+t+')' not in paper]
print('tags:',len(tags),'not found in paper text:',nt)
# page refs out of range
pgs=[int(x) for x in re.findall(r'class="pg">pp?\. (\d+)',html)]
print('page refs:',len(pgs),'max',max(pgs),'min',min(pgs))
# section headings pages
for m in re.finditer(r'<h2>(\d+)\. ([^<]+?) <span class="pg">pp?\. (\d+)',html):
    sec,title,pg=m.group(1),m.group(2),int(m.group(3))
    cand=[int(re.match(r'p(\d+)',l).group(1)) for l in idx if re.match(r'p\d+\t§'+sec+r' ',l)]
    flag='' if (cand and pg in cand) or sec=='1' else '  <-- CHECK index '+str(cand)
    print('sec',sec,pg,flag)
