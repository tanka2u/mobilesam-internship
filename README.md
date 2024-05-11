Internship Take Home Assignment - Software Engineer:

I made microservices for image processing. I have windows, so, I am writing accordingly.

How to run the code:

1. Activate the virtual Environment.
   source venv/Scripts/activate
2. install the fastapi and run:
   uvicorn app:app --reload(It will starts the FastAPI server)

3. I use postman for testing which give me success result.
4. Task complition: MobileSam Segmentation Model Service

   I developed a FastAPI service to deploy the MobileSam segmentation model, containerize the service with Docker, and ensure efficient interaction with the model on the CPU.

   I created a microservices that allows users to interact with this model via an API. The script is found in app.py and a function segment_everything is imported from image_module.py that takes an image as input and returns the segmentation result.

5. Docker Familiarity: I have containerize the service using docker.
   I create Dockerfile, READMEDocker.md, compose.yaml and .dockerignore file.

How to build file using Docker:

    1. Activate the virtual Environment.
    sourc venv/Scripts/activate

    2. In docker file I create necessary settings and requirements.
    3. add fastapi and uvicorn in requirements.txt file.
    3. To build docker container first run docker desktop and type the command below
    	docker compose up --build (It will run docker)
    4. I use postman for testing which give me success result.
