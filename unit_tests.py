import mainws

try:
    # Test get_html() with a URL
    assert mainws.get_html('https://www.google.com') != None
    # Test get_html() with a file
    assert mainws.get_html('test_pages/test.html') != None
    # Test error_log()
    assert mainws.error_log('Test error') == None
    # Test error_log() with an exception
    assert mainws.error_log(Exception) == None
    # test get_html() with an exception
    assert mainws.get_html('https://www.google') == None
    # test get_html() with an exception
    assert mainws.get_html('tests/test') == None
except AssertionError as e:
    print('Test failed!',e)
    exit(1)
finally:
    print('All tests passed!')
    exit(0)