def read_files(paths):
    print(type(paths))
    """ if type(paths) == 'string':
        print(type(paths)) """


def test_reads():
    assert read_files("teste")
