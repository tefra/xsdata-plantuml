from xsdata.codegen.writer import CodeWriter

from xsdata_plantuml.generator import PlantUmlGenerator

CodeWriter.register_generator("plantuml", PlantUmlGenerator)
