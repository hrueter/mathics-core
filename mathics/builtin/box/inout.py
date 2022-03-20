# -*- coding: utf-8 -*-

from mathics.builtin.base import Builtin

from mathics.core.attributes import hold_all_complete, protected, read_protected


class ButtonBox(Builtin):
    """
    <dl>
    <dt>'ButtonBox[$boxes$]'
        <dd> is a low-level box construct that represents a button in a
    notebook expression.
    </dl>
    """

    summary_text = "ButtonBox summary still not available"
    summary_text = "ButtonBox summary still not available"
    attributes = protected | read_protected


class InterpretationBox(Builtin):
    """
    <dl>
    <dt>'InterpretationBox[{...}]'
        <dd> is a low-level box construct that displays as
    boxes but is interpreted on input as expr.
    </dl>
    """

    summary_text = "InterpretationBox summary still not available"
    summary_text = "InterpretationBox summary still not available"
    attributes = hold_all_complete | protected | read_protected


class SubscriptBox(Builtin):
    summary_text = "SubscriptBox summary still not available"
    pass


class SubsuperscriptBox(Builtin):
    summary_text = "SubsuperscriptBox summary still not available"
    pass


class SuperscriptBox(Builtin):
    summary_text = "SuperscriptBox summary still not available"
    pass


class RowBox(Builtin):
    """
    <dl>
    <dt>'RowBox[{...}]'
        <dd>is a box construct that represents a sequence of boxes
        arranged in a horizontal row.
    </dl>
    """

    summary_text = "RowBox summary still not available"
    pass


class StyleBox(Builtin):
    """
    <dl>
    <dt>'StyleBox[boxes, options]'
        <dd> is a low-level representation of boxes
     to be shown with the specified option settings.
    <dt>'StyleBox[boxes, style]'
        <dd> uses the option setting for the specified style in
    the current notebook.
    </dl>
    """

    summary_text = "StyleBox summary still not available"
    attributes = protected | read_protected


class TagBox(Builtin):
    """
    <dl>
    <dt>'TagBox[boxes, tag]'
        <dd> is a low-level box construct that displays as
    boxes but is interpreted on input as expr
    </dl>
    """

    summary_text = "TagBox summary still not available"
    attributes = hold_all_complete | protected | read_protected


class TemplateBox(Builtin):
    """
    <dl>
    <dt>'TemplateBox[{$box_1$, $box_2$,...}, tag]'
        <dd>is a low-level box structure that parameterizes the display and evaluation     of the boxes $box_i$ .
    </dl>
    """

    summary_text = "TemplateBox summary still not available"
    attributes = hold_all_complete | protected | read_protected


class TooltipBox(Builtin):
    """
    <dl>
    <dt>'TooltipBox[{...}]'
        <dd>undocumented...
    </dl>
    """

    summary_text = "TooltipBox summary still not available"
    pass
