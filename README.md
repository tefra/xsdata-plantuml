# [xsdata](https://pypi.org/project/xsdata/) - PlantUML plugin

Generate [PlantUML](https://plantuml.com/class-diagram) class diagrams from xml schemas,
wsdl definitions and directly from xml documents.

[![image](https://github.com/tefra/xsdata-plantuml/workflows/tests/badge.svg)](https://github.com/tefra/xsdata-plantuml/actions)
[![image](https://codecov.io/gh/tefra/xsdata-plantuml/branch/main/graph/badge.svg)](https://codecov.io/gh/tefra/xsdata-plantuml)
[![image](https://www.codefactor.io/repository/github/tefra/xsdata-plantuml/badge)](https://www.codefactor.io/repository/github/tefra/xsdata-plantuml)
[![image](https://img.shields.io/pypi/pyversions/xsdata-plantuml.svg)](https://pypi.org/pypi/xsdata-plantuml/)
[![image](https://img.shields.io/pypi/v/xsdata-plantuml.svg)](https://pypi.org/pypi/xsdata-plantuml/)

---

## Usage

```console
$ pip install xsdata-plantuml

$ xsdata samples/order.xsd --output plantuml --package samples
```

```
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
```

[image](https://github.com/tefra/xsdata-plantuml/raw/main/samples/order.svg)
