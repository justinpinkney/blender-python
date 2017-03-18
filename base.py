import bpy
import mathutils

def clear(names=None):
    '''Clear all objects from a scene.'''
    if not names:
        for object in bpy.data.objects:
            object.select = True
            bpy.ops.object.delete()
    else:
        for object in bpy.data.objects:
            print('checking object {}'.format(object.name))
            if object.name in names:
                print('deleting object {}'.format(object.name))
                object.select = True
            else:
                print('preserving object {}'.format(object.name))
                object.select = False
        bpy.ops.object.delete()


def sphere(location=(0,0,0),
             rotation=(0,0,0),
             matrix=None,
             subdivisions=3,
             size=1):
    '''Add a sphere to the current scene.'''

    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=subdivisions, 
                                            size=size, 
                                            location=location, 
                                            rotation=rotation)
    bpy.ops.object.shade_smooth()
    if matrix:
        bpy.context.selected_objects[0].matrix_world = matrix
    
    return bpy.context.selected_objects[0].name


def cube(location=(0,0,0),
             rotation=(0,0,0),
             matrix=None,
             subdivisions=3,
             size=1):
    '''Add a cube to the current scene.'''

    bpy.ops.mesh.primitive_cube_add(location=location, 
                                            rotation=rotation)
    if matrix:
        bpy.context.selected_objects[0].matrix_world = matrix
    
    return bpy.context.selected_objects[0].name


if __name__ == '__main__':
    clear()
    print(sphere(location=mathutils.noise.random_unit_vector(), size=0.2))
