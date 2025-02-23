'''OpenGL extension NV.framebuffer_multisample

This module customises the behaviour of the 
OpenGL.raw.GLES2.NV.framebuffer_multisample to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension extends the framebuffer object framework to
	enable multisample rendering.
	
	The new operation RenderbufferStorageMultisampleNV() allocates
	storage for a renderbuffer object that can be used as a multisample
	buffer.  A multisample render buffer image differs from a
	single-sample render buffer image in that a multisample image has a
	number of SAMPLES that is greater than zero.  No method is provided
	for creating multisample texture images.
	
	All of the framebuffer-attachable images attached to a framebuffer
	object must have the same number of SAMPLES or else the framebuffer
	object is not "framebuffer complete".  If a framebuffer object with
	multisample attachments is "framebuffer complete", then the
	framebuffer object behaves as if SAMPLE_BUFFERS is one.
	
	A resolve operation is executed by calling
	BlitFramebufferNV (provided by the NV_framebuffer_blit
	extension) where the source is a multisample framebuffer object
	and the destination is a single-sample framebuffer object.
	Source and destination framebuffer may be either application-created
	or window-system provided.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/NV/framebuffer_multisample.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLES2 import _types, _glgets
from OpenGL.raw.GLES2.NV.framebuffer_multisample import *
from OpenGL.raw.GLES2.NV.framebuffer_multisample import _EXTENSION_NAME

def glInitFramebufferMultisampleNV():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION