'''OpenGL extension ARB.multisample

This module customises the behaviour of the 
OpenGL.raw.GLX.ARB.multisample to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension provides a mechanism to antialias all GL primitives:
	points, lines, polygons, bitmaps, and images.  The technique is to
	sample all primitives multiple times at each pixel.  The color
	sample values are resolved to a single, displayable color each time
	a pixel is updated, so the antialiasing appears to be automatic at
	the application level.  Because each sample includes depth and
	stencil information, the depth and stencil functions perform
	equivalently to the single-sample mode.
	
	An additional buffer, called the multisample buffer, is added to
	the framebuffer.  Pixel sample values, including color, depth, and
	stencil values, are stored in this buffer.  When the framebuffer
	includes a multisample buffer, it does not also include separate
	depth or stencil buffers, even if the multisample buffer does not
	store depth or stencil values.  Color buffers (left/right, front/
	back, and aux) do coexist with the multisample buffer, however.
	
	Multisample antialiasing is most valuable for rendering polygons,
	because it requires no sorting for hidden surface elimination, and
	it correctly handles adjacent polygons, object silhouettes, and
	even intersecting polygons.  If only points or lines are being
	rendered, the "smooth" antialiasing mechanism provided by the base
	GL may result in a higher quality image.  This extension is
	designed to allow multisample and smooth antialiasing techniques
	to be alternated during the rendering of a single scene.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ARB/multisample.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLX import _types, _glgets
from OpenGL.raw.GLX.ARB.multisample import *
from OpenGL.raw.GLX.ARB.multisample import _EXTENSION_NAME

def glInitMultisampleARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION