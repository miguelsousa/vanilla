from vanillaBase import VanillaBaseObject


class Group(VanillaBaseObject):
    
    """
    An invisible container for controls.
    
    To add a control to a group, simply set it as an attribute of the group.
    
    pre.
    from vanilla import *
     
    class GroupDemo(object):
        
        def __init__(self):
            self.w = Window((150, 50))
            self.w.group = Group((10, 10, -10, -10))
            self.w.group.text = TextBox((0, 0, -0, -0),
                                    'This is a group')
            self.w.open()
            
    GroupDemo()
    
    No special naming is required for the attributes. However, each attribute must have a unique name.
    """
    
    def __init__(self, posSize):
        """
        *posSize* Tuple of form (left, top, width, height) representing the position and size of the group.
        """
        self._setupView("NSView", posSize)
    
    def getNSView(self):
        """
        Return the _NSView_ that this object wraps.
        """
        return self._nsObject
