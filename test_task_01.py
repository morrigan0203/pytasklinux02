from checkout import checkout, USER_FOLDER, OUT_FOLDER, TST_FOLDER, FOLDER_FOLDER, TEXT_OK, FILE


def test_step1():
    # test1
    res1 = checkout(f'cd {USER_FOLDER}/{TST_FOLDER}; 7z a {USER_FOLDER}/{OUT_FOLDER}/arx2', TEXT_OK)
    res2 = checkout(f'ls {USER_FOLDER}/{OUT_FOLDER};', "arx2.7z")
    assert res1 and res2, "test1 FAIL"


def test_step2():
    # test2
    res1 = checkout(f'cd {USER_FOLDER}/{OUT_FOLDER}; 7z e arx2.7z -o{USER_FOLDER}/{FOLDER_FOLDER} -y', TEXT_OK)
    res2 = checkout(f'ls {USER_FOLDER}/{FOLDER_FOLDER}', FILE)
    assert res1 and res2, "test2 FAIL"


def test_step3():
    # test3
    assert checkout(f'cd {USER_FOLDER}/{OUT_FOLDER}; 7z t arx2.7z', TEXT_OK), "test3 FAIL"


def test_step4():
    # test4
    res1 = checkout(f'cd {USER_FOLDER}/{OUT_FOLDER}; 7z d arx2.7z', TEXT_OK)
    res2 = checkout(f'cd {USER_FOLDER}/{OUT_FOLDER}; 7z l arx2.7z', "0 files")
    assert res1 and res2, "test4 FAIL"


def test_step5():
    # test5
    assert checkout(f'cd {USER_FOLDER}/{OUT_FOLDER}; 7z u arx2.7z {USER_FOLDER}/{TST_FOLDER}/{FILE}', TEXT_OK), \
        "test5 FAIL"

