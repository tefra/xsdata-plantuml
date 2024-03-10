import os
from pathlib import Path

from click.testing import CliRunner

from xsdata.cli import cli
from xsdata.models.config import GeneratorConfig
from xsdata.utils.testing import ClassFactory, FactoryTestCase
from xsdata_plantuml.generator import PlantUmlGenerator


class PlantUmlGeneratorTests(FactoryTestCase):
    def setUp(self):
        super().setUp()
        config = GeneratorConfig()
        self.generator = PlantUmlGenerator(config)

    def test_render(self):
        classes = [
            ClassFactory.elements(2, package="foo"),
            ClassFactory.elements(3, package="foo"),
        ]

        iterator = self.generator.render(classes)

        actual = [(out.path, out.title, out.source) for out in iterator]
        self.assertEqual(1, len(actual))
        self.assertEqual(3, len(actual[0]))
        self.assertIsInstance(actual[0][0], Path)
        self.assertTrue(actual[0][0].is_absolute())
        self.assertEqual("foo.tests", actual[0][1])
        self.assertEqual(
            str(Path("foo/tests.pu")), str(actual[0][0].relative_to(Path.cwd()))
        )

        output = (
            "@startuml\n"
            "\n"
            "class class_B {\n"
            "    +attr_B : string\n"
            "    +attr_C : string\n"
            "}\n"
            "class class_C {\n"
            "    +attr_D : string\n"
            "    +attr_E : string\n"
            "    +attr_F : string\n"
            "}\n"
            "\n"
            "@enduml"
            "\n"
        )
        self.assertEqual(output, actual[0][2])

    def test_integration(self):
        runner = CliRunner()
        os.chdir(Path(__file__).parent.parent)
        file = Path(__file__).parent.parent.joinpath("samples/order.xsd").absolute()
        result = runner.invoke(cli, [str(file), "-o", "plantuml", "-p", "samples"])

        expected = "Generating package: samples.order"
        self.assertIn(expected, result.output)
