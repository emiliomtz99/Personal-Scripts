import pyglet

window = pyglet.window.Window(resizable=True)

@window.event
def on_resize(width, height):
    print ('The window was resized to %dx%d' % (width, height))