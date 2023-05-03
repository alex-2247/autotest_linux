'''Задание 2. (повышенной сложности)
Доработать функцию из предыдущего задания таким образом, чтобы у неё появился дополнительный режим
работы, в котором вывод разбивается на слова с удалением всех знаков пунктуации (их можно взять из
списка string.punctuation модуля string). В этом режиме должно проверяться наличие слова в выводе.'''
import subprocess
import string


def run_n_textfind(run_command:str, find_text:str) -> bool:
    run_out = subprocess.run(run_command, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    file_content = run_out.stdout
    for item in string.punctuation:
        file_content = file_content.replace(item, " ")
    return (run_out.returncode == 0) and (find_text in file_content)


if __name__ == '__main__':
    print("Проверяем работу функции на тестовых примерах\n")

    comm = "cat /etc/os-release"
    txt = "VERSION"
    print(f'Команда: {comm},   текст: {txt},   результат: {run_n_textfind(comm, txt)}\n')

    comm = "cat /etc/es-rilaised"
    txt = "VERSION"
    print(f'Команда: {comm},   текст: {txt},   результат: {run_n_textfind(comm, txt)}\n')

    comm = "cat /etc/os-release"
    txt = "jimmi"
    print(f'Команда: {comm},   текст: {txt},   результат: {run_n_textfind(comm, txt)}\n')

    comm = "cat /etc/os-release"
    txt = "jammy"
    print(f'Команда: {comm},   текст: {txt},   результат: {run_n_textfind(comm, txt)}\n')
