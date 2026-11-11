exec(open("./dd.py").read())
import copy
t122=json.load(open(S+"/data/coming-soon-template.json"))["data"]["content"]
form=copy.deepcopy([e for e in t122[1]["elements"][0]["elements"] if e["id"]=="soon-form-wrap"][0]["elements"][0])
form["id"]="lk-form"; form["settings"].update({"form_id":"links-signup","button_text":"Join the list","success_message":"You're on the list. See you at the door."})
BODY={"font-family":HG,"font-size":15,"font-weight":"500","color":"#F6F1EA","margin":m0()}
# background: porch photo, fixed
bg=cssid(div("lk-bg",[img("lk-bg-img",BG["frontdoor"],d={"width":pct(100),"height":pct(100),"object-fit":"cover","display":"block"})],
    d={**fixed(0,0,0,0),"overflow":"hidden","z-index":0,"background":{"color":"#1D1814"}}),"dd-bg")
def label(eid,text): return p(eid,text,g=("section-label",),d={"margin":{"block-start":26,"inline-end":0,"block-end":10,"inline-start":0},"text-align":"start","align-self":"stretch"})
LINKS=[("discord","Join the Discord","The community hangout","https://discord.gg/Uddm8bZRHv"),
       ("youtube","YouTube","@donnellsray","https://www.youtube.com/@donnellsray"),
       ("tiktok","TikTok","@donnellsray","https://www.tiktok.com/@donnellsray"),
       ("instagram","Instagram","@donnellsray","https://www.instagram.com/donnellsray/"),
       ("twitch","Twitch","@donnythaman","https://www.twitch.tv/donnythaman"),
       ("linkedin","LinkedIn","Donnell Ray","https://www.linkedin.com/in/donnellray/"),
       ("github","GitHub","AI builds","https://github.com/donnellsray"),
       ("benable","Benable","Things I recommend","https://benable.com/donnellsray")]
rows=[node(f"lk-link-{k}","e-flexbox",{"tag":"a","link":link(u,True)},{**rowf(12),"justify-content":"space-between","min-height":58,"padding":pad(12,20),"width":pct(100)},
           h={"background":{"color":"#FFFFFF1F"}},
           kids=[span(f"lk-link-{k}-name",n,d=BODY),span(f"lk-link-{k}-handle",s,g=("small",),d={"font-size":13,"text-align":"end"})],g=("surface",)) for k,n,s,u in LINKS]
grid={"elType":"widget","widgetType":"loop-grid","id":"lk-work-grid","elements":[],"settings":{
    "template_id":"150","post_query_post_type":"project","posts_per_page":8,"columns":"2","columns_tablet":"2","columns_mobile":"2",
    "column_gap":{"unit":"px","size":10},"row_gap":{"unit":"px","size":10},"equal_height":"yes",
    "enable_nothing_found_message":"yes","nothing_found_message_text":"New work is on the way. Check back soon.",
    "nothing_found_message_color":"#F6F1EAB3","nothing_found_message_typography_typography":"custom","nothing_found_message_typography_font_family":"Figtree",
    "nothing_found_message_typography_font_size":{"unit":"px","size":14},"nothing_found_message_align":"center"}}
panel=cssid(div("lk-panel",[
    node("lk-wordmark",None,{"tag":"span","title":"Donny's Den","link":link("/")},None,widget="e-heading",g=("wordmark",)),
    img("lk-avatar",170,d={"width":96,"height":96,"object-fit":"cover","display":"block","border-radius":999,"margin":mt(18),"border-width":2,"border-style":"solid","border-color":"#F2D39B66"}),
    h("lk-name","Donnell Ray","h1",d={"font-family":NR,"font-size":32,"font-weight":"600","color":"#F6F1EA","margin":mt(14),"line-height":{"size":1.1,"unit":"em"}},t={"font-size":28}),
    p("lk-bio","Technologist and Creator.",g=("room-line",),d={"text-align":"center","margin":mt(6)}),
    p("lk-bio-2","These are the stories from the Den.",g=("room-line",),d={"text-align":"center","margin":mt(2)}),
    label("lk-list-label","Get on the list"),
    div("lk-form-wrap",[form],d={"width":pct(100)}),
    p("lk-note","No spam. One letter when the doors open, then only when the light's on.",g=("small",),d={"text-align":"center","margin":mt(8)}),
    cssid(node("lk-links-toggle","e-flexbox",{"tag":"button"},{**rowf(12),"justify-content":"space-between","min-height":58,"padding":pad(12,20),"width":pct(100),"margin":mt(26)},
        h={"background":{"color":"#FFFFFF1F"}},
        kids=[span("lk-links-toggle-name","All my links",d={**BODY,"font-size":16,"flex":{"$$type":"flex","value":{"flexGrow":{"$$type":"number","value":1},"flexShrink":{"$$type":"number","value":1},"flexBasis":{"$$type":"size","value":{"size":0,"unit":"px"}}}},"text-align":"start"}),
              div("lk-links-toggle-end",[span("lk-links-count",f"{len(LINKS)} links",g=("small",),d={"font-size":13}),
                  cssid(node("lk-links-chev",None,{"svg":{"$$type":"svg-src","value":{"id":None,"url":{"$$type":"url","value":"https://donnysden.1wp.site/wp-content/uploads/dd-icons/next.svg"}}}},widget="e-svg",g=("icon-18",)),"dd-links-chev")],
                  d={**rowf(10),"width":{"size":"","unit":"auto"},"justify-content":"flex-end"})],g=("surface",)),"dd-links-toggle"),
    cssid(div("lk-links",rows,d={**col(10),"width":pct(100),"margin":mt(10)}),"dd-links-list"),
    label("lk-work-label","Featured Content"),
    div("lk-work",[grid],d={"width":pct(100)}),
    div("lk-foot",[p("lk-business","Business inquiries: donnellsraymgmt@gmail.com",g=("small",),d={"text-align":"center"}),
                   node("lk-doorbell",None,{"paragraph":"Ring the doorbell","tag":"p","link":link("mailto:donnellsraymgmt@gmail.com")},{"font-family":HG,"font-size":14,"color":"#E9DCC6","margin":m0(),"text-decoration":"underline"},widget="e-paragraph")],
        d={**col(8),"align-items":"center","width":pct(100),"margin":mt(28),"padding":{"block-start":18,"inline-end":0,"block-end":0,"inline-start":0},
           "border-width":{"$$type":"border-width-v2","value":{"block-start":{"$$type":"size","value":{"size":1,"unit":"px"}},"inline-end":{"$$type":"size","value":{"size":0,"unit":"px"}},"block-end":{"$$type":"size","value":{"size":0,"unit":"px"}},"inline-start":{"$$type":"size","value":{"size":0,"unit":"px"}}}},
           "border-style":"solid","border-color":"#FFFFFF1F"}),
  ],d={**col(0),"align-items":"center","width":pct(100),"max-width":560,"border-radius":32,"padding":pad(32,30,28)},t={"border-radius":26,"padding":pad(26,18,22)},g=("glass",)),"dd-links-panel")
stage=box("lk-stage",[panel],d={**col(0),"align-items":"center","position":"relative","z-index":1,"min-height":{"size":100,"unit":"vh"},"padding":pad(48,16,56)},t={"padding":pad(16,12,32)},tag="main")
print(ab("novamira/elementor-set-content",{"post_id":149,"content":[bg,stage]})[:1500])
