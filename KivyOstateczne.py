__author__ = 'Crejzer'

#!/usr/bin/kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty, StringProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

#klasa obslugujaca elektrony
class Electron(Widget):

    #wspolrzedne pileczki
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    #metoda aktualizujaca pozycje
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

class Logo(Widget):
    pass
class Buzka(Widget):
    pass
class Menu(Screen):

    #stringi uzywane do stworzenia menu
    nazwaGry = StringProperty("Poznaj lepiej pierwszy w Polsce synchrotron!")
    start = StringProperty("Start Quiz")
class Quiz(Screen):
    dobre = NumericProperty(0)
    zle = NumericProperty(0)
    zle = 0
    dobre = 0

    class Quiz1(Screen):
    #obiekty na ktorych bedziemy uzywac danych metod (opcjonalne)
        a = ObjectProperty(None)
        b = ObjectProperty(None)
        c = ObjectProperty(None)
        d = ObjectProperty(None)
        zle = NumericProperty(None)
        dobre = NumericProperty(None)

    #wlaczanie zegara do wykrywania kolizji
        def start(self):
            Clock.schedule_interval(self.update, 1.0/60.0)

        #metoda wprawiajaca w ruch elektrony
        def serve_ball(self, vel=(4, 0)):
            self.a.center = self.center
            self.a.velocity = vel

            self.b.center = self.center
            self.b.velocity = vel

            self.c.center = self.center
            self.c.velocity = vel

            self.d.center = self.center
            self.d.velocity = vel

        def on_touch_up(self, touch):

            #wlaczam zegar aby wprawic w ruch elektrony
            self.start()
            if (self.a.x  <= touch.x - 10 and self.a.y <= touch.y - 10):
                self.zle = Quiz.zle
                self.zle += 1
                self.serve_ball()
                Quiz.zle = self.zle

            if (self.b.x  <= touch.x - 10 and self.b.y <= touch.y - 10 and touch.x < self.a.x):
                self.dobre = Quiz.dobre
                self.dobre += 1
                self.b.canvas.clear()
                Quiz.dobre = self.dobre

            if (self.c.x  <= touch.x - 10 and self.c.y <= touch.y - 10 and touch.y < self.b.y and touch.y < self.a.y):
                self.zle += 1
                self.serve_ball()
                Quiz.zle = self.zle

            if (self.d.x  <= touch.x - 10 and self.d.y <= touch.y - 10 and touch.x < self.c.x and touch.y < self.b.y and touch.y < self.a.y):
                self.zle += 1
                self.serve_ball()
                Quiz.zle = self.zle

        #metoda symulujaca ruch electronu i jego zakres
        def update(self, dt):
            self.a.move()
            self.b.move()
            self.c.move()
            self.d.move()

            if self.a.x < self.center_x:
                self.a.velocity_x *= -1
            if self.a.x > self.width - 600:
                self.a.velocity_x *= -1

            if self.b.x < self.x + 80:
                self.b.velocity_x *= -1
            if self.b.x > self.x:
                self.b.velocity_x *= -1

            if self.c.x < self.center_x:
                self.c.velocity_x *= -1
            if self.c.x > self.width - 600:
                self.c.velocity_x *= -1

            if self.d.x < self.x + 80:
                self.d.velocity_x *= -1
            if self.d.x > self.x:
                self.d.velocity_x *= -1

    class Quiz2(Screen):

        #obiekty na ktorych bedziemy uzywac danych metod (opcjonalne)
        a = ObjectProperty(None)
        b = ObjectProperty(None)
        c = ObjectProperty(None)
        d = ObjectProperty(None)
        zle = NumericProperty(None)
        dobre = NumericProperty(None)

    #wlaczanie zegara do wykrywania kolizji
        def start(self):
            Clock.schedule_interval(self.update, 1.0/60.0)

        #metoda wprawiajaca w ruch elektrony
        def serve_ball(self, vel=(4, 0)):
            self.a.center = self.center
            self.a.velocity = vel

            self.b.center = self.center
            self.b.velocity = vel

            self.c.center = self.center
            self.c.velocity = vel

            self.d.center = self.center
            self.d.velocity = vel

        def on_touch_up(self, touch):

            #wlaczam zegar aby wprawic w ruch elektrony
            self.start()
            if (self.a.x  <= touch.x - 10 and self.a.y <= touch.y - 10):
                self.zle = Quiz.zle
                self.zle += 1
                self.serve_ball()
                Quiz.zle = self.zle

            if (self.b.x  <= touch.x - 10 and self.b.y <= touch.y - 10 and touch.x < self.a.x):
                self.dobre = Quiz.dobre
                self.dobre += 1
                self.b.canvas.clear()
                Quiz.dobre = self.dobre

            if (self.c.x  <= touch.x - 10 and self.c.y <= touch.y - 10 and touch.y < self.b.y and touch.y < self.a.y):
                self.zle += 1
                self.serve_ball()
                Quiz.zle = self.zle

            if (self.d.x  <= touch.x - 10 and self.d.y <= touch.y - 10 and touch.x < self.c.x and touch.y < self.b.y and touch.y < self.a.y):
                self.zle += 1
                self.serve_ball()
                Quiz.zle = self.zle

        #metoda symulujaca ruch electronu i jego zakres
        def update(self, dt):
            self.a.move()
            self.b.move()
            self.c.move()
            self.d.move()

            if self.a.x < self.center_x:
                self.a.velocity_x *= -1
            if self.a.x > self.width - 600:
                self.a.velocity_x *= -1

            if self.b.x < self.x + 80:
                self.b.velocity_x *= -1
            if self.b.x > self.x:
                self.b.velocity_x *= -1

            if self.c.x < self.center_x:
                self.c.velocity_x *= -1
            if self.c.x > self.width - 600:
                self.c.velocity_x *= -1

            if self.d.x < self.x + 80:
                self.d.velocity_x *= -1
            if self.d.x > self.x:
                self.d.velocity_x *= -1

    class Quiz3(Screen):

    #obiekty na ktorych bedziemy uzywac danych metod (opcjonalne)
        a = ObjectProperty(None)
        b = ObjectProperty(None)
        c = ObjectProperty(None)
        d = ObjectProperty(None)
        zle = NumericProperty(None)
        dobre = NumericProperty(None)

    #wlaczanie zegara do wykrywania kolizji
        def start(self):
            Clock.schedule_interval(self.update, 1.0/60.0)

        #metoda wprawiajaca w ruch elektrony
        def serve_ball(self, vel=(4, 0)):
            self.a.center = self.center
            self.a.velocity = vel

            self.b.center = self.center
            self.b.velocity = vel

            self.c.center = self.center
            self.c.velocity = vel

            self.d.center = self.center
            self.d.velocity = vel

        def on_touch_up(self, touch):

            #wlaczam zegar aby wprawic w ruch elektrony
            self.start()
            if (self.a.x  <= touch.x - 10 and self.a.y <= touch.y - 10):
                self.zle = Quiz.zle
                self.zle += 1
                self.serve_ball()
                Quiz.zle = self.zle

            if (self.b.x  <= touch.x - 10 and self.b.y <= touch.y - 10 and touch.x < self.a.x):
                self.dobre = Quiz.dobre
                self.dobre += 1
                self.b.canvas.clear()
                Quiz.dobre = self.dobre

            if (self.c.x  <= touch.x - 10 and self.c.y <= touch.y - 10 and touch.y < self.b.y and touch.y < self.a.y):
                self.zle += 1
                self.serve_ball()
                Quiz.zle = self.zle

            if (self.d.x  <= touch.x - 10 and self.d.y <= touch.y - 10 and touch.x < self.c.x and touch.y < self.b.y and touch.y < self.a.y):
                self.zle += 1
                self.serve_ball()
                Quiz.zle = self.zle

        #metoda symulujaca ruch electronu i jego zakres
        def update(self, dt):
            self.a.move()
            self.b.move()
            self.c.move()
            self.d.move()

            if self.a.x < self.center_x:
                self.a.velocity_x *= -1
            if self.a.x > self.width - 600:
                self.a.velocity_x *= -1

            if self.b.x < self.x + 80:
                self.b.velocity_x *= -1
            if self.b.x > self.x:
                self.b.velocity_x *= -1

            if self.c.x < self.center_x:
                self.c.velocity_x *= -1
            if self.c.x > self.width - 600:
                self.c.velocity_x *= -1

            if self.d.x < self.x + 80:
                self.d.velocity_x *= -1
            if self.d.x > self.x:
                self.d.velocity_x *= -1

    class Quiz4(Screen):

     #obiekty na ktorych bedziemy uzywac danych metod (opcjonalne)
        a = ObjectProperty(None)
        b = ObjectProperty(None)
        c = ObjectProperty(None)
        d = ObjectProperty(None)
        zle = NumericProperty(None)
        dobre = NumericProperty(None)

    #wlaczanie zegara do wykrywania kolizji
        def start(self):
            Clock.schedule_interval(self.update, 1.0/60.0)

        #metoda wprawiajaca w ruch elektrony
        def serve_ball(self, vel=(4, 0)):
            self.a.center = self.center
            self.a.velocity = vel

            self.b.center = self.center
            self.b.velocity = vel

            self.c.center = self.center
            self.c.velocity = vel

            self.d.center = self.center
            self.d.velocity = vel

        def on_touch_up(self, touch):

            #wlaczam zegar aby wprawic w ruch elektrony
            self.start()
            if (self.a.x  <= touch.x - 10 and self.a.y <= touch.y - 10):
                self.zle = Quiz.zle
                self.zle += 1
                self.serve_ball()
                Quiz.zle = self.zle

            if (self.b.x  <= touch.x - 10 and self.b.y <= touch.y - 10 and touch.x < self.a.x):
                self.dobre = Quiz.dobre
                self.dobre += 1
                self.b.canvas.clear()
                Quiz.dobre = self.dobre

            if (self.c.x  <= touch.x - 10 and self.c.y <= touch.y - 10 and touch.y < self.b.y and touch.y < self.a.y):
                self.zle += 1
                self.serve_ball()
                Quiz.zle = self.zle

            if (self.d.x  <= touch.x - 10 and self.d.y <= touch.y - 10 and touch.x < self.c.x and touch.y < self.b.y and touch.y < self.a.y):
                self.zle += 1
                self.serve_ball()
                Quiz.zle = self.zle

        #metoda symulujaca ruch electronu i jego zakres
        def update(self, dt):
            self.a.move()
            self.b.move()
            self.c.move()
            self.d.move()

            if self.a.x < self.center_x:
                self.a.velocity_x *= -1
            if self.a.x > self.width - 600:
                self.a.velocity_x *= -1

            if self.b.x < self.x + 80:
                self.b.velocity_x *= -1
            if self.b.x > self.x:
                self.b.velocity_x *= -1

            if self.c.x < self.center_x:
                self.c.velocity_x *= -1
            if self.c.x > self.width - 600:
                self.c.velocity_x *= -1

            if self.d.x < self.x + 80:
                self.d.velocity_x *= -1
            if self.d.x > self.x:
                self.d.velocity_x *= -1

    class Quiz5(Screen):
    #obiekty na ktorych bedziemy uzywac danych metod (opcjonalne)
        a = ObjectProperty(None)
        b = ObjectProperty(None)
        c = ObjectProperty(None)
        d = ObjectProperty(None)
        zle = NumericProperty(None)
        dobre = NumericProperty(None)

    #wlaczanie zegara do wykrywania kolizji
        def start(self):
            Clock.schedule_interval(self.update, 1.0/60.0)

        #metoda wprawiajaca w ruch elektrony
        def serve_ball(self, vel=(4, 0)):
            self.a.center = self.center
            self.a.velocity = vel

            self.b.center = self.center
            self.b.velocity = vel

            self.c.center = self.center
            self.c.velocity = vel

            self.d.center = self.center
            self.d.velocity = vel

        def on_touch_up(self, touch):

            #wlaczam zegar aby wprawic w ruch elektrony
            self.start()
            if (self.a.x  <= touch.x - 10 and self.a.y <= touch.y - 10):
                self.dobre = Quiz.dobre
                self.dobre += 1
                self.b.canvas.clear()
                Quiz.dobre = self.dobre

            if (self.b.x  <= touch.x - 10 and self.b.y <= touch.y - 10 and touch.x < self.a.x):
                self.zle = Quiz.zle
                self.zle += 1
                self.serve_ball()
                Quiz.zle = self.zle

            if (self.c.x  <= touch.x - 10 and self.c.y <= touch.y - 10 and touch.y < self.b.y and touch.y < self.a.y):
                self.zle += 1
                self.serve_ball()
                Quiz.zle = self.zle

            if (self.d.x  <= touch.x - 10 and self.d.y <= touch.y - 10 and touch.x < self.c.x and touch.y < self.b.y and touch.y < self.a.y):
                self.zle += 1
                self.serve_ball()
                Quiz.zle = self.zle

        #metoda symulujaca ruch electronu i jego zakres
        def update(self, dt):
            self.a.move()
            self.b.move()
            self.c.move()
            self.d.move()

            if self.a.x < self.center_x:
                self.a.velocity_x *= -1
            if self.a.x > self.width - 600:
                self.a.velocity_x *= -1

            if self.b.x < self.x + 80:
                self.b.velocity_x *= -1
            if self.b.x > self.x:
                self.b.velocity_x *= -1

            if self.c.x < self.center_x:
                self.c.velocity_x *= -1
            if self.c.x > self.width - 600:
                self.c.velocity_x *= -1

            if self.d.x < self.x + 80:
                self.d.velocity_x *= -1
            if self.d.x > self.x:
                self.d.velocity_x *= -1

    class Quiz6(Screen):
    #obiekty na ktorych bedziemy uzywac danych metod (opcjonalne)
        a = ObjectProperty(None)
        b = ObjectProperty(None)
        c = ObjectProperty(None)
        d = ObjectProperty(None)
        zle = NumericProperty(None)
        dobre = NumericProperty(None)

    #wlaczanie zegara do wykrywania kolizji
        def start(self):
            Clock.schedule_interval(self.update, 1.0/60.0)

        #metoda wprawiajaca w ruch elektrony
        def serve_ball(self, vel=(4, 0)):
            self.a.center = self.center
            self.a.velocity = vel

            self.b.center = self.center
            self.b.velocity = vel

            self.c.center = self.center
            self.c.velocity = vel

            self.d.center = self.center
            self.d.velocity = vel

        def on_touch_up(self, touch):

            #wlaczam zegar aby wprawic w ruch elektrony
            self.start()
            if (self.a.x  <= touch.x - 10 and self.a.y <= touch.y - 10):
                self.zle = Quiz.zle
                self.zle += 1
                self.serve_ball()
                Quiz.zle = self.zle

            if (self.b.x  <= touch.x - 10 and self.b.y <= touch.y - 10 and touch.x < self.a.x):
                self.zle = Quiz.zle
                self.zle += 1
                self.serve_ball()
                Quiz.zle = self.zle

            if (self.c.x  <= touch.x - 10 and self.c.y <= touch.y - 10 and touch.y < self.b.y and touch.y < self.a.y):
                self.dobre = Quiz.dobre
                self.dobre += 1
                self.b.canvas.clear()
                Quiz.dobre = self.dobre

            if (self.d.x  <= touch.x - 10 and self.d.y <= touch.y - 10 and touch.x < self.c.x and touch.y < self.b.y and touch.y < self.a.y):
                self.zle = Quiz.zle
                self.zle += 1
                self.serve_ball()
                Quiz.zle = self.zle

        #metoda symulujaca ruch electronu i jego zakres
        def update(self, dt):
            self.a.move()
            self.b.move()
            self.c.move()
            self.d.move()

            if self.a.x < self.center_x:
                self.a.velocity_x *= -1
            if self.a.x > self.width - 600:
                self.a.velocity_x *= -1

            if self.b.x < self.x + 80:
                self.b.velocity_x *= -1
            if self.b.x > self.x:
                self.b.velocity_x *= -1

            if self.c.x < self.center_x:
                self.c.velocity_x *= -1
            if self.c.x > self.width - 600:
                self.c.velocity_x *= -1

            if self.d.x < self.x + 80:
                self.d.velocity_x *= -1
            if self.d.x > self.x:
                self.d.velocity_x *= -1

    class Quiz7(Screen):
    #obiekty na ktorych bedziemy uzywac danych metod (opcjonalne)
        a = ObjectProperty(None)
        b = ObjectProperty(None)
        c = ObjectProperty(None)
        d = ObjectProperty(None)
        zle = NumericProperty(None)
        dobre = NumericProperty(None)

    #wlaczanie zegara do wykrywania kolizji
        def start(self):
            Clock.schedule_interval(self.update, 1.0/60.0)

        #metoda wprawiajaca w ruch elektrony
        def serve_ball(self, vel=(4, 0)):
            self.a.center = self.center
            self.a.velocity = vel

            self.b.center = self.center
            self.b.velocity = vel

            self.c.center = self.center
            self.c.velocity = vel

            self.d.center = self.center
            self.d.velocity = vel

        def on_touch_up(self, touch):

            #wlaczam zegar aby wprawic w ruch elektrony
            self.start()
            if (self.a.x  <= touch.x - 10 and self.a.y <= touch.y - 10):
                self.zle = Quiz.zle
                self.zle += 1
                self.serve_ball()
                Quiz.zle = self.zle

            if (self.b.x  <= touch.x - 10 and self.b.y <= touch.y - 10 and touch.x < self.a.x):
                self.zle = Quiz.zle
                self.zle += 1
                self.serve_ball()
                Quiz.zle = self.zle

            if (self.c.x  <= touch.x - 10 and self.c.y <= touch.y - 10 and touch.y < self.b.y and touch.y < self.a.y):
                self.dobre = Quiz.dobre
                self.dobre += 1
                self.b.canvas.clear()
                Quiz.dobre = self.dobre

            if (self.d.x  <= touch.x - 10 and self.d.y <= touch.y - 10 and touch.x < self.c.x and touch.y < self.b.y and touch.y < self.a.y):
                self.zle = Quiz.zle
                self.zle += 1
                self.serve_ball()
                Quiz.zle = self.zle

        #metoda symulujaca ruch electronu i jego zakres
        def update(self, dt):
            self.a.move()
            self.b.move()
            self.c.move()
            self.d.move()

            if self.a.x < self.center_x:
                self.a.velocity_x *= -1
            if self.a.x > self.width - 600:
                self.a.velocity_x *= -1

            if self.b.x < self.x + 80:
                self.b.velocity_x *= -1
            if self.b.x > self.x:
                self.b.velocity_x *= -1

            if self.c.x < self.center_x:
                self.c.velocity_x *= -1
            if self.c.x > self.width - 600:
                self.c.velocity_x *= -1

            if self.d.x < self.x + 80:
                self.d.velocity_x *= -1
            if self.d.x > self.x:
                self.d.velocity_x *= -1

    class Quiz8(Screen):
    #obiekty na ktorych bedziemy uzywac danych metod (opcjonalne)
        a = ObjectProperty(None)
        b = ObjectProperty(None)
        c = ObjectProperty(None)
        d = ObjectProperty(None)
        zle = NumericProperty(None)
        dobre = NumericProperty(None)

    #wlaczanie zegara do wykrywania kolizji
        def start(self):
            Clock.schedule_interval(self.update, 1.0/60.0)

        #metoda wprawiajaca w ruch elektrony
        def serve_ball(self, vel=(4, 0)):
            self.a.center = self.center
            self.a.velocity = vel

            self.b.center = self.center
            self.b.velocity = vel

            self.c.center = self.center
            self.c.velocity = vel

            self.d.center = self.center
            self.d.velocity = vel

        def on_touch_up(self, touch):

            #wlaczam zegar aby wprawic w ruch elektrony
            self.start()
            if (self.a.x  <= touch.x - 10 and self.a.y <= touch.y - 10):
                self.zle = Quiz.zle
                self.zle += 1
                self.serve_ball()
                Quiz.zle = self.zle

            if (self.b.x  <= touch.x - 10 and self.b.y <= touch.y - 10 and touch.x < self.a.x):
                self.zle = Quiz.zle
                self.zle += 1
                self.serve_ball()
                Quiz.zle = self.zle

            if (self.c.x  <= touch.x - 10 and self.c.y <= touch.y - 10 and touch.y < self.b.y and touch.y < self.a.y):
                self.dobre = Quiz.dobre
                self.dobre += 1
                self.b.canvas.clear()
                Quiz.dobre = self.dobre

            if (self.d.x  <= touch.x - 10 and self.d.y <= touch.y - 10 and touch.x < self.c.x and touch.y < self.b.y and touch.y < self.a.y):
                self.zle = Quiz.zle
                self.zle += 1
                self.serve_ball()
                Quiz.zle = self.zle

        #metoda symulujaca ruch electronu i jego zakres
        def update(self, dt):
            self.a.move()
            self.b.move()
            self.c.move()
            self.d.move()

            if self.a.x < self.center_x:
                self.a.velocity_x *= -1
            if self.a.x > self.width - 600:
                self.a.velocity_x *= -1

            if self.b.x < self.x + 80:
                self.b.velocity_x *= -1
            if self.b.x > self.x:
                self.b.velocity_x *= -1

            if self.c.x < self.center_x:
                self.c.velocity_x *= -1
            if self.c.x > self.width - 600:
                self.c.velocity_x *= -1

            if self.d.x < self.x + 80:
                self.d.velocity_x *= -1
            if self.d.x > self.x:
                self.d.velocity_x *= -1


gra = Builder.load_file("gra.kv")

#klasa uruchamjajaca nasza gre
class GraApp(App):
    def build(self):
        return gra

if __name__ == '__main__':
    GraApp().run()