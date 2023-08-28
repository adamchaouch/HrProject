FROM python:3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
WORKDIR /usr/src/app

# Copy requirements.txt and install dependencies
COPY ./requirements.txt /usr/src/app/
RUN apt-get update &&\
    apt-get install -y binutils libproj-dev gdal-bin
    
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy the rest of the application files
COPY . /usr/src/app/

# Set the entry point
# COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
# ENTRYPOINT [ "/usr/src/app/entrypoint.sh" ]