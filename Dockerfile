FROM python:3.8-slim

# set the working directory in the container
WORKDIR /app

# copy the code into the container
COPY . /app

# install the dependencies
RUN pip install -r requirements.txt

# run the code
CMD ["python", "summarization.py"]