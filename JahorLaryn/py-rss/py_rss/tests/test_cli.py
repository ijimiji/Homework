from cli import *
from datetime import datetime
from types import SimpleNamespace


def test_args_handler():
    args = SimpleNamespace(
        source="foo",
        daemon=False,
        date=None,
        version=False,
        json=False,
        verbose=False,
        to_epub=False,
        to_html=False,
        limit=None,
    )
    time = datetime.now().strftime("%Y%d%m")
    out = {
        "version": py_rss_version,
        "limit": None,
        "json": False,
        "date": time,
        "daemon": False,
        "verbose": False,
        "export_queue": [None, None],
        "source": "foo",
    }
    assert handle_args(args) == out


def test_xml_header():
    assert "<h1>foo</h1>" == xml_header("foo")


def test_xml_paragraph():
    assert "<p>foo</p>" == xml_paragraph("foo")


def test_xml_link():
    assert '<a href="foo">foo</a>' == xml_link("foo")


def test_xml_image():
    assert '<img align="center" src="foo"></image>' == xml_image("foo")


def test_html_converter():
    html = """
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <title>py-rss</title>
    </head>
    <body>
        <h1>This document was generated by py-rss</h1>
        <h1>Unnamed article</h1><img align="center" src="https://content.onliner.by/news/thumbnail/2c088b3d36e457c5659a3818c9fd840b.jpeg"></image><p>В любимый белорусами масс-маркет привезли огромное количество зимней верхней одежды. Радует, что многое из представленного подходит для прям-таки настоящей суровой зимы. Осталось только определиться, как совместить тепло со стилем. Onlíner сходил в наиболее востребованные магазины одежды вместе со стилистом Валерией Скочеенковой и сделал обзор самых модных пуханов, пальто и шуб. В качестве моделей — фешен-журналист Лора и симпатичный парень Никита. Читать далее…</p><a href="https://people.onliner.by/2021/10/24/obzor-verxnej-odezhdy-2">https://people.onliner.by/2021/10/24/obzor-verxnej-odezhdy-2</a>
    </body>
</html>"""
    news = [
        {
            "title": "Unnamed article",
            "link": "https://people.onliner.by/2021/10/24/obzor-verxnej-odezhdy-2",
            "description": "В любимый белорусами масс-маркет привезли огромное количество зимней верхней одежды. Радует, что многое из представленного подходит для прям-таки настоящей суровой зимы. Осталось только определиться, как совместить тепло со стилем. Onlíner сходил в наиболее востребованные магазины одежды вместе со стилистом Валерией Скочеенковой и сделал обзор самых модных пуханов, пальто и шуб. В качестве моделей — фешен-журналист Лора и симпатичный парень Никита.\xa0Читать далее…",
            "pubdate": "Sun, 24 Oct 2021 11:00:13 +0300",
            "image": "https://content.onliner.by/news/thumbnail/2c088b3d36e457c5659a3818c9fd840b.jpeg",
            "channel_title": "Люди Onlíner",
        }
    ]
    RSSExporter(news).as_html()
    with open(f"{news[0]['channel_title']}.html") as file:
        assert file.read() == html
