#!/usr/bin/env python3
"""
Audiophile Music Curator - Local-First & Graceful Fallback Engine
Probes local Ollama (port 11434). If active, runs local inference on RTX 4070.
If offline, signals fallback to free cloud subagent tier ($0 cost guaranteed).
"""
import json
import urllib.request
import urllib.error

OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
DEFAULT_MODEL = "deepseek-r1:14b"


def is_ollama_available(timeout=1.5) -> bool:
    try:
        req = urllib.request.Request("http://127.0.0.1:11434/api/tags")
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status == 200
    except Exception:
        return False


def query_local_or_signal_fallback(prompt: str, model: str = DEFAULT_MODEL) -> dict:
    if not is_ollama_available():
        return {
            "tier": 2,
            "engine": "fallback_cloud_free",
            "message": "Yerel Ollama kapalı veya ulaşılamıyor. Ücretsiz dahili alt ajan (Tier 2) devreye alınıyor."
        }
    
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.6,
            "num_predict": 1200
        }
    }
    
    try:
        req = urllib.request.Request(
            OLLAMA_URL,
            data=json.dumps(payload).encode('utf-8'),
            headers={"Content-Type": "application/json"}
        )
        with urllib.request.urlopen(req, timeout=90) as resp:
            res_data = json.loads(resp.read().decode('utf-8'))
            return {
                "tier": 1,
                "engine": f"local_ollama_{model}",
                "response": res_data.get("response", "")
            }
    except Exception as e:
        return {
            "tier": 2,
            "engine": "fallback_cloud_free",
            "error": str(e),
            "message": "Yerel çıkarım sırasında hata oluştu. Ücretsiz dahili alt ajan devreye alınıyor."
        }


if __name__ == "__main__":
    import sys
    test_prompt = sys.argv[1] if len(sys.argv) > 1 else "Merhaba! Aktif misin?"
    res = query_local_or_signal_fallback(test_prompt)
    print(json.dumps(res, ensure_ascii=False, indent=2))
