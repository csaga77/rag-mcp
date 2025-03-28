# Godot RAG MCP

A Model Context Protocol (MCP) tool that retrieves relevant information about Godot game engine from a local ChromaDB database.

It's recommended to use the [website2embeddings](https://github.com/zivshek/website2embeddings) tool to create the chroma vector store.

Although this tool is for Godot in particular, but with small changes to the tool description, it can be used for any chroma database.

## Configuration with Visual Studio Code

The system is configured through `settings.json`:

```json
"mcp": {
    "inputs": [],
    "servers": {
        "godot_rag": { // or whatever name you want
            "command": "cmd", // repace this with "uv" on Mac or Linux
            "args": [
                "/c", // remove this on Mac or Linux
                "uv", // remove this on Mac or Linux
                "run",
                "path to the server script 'server.py'",
                "-d",
                "path to the chroma_db on your computer",
                "-c",
                "name of the collection in the chroma_db"
            ]
        }
    }
}
```
