from checkout import checkout, USER_FOLDER, OUT_FOLDER, FOLDER_FOLDER, TEXT_HEADERS_ERROR


def test_step1():
    # test1
    assert checkout(f'cd {USER_FOLDER}/{OUT_FOLDER}; 7z e bad.7z -o{USER_FOLDER}/{FOLDER_FOLDER} -y',
                    TEXT_HEADERS_ERROR), "test1 FAIL"


def test_step2():
    # test2
    assert checkout(f'cd {USER_FOLDER}/{OUT_FOLDER}; 7z e bad.7z -o{USER_FOLDER}/{FOLDER_FOLDER} -y',
                    TEXT_HEADERS_ERROR), "test2 FAIL"
