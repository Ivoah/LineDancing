import re
import dataclasses

repertoire = {
    'cast': re.compile(r'(?P<couple>1st|2nd) couple cast (?P<direction>up|down) (?P<places>\d+)'),
    'lead': re.compile(r'(?P<couple>1st|2nd) couple lead (?P<direction>up|down) (?P<places>\d+)'),
    'corners_cross_right': re.compile(r'(?P<corners>1st|2nd) corners cross right shoulders'),
    'circle_halfway': re.compile(r'Circle (?P<direction>left|right) halfway')
}

@dataclasses.dataclass
class Step:
    name: str
    start: int
    stop: int
    meta: dict

class Dance:
    def __init__(self, name):
        with open(f'Dances/{name}.txt') as f:
            match = re.match(r'Song: (.+)\nStart: (\d+)\nSpeed: (\d+)\n\n(.+)', f.read(), re.DOTALL)
        self.song = f'Songs/{match[1]}.ogg'
        self.start = int(match[2])
        self.speed = float(match[3])

        last = 0
        self.steps = []
        for step in match[4].strip().split('\n'):
            step, length = re.match(r'(.*) \((\d+) counts?\)', step).groups()
            length = int(length)
            for step in step.split(' : '):
                for name, patt in repertoire.items():
                    match = patt.match(step)
                    if match:
                        self.steps.append(Step(name, last, last + length, match.groupdict()))
            last += length

        self.duration = last

    def get_steps(self, millis):
        if millis < self.start: return []
        count = (millis - self.start)/self.speed%self.duration
        return [(step, (count - step.start)/(step.stop - step.start)) for step in self.steps if step.start <= count < step.stop]

if __name__ == '__main__':
    dance = Dance('Hole in the Wall')
    print(dance.get_steps(0))
