class Animation:
    def __init__(self, frames, speed):
        self.frames = frames
        self.speed = speed
        self.current_frame = 0
        self.timer = 0
        self.paused = False
        self.loop = True
    
    def pause(self):
        self.paused = True
    
    def resume(self):
        self.paused = False
    
    def reset(self):
        self.current_frame = 0
        self.timer = 0
    
    def update(self, dt):
        if self.paused:
            return

        self.timer += dt
        if self.timer >= self.speed:
            if self.loop or self.current_frame < len(self.frames) - 1:
                self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.timer = 0
        
    def get_current_frame(self):
        return self.frames[self.current_frame]