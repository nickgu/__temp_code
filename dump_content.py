#! /bin/python
# encoding=utf-8

import sys
import json

if __name__=='__main__':
    for line in sys.stdin.readlines():
        d = json.loads(line)
        key = 'col:patient_case'
        if key in d:
            for list_item in d[key]:
                if 'content' in list_item:
                    for con in list_item['content']:
                        title = con.get('title', '')
                        if title != u'现病史' and title != u'主诉':
                            continue
                        text = con.get('text', '')
                        text = text.replace('\n', ' ')
                        if len(text) >= 10:
                            print text.encode('utf-8')
