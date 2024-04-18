from OpenGL.GLUT import *
from OpenGL.GL import *

import sys
def draw():
    ##uzaklk 0 uzak 0.5 orta 1 yakn
    # glutWireTeapot(0.8)
    #uzzaklık,360 derceye kaç eşit parcaya bolecek, orta noktadan uca kadar kaç yuvaralak cizilecke
    # glutWireSphere (0.5, 18, 50)
    #uzaklık
    # glutWireCube (0.5)
    # glutWireTetrahedron ()
    # uzaklık,dondürme  ,dısarıya dogru etrafında gezen kac cizgi var,360 derece kaça boluncek
    glutWireTorus(0.5,0.001,20,5)
    glFlush()
glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
glutInitWindowSize(500,500)
glutInitWindowPosition(100,100)
glutCreateWindow(bytes("Merhaba PyOpenG","ascii"))
glutDisplayFunc(draw)
glutMainLoop()