import os
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from PIL import Image
from image_module import segment_everything
import io



app = FastAPI()


def process_image(image):
    try:
        result = segment_everything(image)
        return result
    except Exception as e:
        print(f"Error processing image: {e}")
        return None




@app.post("/test")
async def test(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents)).convert("RGB")
    print(image)
    result = process_image(image=image)
    print(result)
    return JSONResponse(content={"result": image})


@app.post("/segment-image")
async def segment_image(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents)).convert("RGB")
    print(image)
    result = process_image(image=image)
    output_path = "generated/random.png"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    result.save(output_path)
    return JSONResponse(content={"Success": f"Image process sucess, please find the generated file {output_path}"})
