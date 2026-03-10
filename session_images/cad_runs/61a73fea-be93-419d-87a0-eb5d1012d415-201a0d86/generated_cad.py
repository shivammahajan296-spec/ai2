import cadquery as cq

# Parameters
height = 80.0  # Overall height of the jar
outer_diameter = 50.0  # Outer diameter of the jar
wall_thickness = 2.0  # Wall thickness
groove_depth = 1.5  # Depth of the screw thread groove
fillet_radius = 2.0  # Fillet radius for edges
thread_pitch = 2.0  # Thread pitch for the screw closure

# Create the main body of the jar
jar_body = (
    cq.Workplane("XY")
    .circle(outer_diameter / 2)
    .extrude(height)
)

# Create the hollow part of the jar
hollow_body = (
    cq.Workplane("XY")
    .circle((outer_diameter / 2) - wall_thickness)
    .extrude(height)
)

# Subtract the hollow part from the jar body
jar = jar_body.cut(hollow_body)

# Create the screw thread using a helical sweep
screw_thread = (
    cq.Workplane("XY")
    .circle((outer_diameter / 2) - wall_thickness)
    .workplane(offset=height)
    .screw_thread(thread_pitch, height, 0.5, 1.0, 0.0, 0.0)
)

# Combine the jar with the screw thread
final_jar = jar.union(screw_thread)

# Apply fillets to the edges
final_jar = final_jar.edges().fillet(fillet_radius)

# Export to STEP file
step_path = "C:/Users/e430584/Desktop/Projects/2d to 3D for EST/App/v5 - Copy (2)/output/jar_model.step"
cq.exporters.export(final_jar, step_path)