# Gera as fotos que faltam em fotos/<pagina>/<id>.jpg via Space FLUX.1-Krea-dev.
# Uso: HF_TOKEN=... python3 gerar_fotos.py [lab|radar] [ids...]
import os, sys, shutil
from gradio_client import Client
from PIL import Image
sys.path.insert(0, os.path.dirname(__file__))
from fotos import PROMPTS

BASE = os.path.join(os.path.dirname(__file__), "fotos")
pages = [sys.argv[1]] if len(sys.argv) > 1 else list(PROMPTS)
only = set(sys.argv[2:])
client = Client("mcp-tools/FLUX.1-Krea-dev", hf_token=os.environ.get("HF_TOKEN"))
for pg in pages:
    os.makedirs(f"{BASE}/{pg}", exist_ok=True)
    for pid, prompt in PROMPTS[pg].items():
        dst = f"{BASE}/{pg}/{pid}.jpg"
        if os.path.exists(dst) or (only and pid not in only):
            continue
        res = client.predict(prompt=prompt, seed=0, randomize_seed=True, width=1024, height=1280,
                             guidance_scale=4.5, num_inference_steps=24, api_name="/infer")
        path = res[0] if isinstance(res, (list, tuple)) else res
        Image.open(path).convert("RGB").save(dst, quality=92)
        print("ok", dst, flush=True)
