from omni.isaac.examples.base_sample import BaseSample
import numpy as np
from omni.isaac.core.objects import DynamicCuboid

class HelloWorld(BaseSample):
    def __init__(self) -> None:
        super().__init__()
        return

    def setup_scene(self):
        world = self.get_world()
        world.scene.add_default_ground_plane()
        fancy_cube = world.scene.add(
            DynamicCuboid(
                prim_path="/World/random_cube",
                name="fancy_cube",
                position=np.array([0, 0, 1.0]),
                scale=np.array([0.5015, 0.3015, 0.5015]),
                color=np.array([0, 0, 1.0]),
            ))
        test_cube = world.scene.add(
            DynamicCuboid(
                prim_path="/World/random1_cube",
                name="test1_cube",
                position=np.array([1.0, 1.0, 1.0]),
                scale=np.array([0.2, 0.3015, 0.5015]),
                color=np.array([0, 0, 1.0]),
            ))
        return

    async def setup_post_load(self):
        self._world = self.get_world()
        self._cube = self._world.scene.get_object("fancy_cube")
        self._test_cube = self._world.scene.get_object("test1_cube") 
        self._world.add_physics_callback("sim_step", callback_fn=self.print_cube_info) #callback names have to be unique
        return

    # here we define the physics callback to be called before each physics step, all physics callbacks must take
    # step_size as an argument
    def print_cube_info(self, step_size):
        position, orientation = self._cube.get_world_pose()
        pos, orient = self._test_cube.get_world_pose()
        #linear_velocity = self._cube.get_linear_velocity()
        # will be shown on terminal
        print("Cube position is : " + str(position))
        print("Test Cube position is : " + str(pos))
        #print("Cube's orientation is : " + str(orientation))
        #print("Cube's linear velocity is : " + str(linear_velocity))