import maya.cmds as cmds
import mtoa.utils as mutils

# create three lights in relation to an object at the origin
# get location of the top of selected maya object or group

# create placeholder object to connect lights to height
cylinder_obj = cmds.polyCylinder(name="cylinder", height=2, radius=1)

class lights():

    def __init__(self):
        self.cylinder_height = 2
        self.key_exposure = 10.0
        self.key_color = (0.5, 0.5, 0.5)


    def create(self):
        self.create_key_lgt()

    def create_key_lgt(self):
        self.keylgt_node, self.keylgt_obj = mutils.createLocator("aiAreaLight", asLight=True)
        cmds.xform(self.keylgt_obj, translation=(0,self.cylinder_height, 2), worldSpace=True)
        cmds.setAttr(f"{self.keylgt_node}.aiExposure", self.key_exposure)
        cmds.setAttr(f"{self.keylgt_node}.color", *self.key_color, type="double3")

    # create key light
    # create in relation to a selected object's top location
    # set light color attribute with 3 floats
    # get number (float) for light exposure

# create fill light
# create skydome light
# add photo file to connect to skydome, turn off visibility
# get number (float) for light exposure

# create rim light
# create in relation to a selected object's top location OPPOSITE of key light
# set light color attribute with 3 floats
# get number (float) for light exposure

lgt = lights()
lgt.create()
