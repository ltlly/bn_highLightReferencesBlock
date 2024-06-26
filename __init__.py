from binaryninja import *
from binaryninjaui import UIContext


def highLightBlock_high(bv: BinaryView, inst: HighLevelILInstruction):
    func = inst.function.source_function
    hlil = inst.function

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
        block.highlight = HighlightStandardColor.BlueHighlightColor


def resetBlockHighlight_high(bv: BinaryView, inst: HighLevelILInstruction):
    func = inst.function.source_function
    hlil = inst.function

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
        block.highlight = HighlightStandardColor.NoHighlightColor


def highLightBlock_middle(bv: BinaryView, inst: MediumLevelILInstruction):
    func = inst.function.source_function
    mlil = inst.function

    ctx = UIContext.activeContext()
    h = ctx.contentActionHandler()
    a = h.actionContext()
    token_state = a.token
    var = Variable.from_identifier(func, token_state.token.value)
    uses =  mlil.get_var_uses(var)
    defines = mlil.get_var_definitions(var)
    references = uses + defines
    references = list(set(references))
    for ref in references:
        block = mlil.get_basic_block_at(ref.instr_index)
        block.highlight = HighlightStandardColor.BlueHighlightColor


def resetBlockHighlight_middle(bv: BinaryView, inst: MediumLevelILInstruction):
    func = inst.function.source_function
    mlil = inst.function

    ctx = UIContext.activeContext()
    h = ctx.contentActionHandler()
    a = h.actionContext()
    token_state = a.token
    var = Variable.from_identifier(func, token_state.token.value)

    uses = mlil.get_var_uses(var)
    defines = mlil.get_var_definitions(var)
    references = uses + defines
    references = list(set(references))

    for ref in references:
        block = mlil.get_basic_block_at(ref.instr_index)
        block.highlight = HighlightStandardColor.NoHighlightColor


def resetAllBlockHighlight(bv: BinaryView, inst: HighLevelILInstruction):
    hlil = inst.function
    func = inst.function.source_function
    mlil = func.mlil
    for block in hlil.basic_blocks:
        block.highlight = HighlightStandardColor.NoHighlightColor
    for block in mlil.basic_blocks:
        block.highlight = HighlightStandardColor.NoHighlightColor
def isV(bv: BinaryView, inst: HighLevelILInstruction):
    return True


PluginCommand.register_for_high_level_il_instruction(
    "highLight\\hightlight", "", highLightBlock_high, isV)

PluginCommand.register_for_high_level_il_instruction(
    "highLight\\undoHightLight", "", resetBlockHighlight_high, isV)


PluginCommand.register_for_high_level_il_instruction(
    "highLight\\resetAll", "", resetAllBlockHighlight, isV)




PluginCommand.register_for_medium_level_il_instruction(
    "highLight\\hightlight ", "", highLightBlock_middle, isV)

PluginCommand.register_for_medium_level_il_instruction(
    "highLight\\undoHightLight ", "", resetBlockHighlight_middle, isV)

PluginCommand.register_for_medium_level_il_instruction(
    "highLight\\resetAll ", "", resetAllBlockHighlight, isV)
