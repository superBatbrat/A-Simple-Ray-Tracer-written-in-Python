from scene import objects, lights, BGCOLOR

def ray_trace(original_ray):
    obj = get_first_intersection(original_ray)
    if obj is not None:
        point_color = obj.color
    else:
        point_color = BGCOLOR
    
    return point_color

def get_first_intersection(ray):
   closest_intersection_distance = 10000.0
   closest_intersected_object = None
   for obj in objects:
        result = obj.find_intersection(ray)
        if result.hit is True:
            if result.dist < closest_intersection_distance:
                closest_intersected_object = obj
                closest_intersection_distance = result.dist

   return closest_intersected_object
