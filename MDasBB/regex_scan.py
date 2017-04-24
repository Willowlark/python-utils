import sys
import re


class DumbSwitch:

    def __init__(self, flag=0):
        self.flag = flag

    def switch(self):
        pass


class Instance(DumbSwitch):
    def __init__(self):
        self.flag = 0

    def switch(self):
        self.flag = 0 if self.flag else 1


subs = {'*':'i', '**':'b', '_':'u', '&':'color', '&&c':'center', '---':'hr',
        '&c':'color=#79ab66', '&s':'color=#ffb90f', '&r': 'color=#9a5821',
        '&a':'color=#047800', '&v':'color=#ee5d5d', '&w':'color=white',
        '&b':'color=#EC5800', '&p':'color=#D464E4', '&n':'color=#8E44AD', '&u':'color=#FBF9AB'}

state = {code: Instance() if 'color' not in code else DumbSwitch() for code in subs.values()}
state['hr'] = DumbSwitch()
state['color'] = DumbSwitch(1)


def loadText():
    lines = []
    if len(sys.argv) > 1:
        pass
    else:
        paste_data = raw_input("Input text -> ")
        lines.append(paste_data)
        while paste_data is not "":
            paste_data = raw_input("")
            lines.append(paste_data)
    return lines


def convert(lines):
    writer = open('bbify.txt', 'w')
    for line in lines:
        for markdown in reversed(sorted(subs, key=lambda x: len(x))):
            if line != '\n':
                while re.search(re.escape(markdown), line) is not None:
                    line = re.sub(re.escape(markdown), replace(markdown), line, count=1)
        writer.write(line)
        writer.write('\n')
    return 0


def replace(markdown):
    code = subs[markdown]
    if state[code].flag:
        state[code].switch()
        return '[/'+code+']' if 'color' not in code else '[/'+code+']"'
    else:
        state[code].switch()
        return '['+code+']' if 'color' not in code else '"['+code+']'

if __name__ == "__main__":
    lines = loadText()
    convert(lines)
    print "Done!"