import pyglet
from pyglet.gl import *
window = pyglet.window.Window() 
@window.event
def on_draw (): 
  glClear(GL_COLOR_BUFFER_BIT)
  glMatrixMode(GL_MODELVIEW)
  #pyglet.graphics.draw(2, pyglet.gl.GL_LINES, ('v2i', (10,15,300,305)))
  glBegin(GL_TRIANGLES)
  glVertex2i(300,300)
  glColor3f(1,0,0)
  glVertex2i(400,200)
  glColor3f(0,1,0)
  glVertex2i(200,200)
  glColor3f(0,0,1)
  glEnd()
pyglet.app.run()

