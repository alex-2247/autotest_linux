'''Задание 1.    Условие:
Написать функцию на Python, которой передаются в качестве параметров команда и текст. Функция
должна возвращать True, если команда успешно выполнена и текст найден в её выводе и False в
противном случае. Передаваться должна только одна строка, разбиение вывода использовать не нужно.'''
import subprocess


def run_n_textfind(run_command: str, find_text: str) -> bool:
    run_out = subprocess.run(run_command, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    file_content = run_out.stdout
    return run_out.returncode == 0 and find_text in file_content


if __name__ == '__main__':
    print("Проверяем работу функции на тестовых примерах")

    comm = "cat /etc/os-release"
    txt = "22.04.1"
    print(f'Команда: {comm},   текст: {txt},   результат: {run_n_textfind(comm, txt)}')

    comm = "cat /etc/os-release"
    txt = "32.04.1"
    print(f'Команда: {comm},   текст: {txt},   результат: {run_n_textfind(comm, txt)}')

    comm = "cat /etc/es-rilaised"
    txt = "VERSION_CODENAME=jammy"
    print(f'Команда: {comm},   текст: {txt},   результат: {run_n_textfind(comm, txt)}')

    comm = "cat /etc/os-release"
    txt = "jammy"
    print(f'Команда: {comm},   текст: {txt},   результат: {run_n_textfind(comm, txt)}')
