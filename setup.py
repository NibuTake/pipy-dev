from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# long_description(後述)に、GitHub用のREADME.mdを指定
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="koban",  # パッケージ名(プロジェクト名)
    packages=["koban"],  # パッケージ内(プロジェクト内)のパッケージ名をリスト形式で指定
    version="1.0.1",  # バージョン
    license="MIT",  # ライセンス
    install_requires=[""],  # pip installする際に同時にインストールされるパッケージ名をリスト形式で指定
    author="nibutake",  # パッケージ作者の名前
    author_email="0815takeshi@gmail.com",  # パッケージ作者の連絡先メールアドレス
    description="Testing",  # パッケージの簡単な説明
    long_description=long_description,  # PyPIに'Project description'として表示されるパッケージの説明文
    long_description_content_type="text/markdown",
    keywords="koban",  # PyPIでの検索用キーワードをスペース区切りで指定
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
    ],
)
