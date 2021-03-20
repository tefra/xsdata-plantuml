xsData codegen PlantUML plugin
==============================

Generate `PlantUML <https://plantuml.com/class-diagram>`_ class diagrams from xml
schemas, wsdl definitions and directly from xml documents.


Usage
=====


.. code-block:: bash

    $ pip install xsdata-plantuml

    $ xsdata samples/order.xsd --output plantuml --package samples


.. literalinclude:: samples/order.pu

