from kivy.graphics import Line


class DynamicLineWidget():
    instructions = []
    on_canvas = []

    def __init__(self, **kwargs):
        w, h = 950, 750
        self.kwargs = kwargs

        self.parent = kwargs['parent']
        del self.kwargs['parent']
        self.width = kwargs['width'] / (w * h)
        del self.kwargs['width']

        try:
            self.scaled_bezier = list(x / (w if not i % 2 else h)
                                      for i, x in enumerate(kwargs['bezier']))
            del self.kwargs['bezier']
        except:
            pass

        try:
            self.scaled_circle = [
                kwargs['circle'][0] / w, kwargs['circle'][1] / h, kwargs['circle'][2] / (w + h)]
            del self.kwargs['circle']
        except:
            pass

        DynamicLineWidget.instructions.append(self)
        self.redraw()
        self.parent.bind(size=lambda *args: self.dynamic_draw())

    def redraw(self):
        w, h = self.parent.size
        new_width = self.width * (w * h)

        try:
            new_bezier = list(x * (w if not i % 2 else h)
                              for i, x in enumerate(self.scaled_bezier))
            with self.parent.canvas:
                obj = Line(bezier=new_bezier, width=new_width, **self.kwargs)
                DynamicLineWidget.on_canvas.append(obj)
                obj
        except:
            pass

        try:
            new_circle = [self.scaled_circle[0] * w,
                          self.scaled_circle[1] * h, self.scaled_circle[2] * (w + h)]
            with self.parent.canvas:
                obj = Line(circle=new_circle, width=new_width, **self.kwargs)
                DynamicLineWidget.on_canvas.append(obj)
                obj
        except:
            pass

    def dynamic_draw(self):
        for instr in DynamicLineWidget.on_canvas:
            self.parent.canvas.remove(instr)
        DynamicLineWidget.on_canvas.clear()

        for instr in DynamicLineWidget.instructions:
            instr.redraw()

