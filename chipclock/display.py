from multiprocessing.dummy import Pool

class ModeDisplay:
    def __init__(self):
        self.modes = {}
        self.renderers = {}
        self.current_mode = None
        self.is_animating = False
    
    def register_mode(self, name, mode, renderers):
        self.modes[name] = mode
        self.renderers[name] = renderers
        self.current_mode = name

    def notify(self):
        pool = Pool(1)
        pool.apply_async(self.render)
        pool.close()

    def render(self):
        if self.is_animating:
            return False

        mode = self.current_mode

        def render_single(renderer):
            animation_running = True
            while animation_running and mode == self.current_mode:
                value = self.modes.get(mode).value
                animation_running = renderer(value)

        renderers = self.renderers.get(self.current_mode)
        self.is_animating = True
        pool = Pool(len(renderers))
        for renderer in renderers:
            pool.apply_async(render_single, (renderer, ))
        pool.close()
        pool.join()
        self.is_animating = False
      
        if mode != self.current_mode:
            self.render()

    def set_mode(self, name):
        self.current_mode = name
        self.modes.get(name).activate()
        self.render()
