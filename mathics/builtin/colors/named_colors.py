# -*- coding: utf-8 -*-
"""Named Colors

Mathics has definitions for the most common color names which can be used in a graphics or style specification.
"""

from mathics.builtin.base import Builtin

from mathics.core.symbols import strip_context


class _ColorObject(Builtin):
    text_name = None

    def __init__(self, *args, **kwargs):
        super(_ColorObject, self).__init__(*args, **kwargs)
        if self.text_name is None:
            text_name = strip_context(self.get_name()).lower()
        else:
            text_name = self.text_name
        doc = """
            <dl>
            <dt>'%(name)s'
            <dd>represents the color %(text_name)s in graphics.
            </dl>

            >> Graphics[{EdgeForm[Black], %(name)s, Disk[]}, ImageSize->Small]
             = -Graphics-

            >> %(name)s // ToBoxes
             = StyleBox[GraphicsBox[...], ...]
        """ % {
            "name": strip_context(self.get_name()),
            "text_name": text_name,
        }
        if self.__doc__ is None:
            self.__doc__ = doc
        else:
            self.__doc__ = doc + self.__doc__


class Black(_ColorObject):
    """
    >> Black
     = RGBColor[0, 0, 0]
    """

    summary_text = "Black summary still not available"
    rules = {"Black": "RGBColor[0, 0, 0]"}


class Blue(_ColorObject):
    """
    >> Blue
     = RGBColor[0, 0, 1]
    """

    summary_text = "Blue summary still not available"
    rules = {"Blue": "RGBColor[0, 0, 1]"}


class Brown(_ColorObject):
    """
    >> Brown
     = RGBColor[0.6, 0.4, 0.2]
    """

    summary_text = "Brown summary still not available"
    rules = {"Brown": "RGBColor[0.6, 0.4, 0.2]"}


class Cyan(_ColorObject):
    """
    >> Cyan
     = RGBColor[0, 1, 1]
    """

    summary_text = "Cyan summary still not available"
    rules = {"Cyan": "RGBColor[0, 1, 1]"}


class Gray(_ColorObject):
    """
    >> Gray
     = GrayLevel[0.5]
    """

    summary_text = "Gray summary still not available"
    rules = {"Gray": "GrayLevel[0.5]"}


class Green(_ColorObject):
    """
    >> Green
     = RGBColor[0, 1, 0]
    """

    summary_text = "Green summary still not available"
    rules = {"Green": "RGBColor[0, 1, 0]"}


class Magenta(_ColorObject):
    """
    >> Magenta
     = RGBColor[1, 0, 1]
    """

    summary_text = "Magenta summary still not available"
    rules = {"Magenta": "RGBColor[1, 0, 1]"}


class LightBlue(_ColorObject):
    """
    >> Graphics[{LightBlue, EdgeForm[Black], Disk[]}]
     = -Graphics-

    >> Plot[Sin[x], {x, 0, 2 Pi}, Background -> LightBlue]
     = -Graphics-
    """

    text_name = "light blue"
    summary_text = "LightBlue summary still not available"
    rules = {"LightBlue": "RGBColor[0.87, 0.94, 1]"}


class LightBrown(_ColorObject):
    text_name = "light brown"

    summary_text = "LightBrown summary still not available"
    rules = {"LightBrown": "Lighter[Brown, 0.85]"}


class LightCyan(_ColorObject):
    text_name = "light cyan"
    summary_text = "LightCyan summary still not available"
    rules = {"LightCyan": "Lighter[Cyan, 0.9]"}


class LightGray(_ColorObject):
    text_name = "light gray"
    summary_text = "LightGray summary still not available"
    rules = {"LightGray": "Lighter[Gray]"}


class LightGreen(_ColorObject):
    text_name = "light green"
    summary_text = "LightGreen summary still not available"
    rules = {"LightGreen": "Lighter[Green, 0.88]"}


class LightMagenta(_ColorObject):
    text_name = "light magenta"
    summary_text = "LightMagenta summary still not available"
    rules = {"LightMagenta": "Lighter[Magenta]"}


class LightOrange(_ColorObject):
    text_name = "light orange"
    summary_text = "LightOrange summary still not available"
    rules = {"LightOrange": "RGBColor[1, 0.9, 0.8]"}


class LightPink(_ColorObject):
    text_name = "light pink"

    summary_text = "LightPink summary still not available"
    rules = {"LightPink": "Lighter[Pink, 0.85]"}


class LightPurple(_ColorObject):
    text_name = "light purple"
    summary_text = "LightPurple summary still not available"
    rules = {"LightPurple": "Lighter[Purple, 0.88]"}


class LightRed(_ColorObject):
    text_name = "light red"
    summary_text = "LightRed summary still not available"
    rules = {"LightRed": "Lighter[Red, 0.85]"}


class LightYellow(_ColorObject):
    text_name = "light yellow"
    summary_text = "LightYellow summary still not available"
    rules = {"LightYellow": "Lighter[Yellow]"}


class Pink(_ColorObject):
    summary_text = "Pink summary still not available"
    rules = {"Pink": "RGBColor[1.0, 0.5, 0.5]"}


class Purple(_ColorObject):
    summary_text = "Purple summary still not available"
    rules = {"Purple": "RGBColor[0.5, 0, 0.5]"}


class Orange(_ColorObject):
    summary_text = "Orange summary still not available"
    rules = {"Orange": "RGBColor[1, 0.5, 0]"}


class Red(_ColorObject):
    """
    >> Red
     = RGBColor[1, 0, 0]
    """

    summary_text = "Red summary still not available"
    rules = {"Red": "RGBColor[1, 0, 0]"}


class Yellow(_ColorObject):
    """
    >> Yellow
     = RGBColor[1, 1, 0]
    """

    summary_text = "Yellow summary still not available"
    rules = {"Yellow": "RGBColor[1, 1, 0]"}


class White(_ColorObject):
    """
    >> White
     = GrayLevel[1]
    """

    summary_text = "White summary still not available"
    rules = {"White": "GrayLevel[1]"}
