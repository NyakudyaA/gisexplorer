project = QgsProject.instance()

for layer in project.mapLayers().values():
    if layer.type() == QgsMapLayer.VectorLayer:
        # Get the geometry type
        layer_geom_type = QgsWkbTypes.displayString(layer.wkbType()).upper()

        # Get the field names and data types
        fields = layer.fields()
        field_list = [f"{field.name()}: {field.typeName()}" for field in fields]

        print(f"Layer: {layer.name()}")
        print(f"Geometry Type: {layer_geom_type}")
        print("Fields:")
        for field in field_list:
            print(f"  - {field}")
        print()
