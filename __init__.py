from binaryninja import *
from binaryninjaui import UIContext


def highLightBlock(bv: BinaryView, func: Function):
    hlil = func.hlil
    mlil = func.mlil
    ctx = UIContext.activeContext()
    h = ctx.contentActionHandler()
    a = h.actionContext()
    token_state = a.token
    var = Variable.from_identifier(func, token_state.token.value)

    uses = hlil.get_var_uses(var)
    defines = hlil.get_var_definitions(var)
    references = uses + defines
    references = list(set(references))
    for ref in references:
        block = hlil.get_basic_block_at(ref.instr_index)
        if not block:
            continue
        block.highlight = HighlightStandardColor.BlueHighlightColor
    uses = mlil.get_var_uses(var)
    defines = mlil.get_var_definitions(var)
    references = uses + defines
    references = list(set(references))
    for ref in references:
        block = mlil.get_basic_block_at(ref.instr_index)
        if not block:
            continue
        block.highlight = HighlightStandardColor.BlueHighlightColor


def resetAllBlockHighlight(bv: BinaryView, func: Function):
    hlil = func.hlil
    mlil = func.mlil
    for block in hlil.basic_blocks:
        block.highlight = HighlightStandardColor.NoHighlightColor
    for block in mlil.basic_blocks:
        block.highlight = HighlightStandardColor.NoHighlightColor


def isV(bv: BinaryView, inst: HighLevelILInstruction):
    return True


PluginCommand.register_for_function(
    "highLight\\hightlight", "", highLightBlock, isV)


PluginCommand.register_for_function(
    "highLight\\resetAll", "", resetAllBlockHighlight, isV)

