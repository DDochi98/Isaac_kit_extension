from omni.isaac.examples.base_sample import BaseSample
import numpy as np
#Can be used to create a new cube or to point to an already existing cube in stage
from omni.isaac.core.objects import DynamicCuboid

class HelloWorld(BaseSample):
    def __init__(self) -> None:
        super().__init__()
        return

    #This function is called to setup the assets in the scene for the first time
    #Class variables should not be assigned here, since this function is not called
    #after a hot-reload, its only called to load the world starting from an EMPTY stage
    def setup_scene(self):
        #A wolrd is defined in the BaseSample, can be accessed everywhere EXCEPT __init__
        world = self.get_world()
        world.scene.add_default_ground_plane() #adds a default ground plane to the scene
        fancy_cube = world.scene.add(
            DynamicCuboid(
                prim_path="/World/random_cube", # The prim path of the cube in the USD stage
                name="fancy_cube",              # The unique name used to retrieve the object from the scene later on 
                position=np.array([0, 0, 1.0]), # Using the current stage units which is in meters by default.
                scale=np.array([0.5015, 0.3015, 0.5015]),   #most arguments accept mainly numpy arrays
                color=np.array([0, 0, 1.0]),                #RGB channels, going from 0-1
            ))
        return

    # Here we assign the class's variables
    # this function is called after load button is pressed
    # regardless starting from an empty stage or not
    # this is called after setup_scene and after
    # one physics time step to propagate appropriate
    # physics hadles which are needed to retrieve
    # many physical properites of the different objects 
    async def setup_post_load(self):
        self._world = self.get_world()
        self._cube = self._world.scene.get_object("fancy_cube")
        # continuously Inspecting the Object Properties during Simulation
        # callback names have to be unique
        self._world.add_physics_callback("sim_step", callback_fn=self.print_cube_info) 
        return

    # here we define the physics callback to be called before each physics step, all physics callbacks must take
    # step_size as an argument
    def print_cube_info(self, step_size):
        position, orientation = self._cube.get_world_pose()
        linear_velocity = self._cube.get_linear_velocity()

        #linear_velocity = self._cube.get_linear_velocity()
        # will be shown on terminal
        print("Cube position is : " + str(position))
        print("Cube's orientation is : " + str(orientation))
        print("Cube's linear velocity is : " + str(linear_velocity))
