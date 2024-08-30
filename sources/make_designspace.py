import os

from fontTools.designspaceLib import DesignSpaceDocument, AxisDescriptor, SourceDescriptor, InstanceDescriptor

root = os.getcwd()
doc = DesignSpaceDocument()

familyName = "Samaano"

#------
# axes
#------

a1 = AxisDescriptor()
a1.maximum = 900
a1.minimum = 100
a1.default = 100
a1.name = "weight"
a1.tag = "wght"
doc.addAxis(a1)

#---------
# masters
#---------

s0 = SourceDescriptor()
s0.path = "Samaano-Thin.ufo"
s0.name = "master.Samano.Thin.0"
s0.familyName = familyName
s0.styleName = "Thin"
s0.location = dict(weight=100, width=100)
s0.copyLib = True
s0.copyInfo = True
s0.copyGroups = True
s0.copyFeatures = True
doc.addSource(s0)

s1 = SourceDescriptor()
s1.path = "Samaano-Bold.ufo"
s0.name = "master.Samaano.Bold.0"
s1.familyName = familyName
s1.styleName = "Bold"
s1.location = dict(weight=900, width=0)
doc.addSource(s1)

#--------
# saving
#--------

path = os.path.join(root, "Samaano.designspace")
doc.write(path)
