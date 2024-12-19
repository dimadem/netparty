from app.core.scene import BaseScene

class CompositeScene(BaseScene):
    def __init__(self):
        self.layers = {}  # Перемещаем инициализацию перед super().__init__()
        self.layer_order = []
        super().__init__()

    def initialize(self):
        # Каждый слой должен быть инициализирован
        for layer in self.layers.values():
            layer.initialize()
            layer.active = True

    def add_layer(self, name, scene, order=None):
        self.layers[name] = scene
        scene.initialize()  # Инициализируем слой при добавлении
        scene.active = True  # Активируем слой
        if order is not None:
            self.layer_order.insert(order, name)
        else:
            self.layer_order.append(name)

    def on_enter(self):
        super().on_enter()
        # Активируем все слои при входе в сцену
        for layer in self.layers.values():
            layer.on_enter()

    def on_exit(self):
        super().on_exit()
        # Деактивируем все слои при выходе из сцены
        for layer in self.layers.values():
            layer.on_exit()

    def update(self, dt):
        # Обновляем все слои
        for layer_name in self.layer_order:
            self.layers[layer_name].update(dt)

    def draw(self, screen):
        # Отрисовываем все слои в правильном порядке
        for layer_name in self.layer_order:
            self.layers[layer_name].draw(screen)

    def handle_input(self, event):
        # Обрабатываем ввод для каждого слоя в обратном порядке
        for layer_name in reversed(self.layer_order):
            self.layers[layer_name].handle_input(event)
