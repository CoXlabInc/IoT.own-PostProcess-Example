FROM python

WORKDIR /root

RUN python3 -m pip install pyiotown==0.3.1

COPY ./PostProcess /root/
CMD python3 PostProcessExample.py
