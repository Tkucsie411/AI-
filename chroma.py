import os
import openai
import chromadb
import pandas as pd
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import Document, VectorStoreIndex, StorageContext, SimpleDirectoryReader

#設定 OpenAI API
os.environ["OPENAI_API_KEY"] = "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"  # 🔹記得替換你的 API Key

#設定 OpenAI LLM 和嵌入模型
llm = OpenAI(model="gpt-4")  # 使用 GPT-4
embed_model = OpenAIEmbedding(model="text-embedding-ada-002")  # 適用於向量嵌入

#讀取 PDF 檔案
pdf_documents = SimpleDirectoryReader(input_dir="./113_1", required_exts=[".pdf"]).load_data()

#讀取 Excel 檔案
excel_documents = []
excel_file_path = "./data/sample.xlsx"  #請修改為你的 Excel 路徑
if os.path.exists(excel_file_path):
    df = pd.read_excel(excel_file_path)  # 讀取 Excel
    for index, row in df.iterrows():
        text = " ".join([str(val) for val in row.values])  # 把每一行轉成文字
        excel_documents.append(Document(text=text))

#合併 PDF 與 Excel 內容
documents = pdf_documents + excel_documents

#連接 ChromaDB
chroma_client = chromadb.PersistentClient(path="./chroma_db")
chroma_collection = chroma_client.get_or_create_collection("quickstart")

#建立 Chroma Vector Store
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
storage_context = StorageContext.from_defaults(vector_store=vector_store)

#建立 Index 並存入 ChromaDB
index = VectorStoreIndex.from_documents(
    documents, 
    storage_context=storage_context, 
    embed_model=embed_model  # 使用 OpenAI 嵌入模型
)

#檢查 ChromaDB 內容
print(chroma_collection.get())
