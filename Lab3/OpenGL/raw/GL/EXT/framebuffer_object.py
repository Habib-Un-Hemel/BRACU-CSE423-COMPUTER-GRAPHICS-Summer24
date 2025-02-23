'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_EXT_framebuffer_object'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GL,'GL_EXT_framebuffer_object',error_checker=_errors._error_checker)
GL_COLOR_ATTACHMENT0_EXT=_C('GL_COLOR_ATTACHMENT0_EXT',0x8CE0)
GL_COLOR_ATTACHMENT10_EXT=_C('GL_COLOR_ATTACHMENT10_EXT',0x8CEA)
GL_COLOR_ATTACHMENT11_EXT=_C('GL_COLOR_ATTACHMENT11_EXT',0x8CEB)
GL_COLOR_ATTACHMENT12_EXT=_C('GL_COLOR_ATTACHMENT12_EXT',0x8CEC)
GL_COLOR_ATTACHMENT13_EXT=_C('GL_COLOR_ATTACHMENT13_EXT',0x8CED)
GL_COLOR_ATTACHMENT14_EXT=_C('GL_COLOR_ATTACHMENT14_EXT',0x8CEE)
GL_COLOR_ATTACHMENT15_EXT=_C('GL_COLOR_ATTACHMENT15_EXT',0x8CEF)
GL_COLOR_ATTACHMENT1_EXT=_C('GL_COLOR_ATTACHMENT1_EXT',0x8CE1)
GL_COLOR_ATTACHMENT2_EXT=_C('GL_COLOR_ATTACHMENT2_EXT',0x8CE2)
GL_COLOR_ATTACHMENT3_EXT=_C('GL_COLOR_ATTACHMENT3_EXT',0x8CE3)
GL_COLOR_ATTACHMENT4_EXT=_C('GL_COLOR_ATTACHMENT4_EXT',0x8CE4)
GL_COLOR_ATTACHMENT5_EXT=_C('GL_COLOR_ATTACHMENT5_EXT',0x8CE5)
GL_COLOR_ATTACHMENT6_EXT=_C('GL_COLOR_ATTACHMENT6_EXT',0x8CE6)
GL_COLOR_ATTACHMENT7_EXT=_C('GL_COLOR_ATTACHMENT7_EXT',0x8CE7)
GL_COLOR_ATTACHMENT8_EXT=_C('GL_COLOR_ATTACHMENT8_EXT',0x8CE8)
GL_COLOR_ATTACHMENT9_EXT=_C('GL_COLOR_ATTACHMENT9_EXT',0x8CE9)
GL_DEPTH_ATTACHMENT_EXT=_C('GL_DEPTH_ATTACHMENT_EXT',0x8D00)
GL_FRAMEBUFFER_ATTACHMENT_OBJECT_NAME_EXT=_C('GL_FRAMEBUFFER_ATTACHMENT_OBJECT_NAME_EXT',0x8CD1)
GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE_EXT=_C('GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE_EXT',0x8CD0)
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_3D_ZOFFSET_EXT=_C('GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_3D_ZOFFSET_EXT',0x8CD4)
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_CUBE_MAP_FACE_EXT=_C('GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_CUBE_MAP_FACE_EXT',0x8CD3)
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LEVEL_EXT=_C('GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LEVEL_EXT',0x8CD2)
GL_FRAMEBUFFER_BINDING_EXT=_C('GL_FRAMEBUFFER_BINDING_EXT',0x8CA6)
GL_FRAMEBUFFER_COMPLETE_EXT=_C('GL_FRAMEBUFFER_COMPLETE_EXT',0x8CD5)
GL_FRAMEBUFFER_EXT=_C('GL_FRAMEBUFFER_EXT',0x8D40)
GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT_EXT=_C('GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT_EXT',0x8CD6)
GL_FRAMEBUFFER_INCOMPLETE_DIMENSIONS_EXT=_C('GL_FRAMEBUFFER_INCOMPLETE_DIMENSIONS_EXT',0x8CD9)
GL_FRAMEBUFFER_INCOMPLETE_DRAW_BUFFER_EXT=_C('GL_FRAMEBUFFER_INCOMPLETE_DRAW_BUFFER_EXT',0x8CDB)
GL_FRAMEBUFFER_INCOMPLETE_FORMATS_EXT=_C('GL_FRAMEBUFFER_INCOMPLETE_FORMATS_EXT',0x8CDA)
GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT_EXT=_C('GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT_EXT',0x8CD7)
GL_FRAMEBUFFER_INCOMPLETE_READ_BUFFER_EXT=_C('GL_FRAMEBUFFER_INCOMPLETE_READ_BUFFER_EXT',0x8CDC)
GL_FRAMEBUFFER_UNSUPPORTED_EXT=_C('GL_FRAMEBUFFER_UNSUPPORTED_EXT',0x8CDD)
GL_INVALID_FRAMEBUFFER_OPERATION_EXT=_C('GL_INVALID_FRAMEBUFFER_OPERATION_EXT',0x0506)
GL_MAX_COLOR_ATTACHMENTS_EXT=_C('GL_MAX_COLOR_ATTACHMENTS_EXT',0x8CDF)
GL_MAX_RENDERBUFFER_SIZE_EXT=_C('GL_MAX_RENDERBUFFER_SIZE_EXT',0x84E8)
GL_RENDERBUFFER_ALPHA_SIZE_EXT=_C('GL_RENDERBUFFER_ALPHA_SIZE_EXT',0x8D53)
GL_RENDERBUFFER_BINDING_EXT=_C('GL_RENDERBUFFER_BINDING_EXT',0x8CA7)
GL_RENDERBUFFER_BLUE_SIZE_EXT=_C('GL_RENDERBUFFER_BLUE_SIZE_EXT',0x8D52)
GL_RENDERBUFFER_DEPTH_SIZE_EXT=_C('GL_RENDERBUFFER_DEPTH_SIZE_EXT',0x8D54)
GL_RENDERBUFFER_EXT=_C('GL_RENDERBUFFER_EXT',0x8D41)
GL_RENDERBUFFER_GREEN_SIZE_EXT=_C('GL_RENDERBUFFER_GREEN_SIZE_EXT',0x8D51)
GL_RENDERBUFFER_HEIGHT_EXT=_C('GL_RENDERBUFFER_HEIGHT_EXT',0x8D43)
GL_RENDERBUFFER_INTERNAL_FORMAT_EXT=_C('GL_RENDERBUFFER_INTERNAL_FORMAT_EXT',0x8D44)
GL_RENDERBUFFER_RED_SIZE_EXT=_C('GL_RENDERBUFFER_RED_SIZE_EXT',0x8D50)
GL_RENDERBUFFER_STENCIL_SIZE_EXT=_C('GL_RENDERBUFFER_STENCIL_SIZE_EXT',0x8D55)
GL_RENDERBUFFER_WIDTH_EXT=_C('GL_RENDERBUFFER_WIDTH_EXT',0x8D42)
GL_STENCIL_ATTACHMENT_EXT=_C('GL_STENCIL_ATTACHMENT_EXT',0x8D20)
GL_STENCIL_INDEX16_EXT=_C('GL_STENCIL_INDEX16_EXT',0x8D49)
GL_STENCIL_INDEX1_EXT=_C('GL_STENCIL_INDEX1_EXT',0x8D46)
GL_STENCIL_INDEX4_EXT=_C('GL_STENCIL_INDEX4_EXT',0x8D47)
GL_STENCIL_INDEX8_EXT=_C('GL_STENCIL_INDEX8_EXT',0x8D48)
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint)
def glBindFramebufferEXT(target,framebuffer):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint)
def glBindRenderbufferEXT(target,renderbuffer):pass
@_f
@_p.types(_cs.GLenum,_cs.GLenum)
def glCheckFramebufferStatusEXT(target):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glDeleteFramebuffersEXT(n,framebuffers):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glDeleteRenderbuffersEXT(n,renderbuffers):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum,_cs.GLuint)
def glFramebufferRenderbufferEXT(target,attachment,renderbuffertarget,renderbuffer):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum,_cs.GLuint,_cs.GLint)
def glFramebufferTexture1DEXT(target,attachment,textarget,texture,level):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum,_cs.GLuint,_cs.GLint)
def glFramebufferTexture2DEXT(target,attachment,textarget,texture,level):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum,_cs.GLuint,_cs.GLint,_cs.GLint)
def glFramebufferTexture3DEXT(target,attachment,textarget,texture,level,zoffset):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glGenFramebuffersEXT(n,framebuffers):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glGenRenderbuffersEXT(n,renderbuffers):pass
@_f
@_p.types(None,_cs.GLenum)
def glGenerateMipmapEXT(target):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glGetFramebufferAttachmentParameterivEXT(target,attachment,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glGetRenderbufferParameterivEXT(target,pname,params):pass
@_f
@_p.types(_cs.GLboolean,_cs.GLuint)
def glIsFramebufferEXT(framebuffer):pass
@_f
@_p.types(_cs.GLboolean,_cs.GLuint)
def glIsRenderbufferEXT(renderbuffer):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLsizei,_cs.GLsizei)
def glRenderbufferStorageEXT(target,internalformat,width,height):pass
