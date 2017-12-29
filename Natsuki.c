#include <GL/glew.h>
#include <GL/glut.h>
#include <stdlib.h>
#include <stdio.h> 



int main(int argc, char** argv)
{
  glutInit(&amp;argc, argv);
  glutInitDisplayMode(GLUT_DOUBLE);
  glutCreateWindow("Multipass texturing Demo");
  glewInit();
 
  glutTimerFunc(0,timer,0);
  glutDisplayFunc(display);
  glutKeyboardFunc(keyboard);
 
  init();
 
  glutMainLoop();
  return 0;
}