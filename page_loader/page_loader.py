import requests
import os
import argparse
import re


def main():
    parser = argparse.ArgumentParser(description='Page Loader')

    parser.add_argument('url_page')
    parser.add_argument('-o', '--output', default=os.getcwd(),
                        help='dir for output')

    args = parser.parse_args()

    url_page = vars(args)['url_page']
    dir_path = vars(args)['output']

    # url_page = 'https://ru.hexlet.io/courses'
    download(url_page, dir_path)


def url_converter(file_path):
    file_path = file_path.replace('https://', '').replace('http://', '')
    file_path = re.sub('\W', '-', file_path)
    file_path += '.html'
    return file_path


def download(url_page, dir_path):

    r = requests.get(url_page, allow_redirects=True)

    file_path = url_converter(url_page)
    print(file_path)
    file_path = os.path.join(dir_path, file_path)

    with open (file_path, 'w', encoding='UTF-8') as file:
        file.write(r.text)
    
    return file_path


if __name__ == '__main__':

    main()

