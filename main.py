!pip install google-genai
from google import genai
from IPython.display import display, Markdown

# 1. 準備
client = genai.Client(api_key="YOUR_API_KEY_HERE")
print("====================================")
print("🤖 LLMOコンテンツ生成システムへようこそ")
print("====================================")

# 2. ユーザーにキーワードを入力させる画面を作る
keyword = input("① 記事のメインキーワードを入力してください（例：営業DX）: ")
summary = input("② この記事で伝えたい内容（概要）を簡単に入力してください: ")
print("====================================\n")

# 3. AIへの「LLMO特化の指示書（プロンプト）」を作る
title_prompt = f"""
あなたは優秀なSaaS企業のマーケターです。
以下のキーワードと概要について、ChatGPTなどのLLMに「引用・推薦されやすい（LLMO）」ブログ記事のタイトル案を5つ出力してください。

【キーワード】: {keyword}
【伝えたい概要】: {summary}

【LLMO最適化のための必須条件】
1. 感情的な煽り文句は排除し、客観的でフラットなトーンにすること。
2. AIが事実（ファクト）として抽出しやすいよう、具体的な数値（％や時間）を仮想で良いので含めること。

"""

print("AIがLLMOに最適なタイトル案を考えています...（数秒お待ちください）\n")

title_response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=title_prompt
)

# 5. タイトル案を表示する
print("--- 🎯 AIが生成したタイトル案 ---")
print(title_response.text)
print("\n====================================")

# 4. タイトルを選んで記事本文を生成する
selected_title = input("③ 上記から記事にしたいタイトルを1つコピーして貼り付けてください: ")
print("====================================\n")

article_prompt = f"""
あなたは優秀なSaaS企業のコンテンツマーケターです。
以下のタイトルで、AI（LLM）に引用・推薦されやすいブログ記事の本文を作成してください。

【選択されたタイトル】: {selected_title}
【記事の前提となる概要】: {summary}

【LLMO最適化のための記事構成ルール】
1. 構成：「導入」「見出し2（複数）」「見出し3」「まとめ」の構造を厳守すること。
2. 結論ファースト：導入部分で「この記事で解決できる課題と結論」を明確に述べること。
3. 構造化データ：AIが情報を抽出しやすいように、「箇条書き」や「比較表（マークダウン形式）」を必ず使うこと。
"""

print("選ばれたタイトルをもとに、AIが記事本文を執筆しています...（10〜20秒お待ちください）\n")

article_response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=article_prompt
)

# 5. 最終結果を綺麗に表示
print("--- 📝 完成したLLMO最適化記事 ---")
display(Markdown(article_response.text))
