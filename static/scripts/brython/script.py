from browser import window,document, alert
from browser import document as doc

jq = window.jQuery
def callback(event, isInView):
  if(isInView):
    print("見えた")
#    contents_list.appendChild()
    for i in range(0,15):
      doc["contents_list"].html += "<li>test</li>"
  else:
    print("消えた")

jq('#last').on('inview', callback)
