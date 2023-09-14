
import pytest
# python -m pytest -v -s .\FixtureScope.py .\Fixtures.py


@pytest.fixture(scope='session', autouse=True)
def setup_session(request):
    print('\nSetup Session')
    # yield either this or addfinallizer can be used,but we can add multiple finalizers using addfinalizer
    yield
    print('\nTeardown Session')


@pytest.fixture(scope='module', autouse=True)
def setup_module(request):
    print('\nSetup Module')
    # yield either this or addfinallizer can be used,but we can add multiple finalizers using addfinalizer
    yield
    print('\nTeardown Module')


@pytest.fixture(scope='class', autouse=True)
def setup_class(request):
    print('\nSetup Class')
    # yield either this or addfinallizer can be used,but we can add multiple finalizers using addfinalizer
    yield
    print('\nTeardown Class')


@pytest.fixture(scope='function', autouse=True)
def setup_function(request):
    print('\nSetup Function')
    # yield either this or addfinallizer can be used,but we can add multiple finalizers using addfinalizer
    yield
    print('\nTeardown Function')


class TestClass:
    def test_1(self):
        print("Executing Test1")
        assert True

    def test_2(self):
        print("Executing Test2")
        assert True
