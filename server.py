from mcp.server.fastmcp import FastMCP
import chromadb
from sentence_transformers import SentenceTransformer
import argparse

mcp = FastMCP("Godot RAG Server")

client: chromadb.PersistentClient
collection: chromadb.Collection
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

@mcp.tool()
def get_godot_context(query: str) -> list:
    """
    Godot engine has evolved a lot, and a lot of the pretrained knowledge is outdated and cannot be relied on.
    This tool retrieves a list of the latest relevant Godot documentation snippets based on the provided query.
    If user askes anything related to the Godot engine, including api and class references, even you are confident,
    this function should still be called. If there is any conflict between your knowledge and the retrieved snippets,
    the snippets should be considered more reliable, otherwise it's okay to rely on your knowledge. Only call this
    function if you are certain it's about the Godot engine.
    
    Args:
        query: keywords related to Godot engine
        
    Returns:
        list of relevant Godot documentation/references snippets
    """
    try:
        results = collection.query(
            query_embeddings=model.encode([query]).astype(float).tolist(), n_results=20)
        
        # based on your data, you may include other info such as metadata, etc.
        documents = results["documents"][0][:]
        
        return documents
    except Exception as e:
        return {"error": f"Failed to query ChromaDB: {str(e)}"}
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Start the Godot RAG MCP Server')
    parser.add_argument('--chromadb-path', '-d', type=str, 
                        help='Path to the ChromaDB database',
                        default="../web2embeddings/artifacts/vector_stores/chroma_db")
    parser.add_argument('--collection-name', '-c', type=str, 
                        help='Name of the ChromaDB collection to query',
                        default="godotengine_chunks_SZ_400_O_20_all-MiniLM-L6-v2")
    
    args = parser.parse_args()
    
    client = chromadb.PersistentClient(path=args.chromadb_path)
    # Retrieve the list of collections
    collections = client.list_collections()

    # Print the collections
    for collection in collections:
        print(collection)

    collection = client.get_collection(args.collection_name)
    
    mcp.run(transport="stdio")