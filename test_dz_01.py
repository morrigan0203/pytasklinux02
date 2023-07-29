from checkout import checkout, USER_FOLDER, TST_FOLDER, OUT_FOLDER, FOLDER_FOLDER, TEXT_OK, FILE


def test_step1():
    # test1
    res1 = checkout(f'cd {USER_FOLDER}; 7z a {OUT_FOLDER}/arx3 {TST_FOLDER}', TEXT_OK)
    res2 = checkout(f'cd {USER_FOLDER}/{OUT_FOLDER}; 7z x arx3.7z -o{USER_FOLDER}/{FOLDER_FOLDER} -y', TEXT_OK)
    res3 = checkout(f'ls {USER_FOLDER}/{FOLDER_FOLDER}', TST_FOLDER)
    res4 = checkout(f'ls {USER_FOLDER}/{FOLDER_FOLDER}/{TST_FOLDER}', FILE)
    assert res1 and res2 and res3 and res4, "test1 FAIL"
