class ProgressBar:

    def __init__(self, max_value):
        self.cls_line = "\u001b[2K"
        self.move_left = "\u001b[{}D"
        self.max_value = max_value

    def progress(self, progress, ext_str=None):
        print(self.cls_line,
              self.move_left.format(1000),
              self.__build_tag(progress + 1, self.max_value),
              '' if ext_str is None else ext_str,
              end='',
              flush=True)

    def end(self):
        print()

    def __call__(self, *args, **kwargs):
        return range(self.max_value)

    def __build_tag(self, progress, max_value):
        tag = '['

        for _ in range(progress):
            tag += '#'

        for j in range(max_value - progress):
            tag += '-'

        tag += ']'

        return tag
