from binaryninja import *


def highLightBlockHigh(bv: BinaryView, inst: HighLevelILInstruction):
    log_info(f"My plugin was called on inst {inst} in bv `{bv}`")
    hlilFunc = inst.function
    vars = inst.vars
    for var in vars:
        uses = [x.instr for x in hlilFunc.get_var_uses(var)]
        defines = hlilFunc.get_var_definitions(var)
        references = uses + defines
        references = list(set(references))
        log_info(f"var {var} : {references} ")
        for ref in references:
            block = hlilFunc.get_basic_block_at(ref.instr_index)
            block.highlight = HighlightStandardColor.BlueHighlightColor


def resetBlockHighlightHigh(bv: BinaryView, inst: HighLevelILInstruction):
    log_info(f"My plugin:{inst} in bv `{bv}`")
    hlilFunc = inst.function
    vars = inst.vars
    for var in vars:
        uses = [x.instr for x in hlilFunc.get_var_uses(var)]
        defines = hlilFunc.get_var_definitions(var)
        references = uses + defines
        references = list(set(references))
        for ref in references:
            block = hlilFunc.get_basic_block_at(ref.instr_index)
            block.highlight = HighlightStandardColor.NoHighlightColor


def resetAllBlockHighlight(bv: BinaryView, inst: HighLevelILInstruction):
    hlilFunc = inst.function
    for block in hlilFunc.basic_blocks:
        block.highlight = HighlightStandardColor.NoHighlightColor


def isV(bv: BinaryView, inst: HighLevelILInstruction):
    return True


PluginCommand.register_for_high_level_il_instruction(
    "highLight\\hightlight", "", highLightBlockHigh, isV)

PluginCommand.register_for_high_level_il_instruction(
    "highLight\\undoHightLight", "", resetBlockHighlightHigh, isV)


PluginCommand.register_for_high_level_il_instruction(
    "highLight\\resetAll", "", resetAllBlockHighlight, isV)
