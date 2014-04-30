# coding=utf8
import argparse
import sys

from pip.backwardcompat import raw_input

from utils.texttable import Texttable


class Rule:
    '''
    symbol - обозрваемый символ
    state - текущее состояние, число, 1 - начальное состояние
    new_symbol - символ для замены
    shear - сдвиг, -1 - влево, 1 - вправо, 0 - остаься на месте
    next_state - следующее состояни, 0 - конечное состояние
    '''
    symbol = ''
    state = 0
    new_symbol = ''
    shear = 0  # -1, 1, 0
    next_state = 0

    def is_incorrect(self):
        out = (not self.symbol) or (not self.new_symbol)
        return out

    def __init__(self, state, symbol, new_symbol, shear, next_state):
        '''
        symbol - обозрваемый символ
        state - текущее состояние, число, 1 - начальное состояние
        new_symbol - символ для замены
        shear - сдвиг, -1 - влево, 1 - вправо, 0 - остаься на месте
        next_state - следующее состояни, 0 - конечное состояние
        '''
        self.symbol = str(symbol)[0]
        self.state = state
        self.new_symbol = str(new_symbol)[0]
        self.shear = shear
        self.next_state = next_state

    @property
    def preview(self):
        if self.is_incorrect():
            return ''
        str_shear = '0'
        if self.shear <= 1: str_shear = 'L'
        if self.shear >= 1: str_shear = 'R'
        return '{0}, {2}, q{1}' \
            .format(self.new_symbol,
                    self.next_state if self.next_state != 0 else 'END',
                    str_shear)


    def __str__(self):
        return '[q{0}, {1}] : {2}' \
            .format(self.state if self.state != 0 else 'END',
                    self.symbol,
                    self.preview)


class Turing:
    '''
    Машина Тьюринга,
    начальная позиция головки есть 0
    начальное состояние -- 1
    '''
    rules = {}
    _tape = []  # лента
    _position = 0  # текущее положение головки на читающей ленте
    _state = 1  # текущее состояние
    _left_offset = 0
    _empty_cell = '...'

    _step = 0

    empty_symbol = '0'

    # pointer_symbol = '*' if sys.version_info[0] < 3 else '▼'
    pointer_symbol = '▼'

    def __init__(self, empty_symbol='0', path=None):
        self.empty_symbol = empty_symbol
        if path:
            self.load(path)


    def add_rule(self, rule):
        self.rules[rule.state] = self.rules.get(rule.state, {})
        self.rules[rule.state][rule.symbol] = rule

    @property
    def state(self):
        return self._state

    @property
    def alphabet(self):
        out = []
        for (_, dict) in self.rules.items():
            # if key not in out:
            #     out.append(key)
            for (symbol, rule) in dict.items():
                if symbol not in out:
                    out.append(symbol)
                if rule.new_symbol not in out:
                    out.append(rule.new_symbol)

        out.sort()
        return out

    @property
    def states(self):
        out = []
        for (state, dict) in self.rules.items():
            if state not in out:
                out.append(state)
            for (_, rule) in dict.items():
                if rule.state not in out:
                    out.append(rule.state)
                if rule.next_state not in out:
                    out.append(rule.next_state)
        out.sort()
        return out

    def rule(self, state, symbol):
        try:
            return self.rules[state][symbol]
        except KeyError:
            return ''

    def show(self):
        table = Texttable()

        header = ['\\'] + self.alphabet
        # table.set_cols_align(['c'] * len(header))
        table.add_row(header)

        states = self.states
        alphabet = self.alphabet

        for state in states:
            if state == 0:
                continue
            row = ['q{0}'.format(state), ]
            for symbol in alphabet:
                r = self.rule(state, symbol)
                s = r.preview if r else ' '
                row.append(s)

            table.add_row(row)
        return table.draw()

    def __str__(self):
        return '\n'.join(str(s) for s in self.rules)

    @property
    def symbol(self):
        '''
        возвращает текущий обозреваемый символ
        '''
        try:
            return self._tape[self._position]
        except IndexError:
            return self.empty_symbol


    def reset(self):
        self._tape = []
        self._step = 0
        self._state = 1

    def next(self):
        '''
        возвращает True если МТ не завершила работу
        и  False иначе
        '''
        rule = self.rule(self._state, symbol=self.symbol)
        if not rule:
            return False

        self.set_tape(self._position, rule.new_symbol)
        self._position += rule.shear

        if self._position >= len(self._tape):
            self.set_tape(self._position, self.empty_symbol)
        if self._position < 0:
            self.set_tape(self._position, self.empty_symbol)

        self._state = rule.next_state

        if self._state == 0:
            return False

        self._step += 1

        return True


    @property
    def step(self):
        return self._step

    def tape(self, i):
        try:
            return self._tape[i]
        except IndexError:
            return ''

    def set_tape(self, i, value):
        i += self._left_offset
        if i < 0:
            # self._position += 1
            diff = -i;
            self._tape = [self.empty_symbol] * diff + self._tape
            self._tape[0] = value
            self._left_offset += diff
            # self._position += self._left_offset
            # self._left_offset = 0
        elif i >= len(self._tape):
            diff = i - len(self._tape)
            self._tape += [self.empty_symbol] * diff + [str(value)[0]]
        else:
            self._tape[i] = value


    def _create_pointer(self, length):
        out = [' '] * length
        length = int(length / 2)
        out[length] = self.pointer_symbol
        return ''.join(out)

    @property
    def show_tape(self):
        row = [self._empty_cell] + [self.empty_symbol]
        row += list(s if i != self._position else '{0}'.format(s) for i, s in enumerate(self._tape))
        row += [self.empty_symbol] + [self._empty_cell]

        header = list(
            ' ' * len(v) if i != self._position + 2 else self._create_pointer(len(v)) for i, v in enumerate(row))

        sep = '  '
        body = sep.join(header) + '\n'
        body += sep.join(row)

        return '{0}'.format(body)


    def set_tape_array(self, array):
        self._tape = list(str(e) for e in array)


    def load(self, path):
        self.rules.clear()
        f = open(path)
        for l in f:
            l = l.strip()
            if l.startswith('#'):
                continue
            e = l.split(' ')
            self.add_rule(Rule(
                state=int(e[0]),
                symbol=e[1],
                new_symbol=e[2],
                shear=int(e[3]),
                next_state=int(e[4])))


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="sample (subtract one):\n\n"
                    "#in state 1 saw 1, change it for 1, move right set current state to 1\n"
                    "1 1 1 1 1\n"
                    "# in state 1 saw 0 change it for 0, move left, set current state to 2\n"
                    "1 0 0 -1 2\n"
                    "# in state 2 saw 1 change it for 0, dont move head, set current state to end state\n"
                    "2 1 0 0 0\n"
                    "# in state 2 saw 0 change it for 0, dont move head, set current state to end state\n"
                    "2 0 0 0 0\n")
    parser.add_argument('path', metavar='path', help='path to file with turing machine description')
    parser.add_argument('tape', help='tape state of turing machine (ex: 001110100100')
    parser.add_argument('emptysymbol', help='empty symbol for tape')

    args = parser.parse_args()

    t = Turing()
    t.empty_symbol = args.emptysymbol
    t.load(args.path)

    print ('-=-=-=-=-=-\n{0}:'.format(args.path))
    print(t.show())
    print ('-=-=-=-=-=-\n')

    t.set_tape_array(str(args.tape))
    info_prompt = ''

    while True:
        print('{0}. {4}\n{2}\n'.format(t.step+1,
                                       t.state,
                                       t.show_tape,
                                       t.symbol,
                                       t.rule(t.state, t.symbol)))

        if sys.version_info[0] < 3:
            k = raw_input(info_prompt)
        else:
            k = input(info_prompt)

        if k and k.lower() == 'q':
            break

        if not t.next():
            break


if __name__ == "__main__":
    main()
