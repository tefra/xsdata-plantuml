`xsData <https://pypi.org/project/xsdata/>`_ PlantUML plugin
============================================================

Generate `PlantUML <https://plantuml.com/class-diagram>`_ class diagrams from xml
schemas, wsdl definitions and directly from xml documents.

.. image:: https://github.com/tefra/xsdata-plantuml/workflows/tests/badge.svg
    :target: https://github.com/tefra/xsdata-plantuml/actions

.. image:: https://codecov.io/gh/tefra/xsdata-plantuml/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/tefra/xsdata-plantuml

.. image:: https://www.codefactor.io/repository/github/tefra/xsdata-plantuml/badge
   :target: https://www.codefactor.io/repository/github/tefra/xsdata-plantuml

.. image:: https://img.shields.io/pypi/pyversions/xsdata-plantuml.svg
    :target: https://pypi.org/pypi/xsdata-plantuml/

.. image:: https://img.shields.io/pypi/v/xsdata-plantuml.svg
    :target: https://pypi.org/pypi/xsdata-plantuml/

Usage
=====

.. code:: bash

    $ pip install xsdata-plantuml

    $ xsdata samples/order.xsd --output plantuml --package samples


.. code::

    @startuml

    class Items {
        +item : item[]
    }
    Items +-- item
    class item {
        +productName : string
        +quantity : positiveInteger
        +USPrice : decimal
        +comment : string
        +shipDate : date
        +partNum : string
    }
    class PurchaseOrderType {
        +shipTo : USAddress
        +billTo : USAddress
        +comment : string
        +items : Items
        +orderDate : date
    }
    class USAddress {
        +name : string
        +street : string
        +city : string
        +state : string
        +zip : decimal
        +country : NMTOKEN
    }
    class comment {
        +@value : string
    }
    class purchaseOrder {
    }
    purchaseOrder *- PurchaseOrderType

    @enduml


.. image:: https://github.com/tefra/xsdata-plantuml/raw/master/samples/order.svg
