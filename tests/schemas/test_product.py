from pydantic import ValidationError

import pytest
from store.schemas.product import ProductIn
from tests.factories import product_data


def test_schemas_return_success():
    data = product_data()
    product = ProductIn.model_validate(data)

    assert product.name == "Samsung S23"


def test_schemas_return_raise():
    data = {"name": "Samsung S23", "quantity": 10, "price": "5.600"}

    with pytest.raises(ValidationError) as err:
        ProductIn.model_validate(data)

    assert err.value.errors()[0] == {
        "type": "missing",
        "loc": ("status",),
        "msg": "Field required",
        "input": {"name": "Samsung S23", "quantity": 10, "price": "5.600"},
        "url": "https://errors.pydantic.dev/2.7/v/missing",
    }
