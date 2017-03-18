#!/home/justin/opt/blender-2.78c-linux-glibc219-x86_64/2.78/python/bin/python3.5m 

import base
import bpy
from mathutils import Vector

def test_clear():
    bpy.ops.mesh.primitive_ico_sphere_add()
    # There are 3 objects in the startup scene
    assert(len(bpy.data.objects) == 4)
    base.clear()
    assert(len(bpy.data.objects) == 0)

def test_clear_names():
    base.clear()
    bpy.ops.mesh.primitive_ico_sphere_add()
    bpy.ops.mesh.primitive_ico_sphere_add()
    bpy.ops.mesh.primitive_ico_sphere_add()
    assert(len(bpy.data.objects) == 3)
    name1 = bpy.data.objects[0].name
    name2 = bpy.data.objects[1].name
    name3 = bpy.data.objects[2].name
    base.clear(names=(name2,))
    assert(len(bpy.data.objects) == 2)
    remaining_name = bpy.data.objects[0].name
    assert(remaining_name == name1)

def test_sphere_noargs():
    base.clear()
    name = base.sphere()
    sphere = bpy.data.objects[0]
    assert(len(bpy.data.objects) == 1)
    assert(name == sphere.name)
    assert(Vector((0,0,0)) == sphere.location)

def test_sphere_postion():
    base.clear()
    position = Vector((1,3,-1))
    name = base.sphere(location=position)
    sphere = bpy.data.objects[0]
    assert(position == sphere.location)

def test_cube_noargs():
    base.clear()
    name = base.cube()
    cube = bpy.data.objects[0]
    assert(len(bpy.data.objects) == 1)
    assert(name == cube.name)
    assert(Vector((0,0,0)) == cube.location)
