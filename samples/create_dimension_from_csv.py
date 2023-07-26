import pandas as pd
from TM1py import TM1Service, Hierarchy, Dimension

DIMENSION_NAME = "TM1py Products"

TM1_PARAMS = {
    "address": "localhost",
    "port": "12354",
    "ssl": "True",
    "user": "admin",
    "password": "apple"
}

# read CSV
df = pd.read_csv("products.csv")

# first column has the element name!
element_name_column = df.columns[0]
# other columns have the attribute names
attribute_columns = df.columns[1:]

# create a hierarchy structure in Python
hierarchy = Hierarchy(
    name=DIMENSION_NAME,
    dimension_name=DIMENSION_NAME)

# Add 'All' Consolidation to Hierarchy
hierarchy.add_element("All Products", element_type="Consolidated")
for attribute_names in attribute_columns:
    hierarchy.add_element_attribute(
        name=attribute_names,
        attribute_type="String")

# Add leaves to Hierarchy based on values in column 0
for element_name in df[element_name_column].values:
    hierarchy.add_component(
        parent_name="All Products",
        component_name=element_name,
        weight=1)
dimension = Dimension(name=DIMENSION_NAME, hierarchies=[hierarchy])

# Connect to TM1
with TM1Service(**TM1_PARAMS) as tm1:

    # send dimension to TM1 with TM1py
    tm1.dimensions.update_or_create(dimension)

    # melt attributes dataframe from n columns to 3 columns: product, attribute, value
    df_attributes = df.melt(id_vars=element_name_column, value_vars=attribute_columns)

    # write attribute values
    tm1.cells.write_dataframe(
        "}ElementAttributes_" + DIMENSION_NAME,
        df_attributes,
        use_blob=True)
