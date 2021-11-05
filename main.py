import pysrt
import opencc

c = opencc.OpenCC('s2tw')

subs = pysrt.open('input.srt')
for i in range(len(subs)):
    subs[i].text = c.convert(subs[i].text)
subs.save('output.srt', encoding='utf-8')
