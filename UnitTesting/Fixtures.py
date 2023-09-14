import pytest


@pytest.fixture()
def setup1(request):
    print('\nSetup 1')
    # yield either this or addfinallizer can be used,but we can add multiple finalizers using addfinalizer
    yield
    print('\nTeardown 1')


@pytest.fixture()
def setup2(request):
    print('\nSetup A')
    # yield either this or addfinallizer can be used,but we can add multiple finalizers using addfinalizer

    def teardown_1():
        print('\nTeardown A')
    request.addfinalizer(teardown_1)

    def teardown_2():
        print('\nTeardown A')
    request.addfinalizer(teardown_2)


def test_1():  # def test_1(setup):
    print("Executing Test1")
    assert True


# @pytest.mark.usefixtures('setup')
def test_2():
    print("Executing Test2")
    assert True
