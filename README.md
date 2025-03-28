# Godot RAG MCP Tool

A Model Context Protocol (MCP) tool that retrieves relevant information about Godot game engine from a local ChromaDB database.

It's recommended to use the [website2embeddings](https://github.com/zivshek/website2embeddings) tool to create the chroma vector store.

## Configuration with Visual Studio Code

The system is configured through `settings.json`:

```json
"mcp": {
    "inputs": [],
    "servers": {
        "godot_rag": {
            "command": "cmd", // repace this with "uv" on Mac or Linux
            "args": [
                "/c", // remove this on Mac or Linux
                "uv", // remove this on Mac or Linux
                "run",
                "G:\\repos\\rag_mcp\\server.py", // path to the server script
                "-d",
                "G:\\repos\\web2embedding\\artifacts\\vector_stores\\chroma_db", // path to the chroma_db
                "-c",
                "chunks_SZ_400_O_20_sentence-transformers_all-MiniLM-L6-v2" // name of the collection in the chroma_db
            ]
        }
    }
}
```