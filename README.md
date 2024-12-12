# LANGGRAPH-DATAVIZ

## RUN LLM
```shell
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
docker exec -it ollama ollama run llama3.1

curl http://localhost:11434/api/generate -d '{
  "model": "phi",
  "prompt": "There once was a mouse named",
  "raw": true,
  "stream": false
}'
```

other models https://ollama.com/library