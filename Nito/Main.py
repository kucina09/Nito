import kivy
from kivy.lang import Builder
from kivy.app import App

kivy.require('2.2.1')

class CameraApp(App):
    def build(self):
        return Builder.load_file('main.kv')

    def capture(self):
        camera = self.root.ids.camera
        camera.export_to_png("photo.png")
        print("Zdjęcie zapisane jako photo.png")

if __name__ == '__main__':
    CameraApp().run()
