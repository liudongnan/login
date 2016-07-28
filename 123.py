# coding: gb2312
import requests

re = requests.get('http://www.ppdai.com/blacklistdetail/pdu2130278681')
re.encoding = 'utf-8'
target = re.content


def parse_by_tag(html, tag_b, tag_e):

    word_list = []
    while html:
        try:
            index = html.index(tag_b)
            begin = index + len(tag_b)
            end = begin + len(html[begin:begin+html[begin:].index(tag_e)])
            word_list.append(html[begin:end].strip())
            html = html[end+len(tag_e):]
        except ValueError:
            break
    return word_list


th = parse_by_tag(target, '<th>', '</th>')
td = parse_by_tag(target, '<td>', '</td>')
hr = parse_by_tag(target, '<hr>', '</p>')

for i, j in zip(th, td):
    print i, ":", j

for i in hr:
    for j in i.split('<br>'):
        print j.strip()





