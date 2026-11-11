# Shared helpers for Donny's Den Elementor atomic trees
import json,subprocess
S="."
GC={"glass":"gc-c31c6a06ce7f2bd0","surface":"gc-339eb14c4041acd5","btn":"gc-8f32ec87d0c03833","quiet":"gc-bb1ab75f518dad47",
    "chip":"gc-22100acf6e43752e","room-title":"gc-7f9ae85065c71003","welcome":"gc-fb0b4ef9181d5a9c","room-line":"gc-c8d67dfe0505462c",
    "tile-title":"gc-0b854826bb4c2eb0","small":"gc-0743978c291fac68","wordmark":"gc-7926b6aa49120e4a","kicker":"gc-0ea7756694a7bb78",
    "section-label":"gc-2e4fa2d3bb6cc2c4","selected":"gc-92f75275baf81efb","pill":"gc-fcf0177aff3ffe10","pill-name":"gc-17d59cbcc180f173",
    "pill-label":"gc-25eb5d21ba842eb9","icon-btn":"gc-45a0b6f608f8db23","icon-20":"gc-cfad04170ef04e44","icon-18":"gc-7e9cecab3121a6b2","sr-only":"gc-ca86486090c6cb37"}
BG={"frontdoor":77,"living":78,"hallway":79,"screening":80,"study":81,"kitchen":82,"office":83,"backyard":84}
HG={"$$type":"font-family","value":"Figtree"}; NR={"$$type":"font-family","value":"Bricolage Grotesque"}
def pad(t,r=None,b=None,l=None):
    r=t if r is None else r; b=t if b is None else b; l=r if l is None else l
    return {"block-start":t,"inline-end":r,"block-end":b,"inline-start":l}
def pct(x): return {"size":x,"unit":"%"}
def m0(): return {"block-start":0,"inline-end":0,"block-end":0,"inline-start":0}
def mt(v): return {"block-start":v,"inline-end":0,"block-end":0,"inline-start":0}
def mb(v): return {"block-start":0,"inline-end":0,"block-end":v,"inline-start":0}
col=lambda gap,**k: {"display":"flex","flex-direction":"column","gap":gap,**k}
rowf=lambda gap,**k: {"display":"flex","flex-direction":"row","gap":gap,"align-items":"center",**k}
def styles(eid,desktop=None,tablet=None,mobile=None,hover=None):
    v=[]
    if desktop is not None: v.append({"meta":{"breakpoint":"desktop","state":None},"props":desktop})
    if tablet: v.append({"meta":{"breakpoint":"tablet","state":None},"props":tablet})
    if mobile: v.append({"meta":{"breakpoint":"mobile","state":None},"props":mobile})
    if hover: v.append({"meta":{"breakpoint":"desktop","state":"hover"},"props":hover})
    sid="s-"+eid
    return sid,{sid:{"id":sid,"type":"class","label":"local","variants":v}}
def node(eid,eltype,settings=None,d=None,t=None,m=None,h=None,kids=None,widget=None,g=()):
    n={"id":eid,"elType":"widget" if widget else eltype,"settings":dict(settings or {}),"elements":kids or []}
    if widget: n["widgetType"]=widget
    cls=[GC[x] if x in GC else x for x in g]
    if any(x is not None for x in (d,t,m,h)):
        sid,st=styles(eid,d if d is not None else {},t,m,h); n["styles"]=st; cls=[sid]+cls
    if cls: n["settings"]["classes"]={"$$type":"classes","value":cls}
    return n
def _nopad(d):
    d=dict(d or {}); d.setdefault("padding",0); return d
def box(eid,kids,d=None,t=None,m=None,g=(),tag="div",h=None):
    return node(eid,"e-flexbox",{"tag":tag},_nopad(d),t,m,h,kids,g=g)
def div(eid,kids,d=None,t=None,m=None,g=(),tag="div"):
    return node(eid,"e-div-block",{"tag":tag},_nopad(d),t,m,None,kids,g=g)
def h(eid,text,tag="h2",g=(),d=None,t=None,m=None):
    return node(eid,None,{"tag":tag,"title":text},d,t,m,widget="e-heading",g=g)
def p(eid,text,g=(),d=None,t=None,m=None,tag="p"):
    return node(eid,None,{"paragraph":text,"tag":tag},d,t,m,widget="e-paragraph",g=g)
def span(eid,text,g=(),d=None,t=None,m=None): return p(eid,text,g=g,d=d,t=t,m=m,tag="span")
def link(url,blank=False): return {"$$type":"link","value":{"destination":{"$$type":"url","value":url},"isTargetBlank":{"$$type":"boolean","value":blank}}}
def btn(eid,text,url=None,g=("btn",),d=None,t=None,m=None):
    s={"text":text}
    if url: s["link"]=link(url)
    return node(eid,None,s,d,t,m,widget="e-button",g=g)
def img(eid,att_id,d=None,t=None,m=None):
    return node(eid,None,{"image":{"$$type":"image","value":{"src":{"$$type":"image-src","value":{"id":{"$$type":"image-attachment-id","value":att_id},"url":None}},"size":{"$$type":"string","value":"full"}}}},d,t,m,widget="e-image")
def cssid(n,v): n["settings"]["_cssid"]=v; return n
def fixed(top=None,right=None,bottom=None,left=None):
    o={"position":"fixed","width":{"size":"","unit":"auto"}}
    for k,v in (("inset-block-start",top),("inset-inline-end",right),("inset-block-end",bottom),("inset-inline-start",left)):
        if v is not None: o[k]=v
    return o
def ab(name,params):
    r=subprocess.run(["sh",S+"/ab.sh",name,json.dumps(params)],capture_output=True,text=True)
    return r.stdout+r.stderr
def php(code):
    return ab("novamira/execute-php",{"code":code})
PAGES={"living":(91,"/living-room/"),"screening":(93,"/portfolio/"),"study":(94,"/blog/"),"kitchen":(95,"/shop/"),"office":(96,"/about/"),"backyard":(97,"/community/")}
