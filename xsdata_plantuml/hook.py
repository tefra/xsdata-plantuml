from xsdata.codegen.writer import CodeWriter

from xsdata_plantuml.formats.plantuml.generator import PlantUmlGenerator

CodeWriter.register_generator("plantuml", PlantUmlGenerator)