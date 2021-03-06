# coding:utf8
# https://github.com/faif/python-patterns/blob/master/structural/decorator.py


class TextTag(object):
    ''' Represents a base text tag '''
    def __init__(self, text):
        self._text = text

    def render(self):
        return self._text


class BoldWrapper(TextTag):
    ''' wraps a tag in <b> '''
    def __init__(self, wrapped):
        self._wrapped = wrapped

    def render(self):
        return f'<b>{self._wrapped.render()}</b>'


class ItalicWrapper(TextTag):
    ''' wraps a tag in <i> '''
    def __init__(self, wrapped):
        self._wrapped = wrapped

    def render(self):
        return f'<i>{self._wrapped.render()}</i>'


if __name__ == '__main__':
    simple_hello = TextTag('hello, world')
    special_hello = ItalicWrapper(BoldWrapper(simple_hello))
    print('before->', simple_hello.render())
    print('after->', special_hello.render())

# before-> hello, world
# after-> <i><b>hello, world</b></i>
