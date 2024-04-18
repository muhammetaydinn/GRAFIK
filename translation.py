from OpenGL.GL import *
from OpenGL.GLUT import *

def draw_square():
    glBegin(GL_QUADS)
    glVertex2f(-0.5, -0.5)
    glVertex2f(0.5, -0.5)
    glVertex2f(0.5, 0.5)
    glVertex2f(-0.5, 0.5)
    glEnd()
def display_rotate_translate():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    glLoadIdentity()
    glRotatef(45, 0.0, 0.0, 1.0)  # Önce çevirme
    glTranslatef(0.5, 0.0, 0.0)   # Sonra çevirme
    
    glColor3f(1.0, 0.0, 0.0)
    draw_square()
    
    glutSwapBuffers()
def display_translate_rotate():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    glLoadIdentity()
    glTranslatef(0.5, 0.0, 0.0)   # Önce çevirme
    glRotatef(45, 0.0, 0.0, 1.0)  # Sonra çevirme
    
    glColor3f(0.0, 1.0, 0.0)
    draw_square()
    
    glutSwapBuffers()
def display_normal():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    glLoadIdentity()
    
    glColor3f(0.0, 0.0, 1.0)
    draw_square()
    
    glutSwapBuffers()
def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"OpenGL Rotate Translate Example")
    
    glutDisplayFunc(display_rotate_translate)
    glutIdleFunc(display_rotate_translate)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"OpenGL Translate Rotate Example")
    
    glutDisplayFunc(display_translate_rotate)
    glutIdleFunc(display_translate_rotate)
    
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"OpenGL Normal Example")
    
    glutDisplayFunc(display_normal)
    glutIdleFunc(display_normal)
    
    glutMainLoop()

if __name__ == "__main__":
    main()
