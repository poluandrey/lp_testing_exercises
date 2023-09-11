from functions.level_1.three_url_builder import build_url


def test_build_url__without_params():
    assert build_url('example.com', 'home') == 'example.com/home', 'url_builder without params work incorrectly'


def test_build_url__with_one_params():
    assert build_url('example.com', 'home', {'username': 'Andrey'}) == 'example.com/home?username=Andrey', 'url_builder with one param work incorrectly'


def test_build_url__with_few_params():
    assert build_url('example.com', 'home', {'username': 'Andrey', 'group': 'my_group'}) == 'example.com/home?username=Andrey&group=my_group', 'url builder with few params work incorrectly'

