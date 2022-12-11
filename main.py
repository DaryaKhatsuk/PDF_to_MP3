from gtts import gTTS
from art import tprint
import pdfplumber
from pathlib import Path


def pdf_mp3(file_path="test.pdf", language='en'):
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        # return 'File exists'
        print(f'File {file_path} processing...')
        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]
        text = ''.join(pages)
        text = text.replace('\n', '')
        new_audio = gTTS(text=text, lang=language)
        file_name = Path(file_path).stem
        new_audio.save(f'{file_name}.mp3')
        return f'{file_name}.mp3 saved'
    else:
        return 'File not exists, check the file path'


def main():
    tprint('PDF>>>TO>>>MP3', font='small')
    file_path = input("\nEnter a file's path: ")
    language = input("Choose language, for example 'en' or 'ru': ")
    print(pdf_mp3(file_path=file_path, language=language))


if __name__ == '__main__':
    main()
