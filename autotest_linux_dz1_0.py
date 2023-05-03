'''Самостоятельная работа (сдавать не обязательно)
Доработать тест на питоне из предыдущего задания таким образом,
чтобы вывод сохранялся построчно в список и в тесте проверялось, что в этом списке есть
строки VERSION="22.04.1 LTS (Jammy Jellyfish)" и VERSION_CODENAME=jammy.
Проверка должна выполняться только если код возврата равен 0.'''
import subprocess

if __name__ == '__main__':
    run_out = subprocess.run("cat /etc/os-release", shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    print('"Грязный" вывод:\n', run_out, '\n')
    file_content = run_out.stdout
    print('Вывод построчно:\n', file_content, '\n')

    content_list = file_content.split('\n')
    print('Вывод LIST:\n', file_content, '\n')

    if run_out.returncode == 0:
        if 'VERSION="22.04.1 LTS (Jammy Jellyfish)"' in content_list \
                        and 'VERSION_CODENAME=jammy' in content_list:
            print("SUCCESS")
        else:
            print("substrings exist FAIL")
    else:
        print("file read FAIL")
