from datetime import datetime
from pathlib import Path
from typing import List


def create_html_list(root_directory: Path, html_files: List[Path], title: str) -> str:
    """
    HTMLファイルのリストからリンク付きのHTMLを生成する

    Args:
        root_directory (Path): ルートディレクトリのPathオブジェクト
        html_files (List[Path]): .htmlファイルのPathオブジェクトのリスト
        title (str): HTMLページのタイトル

    Returns:
        str: 生成されたHTML文字列
    """
    # HTMLの基本構造を作成
    # メタデータとスタイルを追加して、ページの見た目と機能性を向上
    html_content = f"""
    <!DOCTYPE html>
    <html lang="ja">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="description" content="{title}のファイルインデックス">
        <title>{title}</title>
        <style>
            body {{ font-family: Arial, sans-serif; line-height: 1.6; padding: 20px; }}
            h1 {{ color: #333; }}
            ul {{ list-style-type: none; padding: 0; }}
            li {{ margin-bottom: 10px; }}
            a {{ color: #0066cc; text-decoration: none; }}
            a:hover {{ text-decoration: underline; }}
        </style>
    </head>
    <body>
        <h1>{title}</h1>
        <ul>
    """

    # 各HTMLファイルに対してリンクを生成
    for html_file in sorted(html_files):  # ファイルを名前順にソート
        # ファイルの相対パスを取得し、リンクとして使用
        relative_path = html_file.relative_to(root_directory)
        html_content += f"""
        <li>
            <a href="{relative_path}">{relative_path}</a>
        </li>"""

    # HTMLの閉じタグを追加
    html_content += """
        </ul>
    </body>
    </html>
    """

    return html_content


def get_html_files(directory: Path) -> List[Path]:
    """
    指定されたディレクトリ以下の全HTMLファイルを再帰的に取得する

    Args:
        directory (Path): 探索を開始するディレクトリのPathオブジェクト

    Returns:
        List[Path]: 見つかったHTMLファイルのPathオブジェクトのリスト
    """
    # 指定されたディレクトリ以下の全HTMLファイルを再帰的に取得
    return list(directory.rglob("*.html"))


def save_html_content(content: str, output_path: Path) -> None:
    """
    生成したHTMLコンテンツをファイルに保存する

    Args:
        content (str): 保存するHTMLコンテンツ
        output_path (Path): 出力先のファイルパス
    """
    output_path.write_text(content, encoding="utf-8")
    print(f"HTMLリストが {output_path} に生成されました。")


def main() -> None:
    """
    メイン関数：HTMLファイルのリストを取得し、リンク付きのHTMLを生成して保存する
    """
    # HTMLファイルのリストを再帰的に取得
    root_directory = Path(".")
    html_files = get_html_files(directory=root_directory)
    print(f"見つかったHTMLファイルの数: {len(html_files)}")

    # リンク付きのHTMLを生成
    html_content = create_html_list(
        root_directory=root_directory, html_files=html_files, title="neoAPI"
    )

    # 生成したHTMLを保存
    output_path = Path("index.html")
    save_html_content(content=html_content, output_path=output_path)


if __name__ == "__main__":
    main()
