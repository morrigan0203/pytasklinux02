import subprocess
from checkout import checkout, USER_FOLDER, TST_FOLDER, OUT_FOLDER, TEXT_OK


def test_step1():
    # test1
    res1 = checkout(f'cd {USER_FOLDER}; 7z a {OUT_FOLDER}/arx4 {TST_FOLDER}', TEXT_OK)
    hashcrc32 = subprocess.run(f'cd {USER_FOLDER}/{OUT_FOLDER}; crc32 arx4.7z',
                               shell=True, stdout=subprocess.PIPE, encoding='utf-8').stdout.upper()
    res2 = checkout(f'cd {USER_FOLDER}/{OUT_FOLDER}; 7z h arx4.7z', hashcrc32)
    assert res1 and res2, "test1 FAIL"

