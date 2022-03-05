class Error(Exception):
    """Base class for other exceptions"""
    pass

class ImageNotGenerated(Error):
    """Raised when image is not generated"""
    def __init__(self):
        super().__init__("Image has not been generated")