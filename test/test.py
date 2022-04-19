import pytest
import tonos_ts4.ts4 as ts4

from contracts import Contract

@pytest.mark.parametrize(
    argnames=['x'],
    argvalues=[
        (123,),
        (321,),
    ]
)
@pytest.mark.parametrize(
    argnames=['y'],
    argvalues=[
        (123,),
        (321,),
    ]
)
def test(pytestconfig, x, y):
    ts4.reset_all()
    rootpath = pytestconfig.rootpath
    ts4.init(rootpath.joinpath('../target/'), verbose=False)

    contract = Contract()
    assert contract.call_getter('val') == 0

    contract.add(x)
    ts4.dispatch_messages()

    assert contract.call_getter('val') == x

    contract.add(y)
    ts4.dispatch_messages()

    assert contract.call_getter('val') == x + y
