FROM python

# Create the user that will run the app
RUN adduser --disabled-password --gecos '' user

WORKDIR /opt/scallshap


# Install requirements, including from Gemfury
ADD ./ /opt/scallshap
RUN apt-get update -y

RUN chmod +x /opt/scallshap/download_data.sh
RUN chmod +x /opt/scallshap/run.sh
RUN chown -R user:user ./

RUN apt-get install -y gnumeric 
RUN mkdir /opt/scallshap/data &&\
    cd /opt/scallshap/data &&\
    curl -O 'https://archive.ics.uci.edu/ml/machine-learning-databases/00350/default%20of%20credit%20card%20clients.xls' &&\
    ssconvert default%20of%20credit%20card%20clients.xls data1.csv &&\
    grep -v "X1" data1.csv > data.csv
RUN cd /opt/scallshap/
RUN pip install -U pytest
RUN pip install -r /opt/scallshap/requirements_dev.txt

USER user

CMD ["bash", "./run.sh"]